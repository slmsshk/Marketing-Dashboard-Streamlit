import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import UI 

# import json
# import requests
st.set_page_config(page_title="Dashboard", page_icon="📈")
UI.add_bg_from_local('pages\Background Image.png')

# Title
UI.write(tag='h1',value="Marketing Dashboard",color='white',fontsize=35)

# Subtitle
UI.write(value='This dashboard will help you get more information about the Marketing datasets and their output',tag='h2',textalign='left',fontsize=25,color='#ff033e')
# ==================================================================

# Loading Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_json('pages\data.json')

col1,col2=st.columns(2)

with col1:
    first_rows=col1.number_input(' ',step=1)
    col1.markdown(f"""<p style='color:white;text-align:'center';'>Enter Preview num</'p'>""",unsafe_allow_html=True)
    col1.write(df.head(first_rows))

with col2:
    last_rows=col2.number_input(' ',step=1,key=2)
    col2.markdown(f"""<p style='color:white;text-align:'center';'>Enter Preview num</'p'>""",unsafe_allow_html=True)
    col2.write(df.tail(last_rows))

# ===================================================================


# #Separating orderbook and trade columns
# df=pd.read_json('pages\data.json')
# st.write(df.head())

# cols=df.columns
# UI.markdown(cols)
# l0 = df.columns
# l1 = []
# l2 = []

# # i=0
# # for i,x in enumerate (l0) :
# #     if 'orderbook' in x :
# #         l1.append(x)
# #     elif 'trade' in x:
# #         l2.append(x)
# #     i += 1

# # df1 = pd.DataFrame(l1)
# # df2 = pd.DataFrame(l2) 

# # # Functions for each of the pages
# # #All types of charts

# # #Adding dataframe in a button to show

# # st.sidebar.title("Selecting Visual Charts")
# # st.sidebar.markdown("Selecting the Charts accordingly.")

# # st.sidebar.markdown("<h3 style='text-align: left; color: Black; font-size:15px; '>Show Analysis Status</h1>", unsafe_allow_html=True)
# # Dataset = st.sidebar.checkbox("Show Status", False, key = 1)


# # if Dataset:     
# #     st.write(df)

# # #data = pd.read_json(r"D:\Excelr DataScience\Deployment\Marketing Dashboard\data.json")
# # chart_visual = st.sidebar.selectbox('Select Visual Charts', ('Select Option','Pie Chart', 'Line Chart', 'Bar Chart'))
    
# # def interactive_plot1(l0):
# #     st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Line Chart</h2>", unsafe_allow_html=True)
# #     col1, col2 = st.columns(2)
# #     x_axis_val = col1.selectbox('', options=df1)
# #     y_axis_val = col2.selectbox('', options=df2)
    
# #     plot = px.line(df, x=x_axis_val, y=y_axis_val)
# #     st.plotly_chart(plot)
    
# # def interactive_plot2(l0):
# #     st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Bar Chart</h2>", unsafe_allow_html=True)
# #     col1, col2 = st.columns(2)
    
# #     x_axis_val = col1.selectbox('Select the X-axis', options=df1)
# #     y_axis_val = col2.selectbox('Select the Y-axis', options=df2)

# #     plot = px.bar(df, x=x_axis_val, y=y_axis_val)
# #     st.plotly_chart(plot)
    
# # def interactive_plot3(l0):
# #     st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Pie Chart</h2>", unsafe_allow_html=True)
# #     col1, col2 = st.columns(2)
    
# #     x = col1.selectbox('Select the X-axis', options=df1)
# #     y = col2.selectbox('Select the Y-axis', options=df2)

# #     plot = px.pie(df, x, y)
# #     st.plotly_chart(plot)
    
# # #Sidebar navigation
# # #st.sidebar.title('Navigation')
# # #option=st.sidebar.radio('Select what you want to display:',['Line Chart','Bar Chart','Area Chart','Scatter Chart'])

# # # Navigation options
# # if chart_visual == 'Line Chart':
# #   interactive_plot1(df)
# # elif chart_visual == 'Bar Chart':
# #   interactive_plot2(df)
# # elif chart_visual == 'Pie Chart':
# #   interactive_plot3(df)


