import json
# Kaggle api is installed on the project
import os

import matplotlib

import numpy as np
import pandas as pd
import plotly.express as px
import requests
import seaborn as sns
import streamlit as st
from PIL import Image



def main():
    hide_menu = """
    <style>
    #MainMenu {
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }
    </style>
    """

    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://www.springboard.com/blog/wp-content/uploads/2019/01/blog-ai-general1.png")
        }
       .sidebar .sidebar-content {
            background: url("https://appen.com/wp-content/uploads/2018/09/machine-learning-wiki.jpg")
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    def sub_text(text):
        """

        :param text: text
        """
        html_temp = f"""
        <p style = "color:#1F4E79; text_align:justify;"> {text} </p>
        </div>
        """

        st.markdown(html_temp, unsafe_allow_html=True)  # st.markdown(page_bg_img, unsafe_allow_html=True)


    st.markdown(hide_menu, unsafe_allow_html=True)


if __name__ == "__main__":
    main()