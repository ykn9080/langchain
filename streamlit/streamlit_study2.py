import streamlit as st
import pandas as pd

def clean_text(text):
    return text.replace("`", "").replace("'", "").replace("-\n", "").replace("\n\n", "&&***&&").replace("\n", " ").replace("&&***&&", "\n\n").replace("  ", " ").strip()



st.title("💬 Lesson 2: Intro to layout and images")

st.sidebar.image(
    "images/logo.png", width=50)

st.sidebar.header("💬 Options")
text = st.sidebar.text_area("Paste your API key here", height=5)

button1 = st.sidebar.button("Clean text")
if button1:
    bef, aft = st.columns(2)
    befexpander = bef.expander("Before Expander")
    with befexpander:
        befexpander.header("before")
        befexpander.write(text)

    aft.header("after")
    clean = clean_text(text)
    aft.write(clean)

file=st.file_uploader("Upload a file",type=['csv','txt','json','xlsx'])
if file is not None:
    ext= file.name.split('.')[-1]
    switch(ext,
           "csv",
           st.write(pd.read_csv(file)),
           "txt",
           st.write(file.read()),
           "json",
           st.write(pd.read_json(file)),
           "xlsx",
           st.write(pd.read_excel(file))
    st.write(file)
    st.write(file.read())