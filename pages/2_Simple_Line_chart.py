import streamlit as st
import pandas as pd

st.set_page_config(page_icon='icons\slc.png')

cols=pd.read_json('pages\data.json').columns

for i in cols:
    print(i,type(i))