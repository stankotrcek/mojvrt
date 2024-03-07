import streamlit as st
import duckdb 
import pandas as pd


st.write("test")

con = duckdb.connection('data/portfelj.ddb')

df = con.sql("SELECT * FROM price;")

st.write(df)

con.close()