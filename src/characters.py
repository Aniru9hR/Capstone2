import requests
import pandas as pd
import numpy as np


class Characters:
# Define URL to get data from all characters
    def __init__(self):
        self.api_url = 'https://swapi.dev/api/people/'

        self.get_data()
  
# Scrape API Data for all the pages of characters
    def get_data(self):
        self.characters_list = []
        while True:
            response = requests.get(self.api_url)
            characters = response.json().get('results')
            self.characters_list.append(characters)
            if response.json().get('next') is None:
                break
            self.api_url = response.json().get('next')
        
        return self.get_char_data()

    def get_char_data(self):
        char_list = []
        for characters in self.characters_list:
            for character in characters:
                homeworld = character.get('homeworld')
                if homeworld:
                    response = requests.get(homeworld)
                    homeworld_response = response.json()
                if len(character.get('films')) > 0:
                    self.film_urls = character.get('films')
                    film_list = self.get_films()
                if len(character.get('starships')) > 0:
                    self.starship_urls = character.get('starships')
                    starships_list = self.get_starships()
                char = {
                    "name": character.get("name"),
                    "height": character.get("height"),
                    "mass": character.get("mass"),
                    "gender": character.get("gender"),
                    "hair_color": character.get("hair_color"),
                    "skin_color": character.get("skin_color"),
                    "homeworld": homeworld_response.get("name"),
                    "films": film_list,
                    "starships": starships_list
                }
                char_df = pd.DataFrame.from_dict(char, orient='index').transpose()
                char_list.append(char_df)
        self.character_df = pd.concat(char_list)
        self.character_df = self.character_df.replace(np.nan, None)
        self.character_df = self.character_df.replace('none', 'None')
        return self.character_df

    def get_films(self):
        film_response_list = []
        for url in self.film_urls:
            response = requests.get(url)
            film_response = response.json()
            film_response_name = film_response.get('title')
            film_response_list.append(film_response_name)
            return film_response_list

    def get_starships(self):
        starship_response_list = []
        for url in self.starship_urls:
            response = requests.get(url)
            starship_response = response.json()
            starship_response_name = starship_response.get('name')
            starship_response_list.append(starship_response_name)
        return starship_response_list
        

if __name__ == '__main__':
    c = Characters()
    c.character_df.to_csv('src/data/character_data.csv', index=False)
    