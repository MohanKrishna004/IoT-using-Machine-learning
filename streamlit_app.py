import streamlit as st
import pandas as pd

st.title('Smart Home:)')

st.info('App for anamoly detection')

with st.expander('Data'):
  st.write('RAW DATA')
  df = pd.read_csv("/kaggle/input/bot-iot-4ads/UNSW_2018_IoT_Botnet_Full5pc_4.csv", 
                 low_memory=False)
  df

