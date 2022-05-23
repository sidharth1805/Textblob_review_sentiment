import streamlit as st
import pandas as pd
#from nltk.tokenize import sent_tokenize
#from nltk.tokenize import word_tokenize
import re
import string
#from textblob import TextBlob

#This is a py file

st.title("Data Visualzization App")
file_up=st.sidebar.file_uploader(label="Upload your CSV",type=['csv'])
st.text("##INPUT DATA")
global data
if file_up is not None:
    
    try:
        data = pd.read_csv(file_up)
    except Exception as e:
        print(e)
        data = pd.read_csv(file_up)
st.write(data)
        

