import streamlit 

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

import requests

streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What?', 'Kiwi')
streamlit.write('the user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pandas.json_normalize (fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized )


import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit');

select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST;
