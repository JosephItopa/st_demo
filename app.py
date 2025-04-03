# pip install streamlit
import streamlit as st
import pandas as pd
#------------------------------------
st.title("Our First App")
#------------------------------------
st.header("Our App Header")
st.subheader("Our App Subheader")

#streamlit run app.py
#-----------------------------------------------
st.write("Today, we are learning streamlit")

st.button("submit")

st.button("submit", type="primary")

st.button("hello", type="secondary")

st.button("submit", type="tertiary")
# ---------------------------------------
# st.checkbox("Male", value=True)
# -------------------------------------
df = st.checkbox("Male", value=True)
if df == True:
    st.write("I am a male")
else:
    st.write("I am a female")

st.radio("fruits", options=["Guava","Apple","Mango","Orange"])
# ------------------------------------
st.text_input("first name", max_chars=20, placeholder="enter your first name")

st.text_area("story time", placeholder="enter text here", height=150)
# -------------------------------------------
st.number_input("year", min_value=2000, max_value=2050, step=2, placeholder="increasing year")
# -----------------------------------------
# st.slider("age", min_value=1, max_value=50, step=5)

num = st.slider("age", min_value=1, max_value=50, step=5)

st.write("slider number:", num)
# ------------------------------
# st.file_uploader("upload a file", type=['csv', 'txt'])

data = st.file_uploader("upload a file", type=['csv', 'txt'])
if data:
    df = pd.read_csv(data)
    st.dataframe(df)