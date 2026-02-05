import streamlit as st
st.title('my first web app')
name=st.text_input("enter your name")
age=st.number_input("enter your age",min_value=21, max_value=35)
if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old!")
