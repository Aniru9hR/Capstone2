import requests
import pandas as pd


class Starship:

    def __init__(self):
        self.api_url = 'https://swapi.dev/api/starships/'
        self.get_data()

    
    def get_data(self):
        starship_list = []
        while True:
            response = requests.get(self.api_url)
            print(response)
            if response:
                self.starship = response.json().get("results")
                df = self.get_starship_list()
                if response.json().get('next') is None:
                    break
                self.api_url = response.json().get('next')
                starship_list.append(df)
        self.starships_df = pd.concat(starship_list)
        self.starships_df = self.starships_df.fillna('NA')
        return self.starships_df

    def get_starship_list(self):
        starship_df = pd.DataFrame(self.starship)
        starship_df['films_count'] = starship_df.films.apply(len)
        starship_df['pilots_count'] = starship_df.pilots.apply(len)
        starships_df = starship_df.filter(['name', 'model',
                                         'manufacturer', 'cost_in_credits',
                                          'length', 'max_atmosphering_speed',
                                          'crew', 'passengers',
                                          'cargo_capacity', 'consumables',
                                          'hyperdrive_rating', 'starship_class'
                                          'films_count', 'pilots_count'], axis=1)
        return starships_df
        

if __name__ == '__main__':
    c = Starship()
    c.starships_df.to_csv('src/data/starships_data.csv', index=False)
    