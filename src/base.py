import requests
import pandas as pd


class Base:

# Define URL to get data from all films
    def __init__(self):
        self.api_url = 'https://swapi.dev/api/films/'
        self.get_data()
    
# Scrape API Data for all the pages of films
    def get_data(self):
        response = requests.get(self.api_url)
        print(response)
        if response:
            films_data = response.json()
            print(response.json())
            film_df = pd.DataFrame.from_dict(films_data.get("results"))
            print(film_df)
            film_df['character_count'] = film_df.characters.apply(len)
            film_df['planets_count'] = film_df.planets.apply(len)
            film_df['starships_count'] = film_df.starships.apply(len)
            film_df['vehicles_count'] = film_df.vehicles.apply(len)
            film_df['species_count'] = film_df.species.apply(len)
            self.df = film_df.filter(['title', 'director',
                                            'release_date',
                                            'character_count',
                                            'planets_count',
                                            'starships_count',
                                            'vehicles_count',
                                            'species_count'], axis=1)
            return self.df
        

if __name__ == '__main__':
    c = Base()
    c.df.to_csv('src/data/films_data.csv', index=False)
    