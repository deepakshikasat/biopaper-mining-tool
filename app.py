import pandas as pd
import streamlit as st

st.title("BioPaper Mining Tool")
st.caption("PubMed DILI abstracts with lightweight rule-based structured extraction.")
df = pd.read_csv("outputs/extracted_abstracts.csv")
keyword = st.selectbox("Mechanism keyword", ["all"] + sorted(df.mechanism_keyword.unique()))
if keyword != "all":
    df = df[df.mechanism_keyword == keyword]
st.dataframe(df)
