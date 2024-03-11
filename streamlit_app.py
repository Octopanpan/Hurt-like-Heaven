import streamlit as st 
st.write("Hello")
st.write("je veux faire mon blog sur l'album viva la vida helllp ToT")
name=st.text_input("Your name")
st.write("Hello"+ name)
import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")
genre = st.radio(
  "what's your favorite music genre ?",
  [":rainbow(Pop)]", "***Rock***", "jazz :saxophone"],
  caption = ["Dance and have fun.", "look at that guitar rift !","Chill and relax."])
if genre == ':***Rock***':
  st.write('you selected Rock.')
else:
  st.write("you didn\'t select Rock.")
               


