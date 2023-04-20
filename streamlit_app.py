import streamlit
streamlit.title('I am healthy and wealthy. What a great feeling !!!. Kudos to Baru for providing me healthy food daily :)')
streamlit.header('🥗 🥣 Breakfast Menu')
streamlit.text('🐔 Dosa, Vada, Idly, Sambar')
streamlit.text('🍞 Poori, Sagu, Paneer Butter masala')
streamlit.text('🥑 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
import requests
import snowflake.connector
from urllib.error import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#Create repeatable code block (function)
def get_fruityvice_data(this_fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized
    
streamlit.header('FruityVice Fruit Advice !')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get the information")
  else:
      back_from_function=get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("Hello your fruit load list:")
streamlit.dataframe(my_data_row)

#Allow end user to add fruit to list
add_my_fruit = streamlit.text_input('What fruit would you like to add','Kiwi')
streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')");
