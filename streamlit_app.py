import streamlit
streamlit.title('I am healthy and wealthy. What a great feeling !!!. Kudos to Baru for providing me healthy food daily :)')
streamlit.header('🥗 🥣 Breakfast Menu')
streamlit.text('🐔 Dosa, Vada, Idly, Sambar')
streamlit.text('🍞 Poori, Sagu, Paneer Butter masala')
streamlit.text('🥑 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
