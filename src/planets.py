import requests
import pandas as pd


class Planets:
# Define URL to get data from all planets
    def __init__(self):
        self.api_url = 'https://swapi.dev/api/planets/'
        self.get_data()

# Scrape API Data for all the pages of planets  
    def get_data(self):
        planets_list = []
        while True:
            response = requests.get(self.api_url)
            print(response)
            if response:
                self.planets = response.json().get("results")
                df = self.get_planets_list()
                if response.json().get('next') is None:
                    break
                self.api_url = response.json().get('next')
                planets_list.append(df)
        self.planets_df = pd.concat(planets_list)
        self.planets_df = self.planets_df.fillna('NA')
        return self.planets_df

    def get_planets_list(self):
        planet_df = pd.DataFrame(self.planets)
        planet_df['residents_count'] = planet_df.residents.apply(len)
        planet_df['films_count'] = planet_df.films.apply(len)
        planets_df = planet_df.filter(['name', 'rotation_period',
                                       'orbital_period', 'diameter',
                                       'climate', 'gravity',
                                       'terrain', 'surface_water',
                                       'population', 'residents_count',
                                       'films_count'], axis=1)
        return planets_df
        

if __name__ == '__main__':
    c = Planets()
    c.planets_df.to_csv('src/data/planets_data.csv', index=False)
    