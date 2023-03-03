import spacy
import streamlit as st
from annotated_text import annotated_text
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu



#
# def print_hi(name):
#     print(f'Hi, {name}')
#
# def foo(x):
#     print(x)


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")



# side bar menu
with st.sidebar:
#     selected = option_menu(
#         menu_title="Main Menu",
#         options=["home", "Projects", "Work Experience", "Contact"])

# if selected == "home":
    st.title(f'Hi, I am Hesham, Welcome :wave:')

