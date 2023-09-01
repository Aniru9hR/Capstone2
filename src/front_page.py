import streamlit as st
import os
from pathlib import Path
from PIL import Image

st.title("Welcome to  StarWars ")
st.header(':orange[MAY THE FORCE BE WITH YOU]')

filepath = os.path.join(Path(__file__).parents[0], 'st_img.png')
image = Image.open(filepath)
st.image(image)