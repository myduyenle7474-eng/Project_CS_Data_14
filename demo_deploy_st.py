import streamlit as st
import pandas as pd

st.title('Deploy Streamlit App', text_alignment = 'center')
df = pd.DataFrame([{'Ten': 'Duyen', 'Tuoi': 20, 'Nghe': 'SCM'}])
st.dataframe(df)
if st.button('Balloons'):
    st.balloons