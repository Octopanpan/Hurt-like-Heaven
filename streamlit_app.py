import streamlit as st 
st.write("Hello")
st.write("je veux faire mon blog sur l'album viva la vida helllp ToT")
name=st.text_input("Your name")
st.write("Hello"+ name)
input ="lapin"
list_possibilities=["rabbit, "rare", "rhyme", "rogue"]

import streamlit as st

genre = st.radio(
    "What's your favorite music genre",
    [":rainbow[Pop]", "***Rock***", "Jazz :saxophone:"],
    captions = ["Dancing and Singing.", "Look at that sick guitar riff!", "Chill and relax."])

if genre == ':rainbow[Pop]:':
    st.write('You selected Pop.')
else:
    st.write("You didn\'t select Pop.")
