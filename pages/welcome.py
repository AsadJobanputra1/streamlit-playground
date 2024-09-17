import streamlit as st
from PIL import Image
import os

def show(navigate_to):
    # Apply custom CSS styles
    with open('styles/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Display the welcome image
    image_path = os.path.join('images', 'ai_robot.jpg')
    image = Image.open(image_path)
    st.image(image, caption='AI Robot at a Classic Typewriter', use_column_width=True)

    # Welcome message
    st.title("Welcome to the Writing Workshop!")
    st.write("""
    This application is a writing workshop with a set of writing agents that will write, review, and revise an article.
    """)

    # Begin button to navigate to the write article screen
    if st.button('Begin'):
        navigate_to('write_article')
