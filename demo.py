import streamlit as st

st.title("Even or Odd")

a = st.text_input(label="Enter the term number")

if st.button("Submit"):
    num = int(a)
    if num%2==0:
        st.write("The given term",a,"is even")
    else:
        st.write("The given term",a,"is odd")