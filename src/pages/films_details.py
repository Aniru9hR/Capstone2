import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px
from pathlib import Path
import os
from PIL import Image

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])


conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


# def add_logo(logo_path, width, height):
#     """Read and return a resized logo"""
#     logo = Image.open(logo_path)
#     modified_logo = logo.resize((width, height))
#     return modified_logo


# logo_filepath = os.path.join(Path(__file__).parents[1], 'logo.jpg')

# my_logo = add_logo(logo_path=logo_filepath, width=400, height=200)
# st.image(my_logo)


st.title(":orange[StarWars movies!!]")
rows = run_query("SELECT title, director, release_date, character_count, planets_count, starships_count,vehicles_count,species_count from films;")
film_df = pd.DataFrame(rows, columns=['Title', 'Director', 'Release date',
                               'Character count', 'Planets count',
                               'Starships count', 'Vehicles count',
                               'Species count'])
# st.dataframe(film_df)
st.dataframe(film_df.style.highlight_max(subset =['Character count','Planets count','Starships count','Vehicles count','Species count'],color = 'orange', axis = 0))


st.header(':orange[Lets have some fun visualizing the data!!!]')
# Establish a filepath to the films_data.csv file
filepath = os.path.join(Path(__file__).parents[1], 'data/films_data.csv')
df = pd.read_csv(filepath, low_memory=False)

answer2 = st.selectbox('Select a column to visualize on the Y-axis:', options= sorted(list(df.columns)))
if answer2:
    try:
        st.bar_chart(df, x='title', y=answer2, use_container_width=True)
    except BaseException:
        print("Error visualizing this column for bar chart")