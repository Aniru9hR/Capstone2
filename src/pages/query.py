import streamlit as st
import psycopg2
import pandas as pd

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


st.title(":orange[Query planet data!!]")
answer = st.text_input('Enter a planet name :(ex: Alderaan,Hoth,Dagobah,Bespin)', value = 'Tatooine')
sql = "SELECT name,rotation_period,orbital_period,diameter,climate,gravity,terrain,surface_water,population,residents_count,films_count from  planets  where name = "+"'"+answer+"'"+";"

rows = run_query(sql)
film_df = pd.DataFrame(rows, columns=['Name', 'Rotation period', 'Orbital period',
                               'Diameter', 'Climate',
                               'Gravity', 'Terrain',
                               'Surface water','Population',
                               'Residents count','Films count'])

st.table(film_df)