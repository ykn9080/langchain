import streamlit as st
import pandas as pd
import streamlit_pandas as sp

@st.cache_data()
def load_data(file):
    df=pd.read_csv(file)
    return df

file="data/titanic.csv"

df=load_data(file)
# st.write(df)
create_data={
    "Sex":"multiselect"
    
}

all_widgets=sp.create_widgets(df,create_data, ignore_columns=["PassengerId"])
res=sp.filter_df(df, all_widgets)
st.write(res)