import streamlit 

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range lEgg')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

import requests

streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What?', 'Kiwi')
streamlit.write('the user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pandas.json_normalize (fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized )
