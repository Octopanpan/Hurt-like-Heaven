import streamlit as st
import pandas as pd
voc=pd.read_cvs('https://docs.google.com/spreadsheets/d/e/2PACX-1vRQ2cabWZZfzicRWSCzVA6rZKOWdNfqpy5kqxrLn6V4VThfaA0bIqd4k_PZv3z5CJPpb18PFhyv8-Ee/pubhtml')
st.dataframe(voc)
              
    
