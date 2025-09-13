import streamlit as st
st.title("CAMPUSX is best chanall")
col1, col2 = st.columns(2)
with col1:
    st.write("Hello world!")
with col2:
    st.write("Hello world!")
st.header("offered course")
st.subheader("Data science")
st.subheader("Data analysis")
st.subheader("Machine Learning")
st.subheader("Data analysis engineering master ")
st.sidebar.title("Data analysis engineering")
st.sidebar.markdown("""
 -name
 -age
 -email
    """)