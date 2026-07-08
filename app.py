import pandas as pd
import streamlit as st
st.title('BioPaper Mining Tool')
st.dataframe(pd.read_csv('outputs/extracted_abstracts.csv'))
