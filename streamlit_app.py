import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRQ2cabWZZfzicRWSCzVA6rZKOWdNfqpy5kqxrLn6V4VThfaA0bIqd4k_PZv3z5CJPpb18PFhyv8-Ee/pub?output=csv')
st.dataframe(voc)
