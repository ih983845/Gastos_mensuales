import streamlit as st
import pandas as pd

st.sidebar.title("Open the excel file")
uploaded_file = st.sidebar.file_uploader("Choose a file",type= 'xlsx' )

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.line_chart(data= df, x= "Fecha", y= "Amount")

    st.bar_chart(data= df, x= "Tipo", y= "Amount")

st.run()