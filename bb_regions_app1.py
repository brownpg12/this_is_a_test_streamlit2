import streamlit as st
import pandas as pd
import numpy as np
import datetime

@st.cache_data
def load_data():
    infile='broadband_itv_regions_summary_pb_020323.csv'
    df=pd.read_csv(infile)
    df.reset_index(inplace=True)
    for col in ['percent_of_premises_unable_to_receive_10Mbit/s','percent_premises_below_the_USO','percent_unconnected','Percent_lt10Mbit/s']:
        df[col]=df[col].str.replace(r'%', '').astype(float)
        
    return df


st.set_page_config(page_title='This is a test, this is a test', layout="wide")

df=load_data()

col1,col2= st.columns(2)
with col1:
    st.title('Broadband in regions: test  :tv:')
with col2:
    st.image('https://www.publicdomainpictures.net/pictures/370000/velka/television-15980966413Ie.jpg',width=200)


tab_coverage,tab_unconnected,tab_connections_lt10mbits = st.tabs(['Coverage','Unconnected','Connections <10Mbits'])

with tab_coverage:
    col1a, col2a = st.columns(2)
    with col1a:
        st.bar_chart(df,x='region',y='Number_premises_unable_to_receive_10Mbit/s')
    with col2a:
        st.bar_chart(df,x='region',y='percent_of_premises_unable_to_receive_10Mbit/s')

with tab_unconnected:
    col1b, col2b = st.columns(2)
    with col1b:
        st.bar_chart(df,x='region',y='Unconnected_Premises')
    with col2b:
        st.bar_chart(df,x='region',y='percent_unconnected')

with tab_connections_lt10mbits:
    col1c, col2c = st.columns(2)
    with col1c:
        st.bar_chart(df,x='region',y='Connections_lt10Mbit/s')
    with col2c:
        st.bar_chart(df,x='region',y='Percent_lt10Mbit/s')
                                                                  
