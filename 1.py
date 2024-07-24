import streamlit as st

st.set_page_config(page_icon="😎", page_title="portfolio")
st.title("Eswar Adesh Ch ",anchor=False)
st.subheader("Web Developer | Coder🧑‍💻 | Badminton Player🏸")
with st.container(border=2):
    st.info("i am so and so....")
    
    
    
col1, col2, col3 =st.columns(3)

with col1:
    with st.expander(label="know me more", expanded=False):
        st.info("i am so and so....")
        st.image("hinata.jpg",width=200)
with col2:
    with st.expander(label="know me more", expanded=False):
        st.warning("Never ever play with my Emotions")
with col3:
    with st.expander(label="know me more", expanded=False):
        st.error("Bakaaaaaa...")