import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRQ2cabWZZfzicRWSCzVA6rZKOWdNfqpy5kqxrLn6V4VThfaA0bIqd4k_PZv3z5CJPpb18PFhyv8-Ee/pub?output=csv')
st.dataframe(voc)
l=voc.shape[0]
i=hp.random.choice(range(l)) 
word_fr= voc['Definiton'].values[i] 
word_chi= voc['Hanzi'].values[i] 
st.write(word_frt+" "+ word_chi)
