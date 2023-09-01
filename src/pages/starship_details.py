import streamlit as st
import psycopg2
import pandas as pd
from pathlib import Path
import os
import plotly.express as px

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


rows = run_query("SELECT name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,crew,passengers,cargo_capacity,consumables,hyperdrive_rating,pilots_count from starship;")
starships_df = pd.DataFrame(rows,columns=['Name', 'Model', 'Manufacturer',
                               'Cost in credits', 'Length',
                               'Max atmosphering speed', 'Crew',
                               'Passengers','Cargo capacity',
                               'Consumables','Hyperdrive rating',
                               'Pilots Count'])

st.title(':orange[StarWars starships!!]')

st.dataframe(starships_df)

st.header(':orange[Lets have some fun visualizing the data!!!]')

filepath = os.path.join(Path(__file__).parents[1], 'data/starships_data.csv')
df = pd.read_csv(filepath, low_memory=False)

vis_to_use = ['scatterplot', 'bar chart']
type_vis = st.selectbox('Select the type of Visualization you would like to see:', options=vis_to_use)

if type_vis == 'scatterplot':
    answer = st.selectbox('Select a Column to Visualize on the X-axis:', options=list(df.columns))
    answer2 = st.selectbox('Select a column to visualize on the Y-axis:', options = sorted(list(df.columns)))
    answer3 = st.selectbox('Select a column to visualize to color', options = sorted(list(df.columns)))
    if answer:
        try:
            st.plotly_chart(px.scatter(df, x=answer, y=answer2, color=answer3), use_container_width=True)
        except BaseException:
            print("Error visualizing this column for scatterplot")
elif type_vis == 'bar chart':
    answer = st.selectbox('Select a Column to Visualize on the X-axis:', options=sorted(list(df.columns)))
    answer2 = st.selectbox('Select a column to visualize on the Y-axis:', options = sorted(list(df.columns)))
    answer3 = st.selectbox('Select a column to visualize to color', options = sorted(list(df.columns)))
    if answer:
        try:
            st.bar_chart(df, x=answer, y=answer2, color=answer3, use_container_width=True)
        except BaseException:
            print("Error visualizing this column for bar chart")
