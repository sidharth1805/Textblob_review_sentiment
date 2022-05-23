import streamlit as st
import pandas as pd
#from nltk.tokenize import sent_tokenize
#from nltk.tokenize import word_tokenize
import re
import string
#from textblob import TextBlob

#This is a py file

st.title("Data Visualzization App")
st.set_options('depreciation.showfileUploaderEncoding',False)
file_up=st.sidebar.file_uploader(label="Upload your CSV",type=['csv'])

global data
if file_up is not None:
    print("Uploaded")

    try:
        data = pd.read_csv(file_up)
    except Exception as e:
        print(e)
        data = pd.read_csv(file_up)
st.write(data)
        
""" 
data = pd.read_csv('../input/chrome-reviews/chrome_reviews.csv')
data= data.drop(['User Name'],axis=1)
data= data.drop(['Developer Reply'],axis=1)
data= data.drop(['Version'],axis=1)
data= data.drop(['Review URL'],axis=1)
data= data.drop(['Review Date'],axis=1)
data= data.drop(['App ID'],axis=1)
data = data[data.Star != 5]
data = data[data.Star != 4]
data = data[data.Star != 3]
senti_list = []
for i in data["Text"]:
    score = TextBlob(i).sentiment[0]
    if (score > 0):
        senti_list.append('Positive')
    elif (score < 0):
        senti_list.append('Negative')
    else:
        senti_list.append('Neutral') 
data["sentiment"]=senti_list
data = data[data.sentiment == 'Positive']

st.write("Hello")
"""
