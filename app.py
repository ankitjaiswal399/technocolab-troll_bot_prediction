# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 10:31:37 2021

@author: 10THHPi3
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))

def predict_genre(no_follow, author_verified, author_comment_karma,author_link_karma, over_18, is_submitter):
    input = pd.DataFrame(np.array([[no_follow, author_verified, author_comment_karma,author_link_karma, over_18,is_submitter]]).astype(np.float64))
    prediction = model.predict(input)

    return prediction
    

def main():
    
    page_bg_img = ''' 
    <style> body{ 
                background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366"); 
                background-size: cover; 
             }
     </style> 
    ''' 
    html_temp = """
        
    <div class = "main">
       <h1 style="color: white;"> Troll-Bot prediction</h1>
    </div>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown(html_temp, unsafe_allow_html=True)
    
    no_follow = st.text_input("Enter the number of followers", "Write 1 for True and 0 for False")
    author_verified = st.text_input("Is author verified? ", "Write 1 for True and 0 for False")
    author_comment_karma = st.text_input("Enter author_comment_karma", "Looking for a Number")
    author_link_karma = st.text_input("Enter author_link_karma", "Looking for a Number")
    over_18 = st.text_input("Is author over 18?", "Write 1 for True and 0 for False")
    is_submitter = st.text_input("Enter is_submitter", "Write 1 for True and 0 for False")
    
    bot_html = """
        <h2 style = "color: red"> Bot </h2>
    """
    
    troll_html = """
        <h2 style = "color: red"> Troll </h2>   
    """
    
    if st.button("Predict"):
        
        output = predict_genre(no_follow, author_verified, author_comment_karma,author_link_karma, over_18, is_submitter)
        
        print(output)
        if output == 0.0:
            st.markdown(bot_html, unsafe_allow_html=True)
        elif output == 1.0:
            st.markdown( troll_html, unsafe_allow_html=True)
        
if __name__ == "__main__":
    main()
