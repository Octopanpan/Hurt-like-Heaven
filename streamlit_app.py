import streamlit as st 
st.write("Hello")
st.write("je veux faire mon blog sur l'album viva la vida helllp ToT")
name=st.text_input("Your name")
st.write("Hello"+ name)
genre=st.radio("what's your favorite music genre ?",
               [":rainbow(Pop)]", "***Rock***", "jazz :saxophone"],
               caption = ["Dance and have fun.", "look at that guitar rift !","Chill and relax."])
if genre == ':***Rock***':
  st.write('you selected Rock.')
else:
  st.write("you didn\'t select Rock.")
               


