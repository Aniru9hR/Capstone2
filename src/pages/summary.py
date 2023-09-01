import streamlit as st

st.title("Star Wars App")


st.markdown('Star Wars is an American epic space opera franchise created by George Lucas and has quickly become a worldwide pop culture phenomenon.'
' The data for the Star Wars app has been scraped from the Star Wars API and the application uses postgres sql for data storage . This app provides information about all the Star Wars films, characters,planets and starships over the years .'
' The Star Wars app has seperate pages for Star Wars films, characters,planets and starships and also allows a user to visualize various attributes for each of the above pages')

st.header('Here are the different pages of my application:')

st.subheader('Characters details')
st.markdown(' Displays the character from the database and allows a user to select the type of attribute and visualization')

st.subheader('Films details')
st.markdown(' Displays the film from the database and allows a user to select the type of attribute and visualization')

st.subheader('Planet details')
st.markdown(' Displays the planet from the database and allows a user to select the type of attribute and visualization')

st.subheader('Starship details')
st.markdown(' Displays the starship from the database and allows a user to select the type of attribute and visualization')

st.subheader("Query Planets")
st.markdown('''Query: Allows a user to enter a planet name and return information about it from 
        our database''')


st.subheader('Character Attributes')
st.text('List of attributes')
st.text('''
name  : The name of this person
height : The height of the person in centimeters
mass :  The mass of the person in kilograms
gender : The gender of this person. Either "Male", "Female" or "unknown", "n/a" if the person does not have a gender
hair color : The hair color of this person. Will be "unknown" if not known or "n/a" if the person does not have hair
skin color : The skin color of this person
homeworld :a planet that this person was born on or inhabits
films : films that this person has been in
starships : starships that this person has piloted
''') 

st.subheader('Films Attributes')
st.text('List of attributes')
st.text('''
title  : The title of this film
director : The name of the director of this film
release date :  The ISO 8601 date format of film release at original creator country
''')   

st.subheader('Planet Attributes')
st.text('List of attributes')
st.text('''
name  : The name of this planet
rotation period : The number of standard hours it takes for this planet to complete a single rotation on its axis
orbital period :  The number of standard days it takes for this planet to complete a single orbit of its local star
diameter : The diameter of this planet in kilometers
climate : The climate of this planet. Comma separated if diverse
gravity : A number denoting the gravity of this planet, where "1" is normal or 1 standard G. "2" is twice or 2 standard Gs. "0.5" is half or 0.5 standard Gs
terrain : The terrain of this planet. Comma separated if diverse
surface water : The percentage of the planet surface that is naturally occurring water or bodies of water
population : The average population of sentient beings inhabiting this planet                  
''') 

st.subheader('Starship Attributes')
st.text('List of attributes')
st.text('''
name  :  The name of this starship
model  : The model or official name of this starship
manufacturer :  The manufacturer of this starship. Comma separated if more than one
cost in credits : The cost of this starship new, in galactic credits  
length : The length of this starship in meters        
max atmosphering speed : The maximum speed of this starship in the atmosphere. "N/A" if this starship is incapable of atmospheric flight
crew : The number of personnel needed to run or pilot this starship
passengers : The number of non-essential people this starship can transport
cargo capacity : The maximum number of kilograms that this starship can transport
consumables : The maximum length of time that this starship can provide consumables for its entire crew without having to resupply
hyperdrive rating : The class of this starships hyperdrive       
''') 
