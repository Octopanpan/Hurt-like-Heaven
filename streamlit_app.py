import streamlit as st 
st.write("Hello")
st.write("je veux faire mon blog sur l'album viva la vida helllp ToT")
name=st.text_input("Your name")
st.write("Hello"+ name)
import streamlit as st

genre = st.radio(
    "What's your favorite music genre",
    [":rainbow[Pop]", "***Rock***", "Jazz :saxophone:"],
    captions = ["Dancing and Singing.", "Look at that sick guitar riff!", "Chill and relax."])

if genre == ':Jazz :saxophone:':
    st.write('You selected Jazz.')
else:
    st.write("You didn\'t select Jazz.")
