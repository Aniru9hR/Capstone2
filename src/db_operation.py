import pandas as pd 
import psycopg2
from pathlib import Path
import os
from sqlalchemy import create_engine


class PGSQL:
    conn = psycopg2.connect(
        dbname='plyquqmz',
        user='plyquqmz',
        password='0ddQrmMaG14JHE65LcNoCvCgfFFmZnMf',
        host='peanut.db.elephantsql.com'
    )

    cur = conn.cursor()

    def create_tables(self):
        """ create tables in the PostgreSQL database"""
        commands = (
            """ CREATE TABLE films (
                    film_id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    director VARCHAR(255) NOT NULL,
                    release_date DATE,
                    character_count INTEGER,
                    planets_count INTEGER,
                    starships_count INTEGER,
                    vehicles_count INTEGER,
                    species_count INTEGER
                    )
            """
            )
        try:

            tables = commands.split(';')
            # create table one by one
            print(commands)
            for table in tables:
                print(self.cur)
                self.cur.execute(table)
            # close communication with the PostgreSQL database server
            self.cur.close()
            # commit the changes
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def insert_data(self):
        # print(Path(__file__).parents[0])
        filepath_film = os.path.join(Path(__file__).parents[0],'data/films_data.csv')
        filepath_character = os.path.join(Path(__file__).parents[0],'data/character_data.csv')
        filepath_planets = os.path.join(Path(__file__).parents[0],'data/planets_data.csv')
        filepath_starships = os.path.join(Path(__file__).parents[0],'data/starships_data.csv')
        df = pd.read_csv(filepath_film, low_memory=False)
        df_character = pd.read_csv(filepath_character, low_memory=False)
        df_planets = pd.read_csv(filepath_planets, low_memory=False)
        df_starships = pd.read_csv(filepath_starships, low_memory=False)
        connection = "postgresql://plyquqmz:0ddQrmMaG14JHE65LcNoCvCgfFFmZnMf@peanut.db.elephantsql.com/plyquqmz"
        df.to_sql(con=connection, name='films', if_exists='replace')
        df_character.to_sql(con=connection, name='character', if_exists='replace')
        df_planets.to_sql(con=connection, name='planets', if_exists='replace')
        df_starships.to_sql(con=connection, name='starship', if_exists='replace')

        
if __name__ == '__main__':
    c = PGSQL()
    c.create_tables()
    c.insert_data()