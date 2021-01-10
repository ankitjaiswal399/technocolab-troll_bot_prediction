# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 10:31:37 2021

@author: 10THHPi3
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd

def main():
    
    html_temp = """
        
    <div class = "main">
       <h1> Bot tweet prediction</h1>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    tweet = st.text_area("Enter the tweet")
    
    bot_html = """
        <h2 style = "color: red"> Bot </h2>
    """
    
    troll_html = """
        <h2 style = "color: red"> Troll </h2>   
    """
    
    if st.button("Predict"):
        
        st.markdown(bot_html, unsafe_allow_html=True)
        st.markdown(troll_html, unsafe_allow_html=True)
        
if __name__ == "__main__":
    main()