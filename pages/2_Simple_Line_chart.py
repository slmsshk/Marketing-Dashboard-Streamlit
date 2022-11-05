import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

import UI

st.set_page_config(page_icon='icons\slc.png')
UI.add_bg_from_local('icons\slc_bg.jpg')
df=pd.read_json('pages\data.json')

col=[i for i in df.columns]
UI.write("Simple Line Chart",tag='h1',fontsize=50,padding='5px',bg='#b2beb5')

col1,col2=st.columns(2)

col1.write(col)

with col2:
    value=st.selectbox('Select Column for line chart',options=col)
st.write(np.log(df[value]))

fig,axes=plt.subplots()
axes.plot(df[value])
fig.suptitle('line Chart',color='blue')
st.pyplot(fig)

fig = px.line(df[value], title='Life expectancy in Canada')
st.plotly_chart(fig)
# st.line_chart()
# @st.cache
