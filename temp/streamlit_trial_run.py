import streamlit as st

st.title("My First App")
number = st.slider("Pick a number", 0, 100, 50)   # returns an int
st.write(f"The square is {number ** 2}")

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(number, 3), columns=["a", "b", "c"])
st.line_chart(df)

st.slider("Min", 0, 100, 25)        # int
st.selectbox("City", ["NY", "SF"])  # selected string
st.multiselect("Tags", ["a", "b"])  # list
st.text_input("Name")               # string
st.number_input("Age", 0, 120)      # int
st.checkbox("Show all")             # bool
st.button("Predict")                # bool (True only on the click-rerun)
st.file_uploader("CSV", type="csv") # uploaded file or None
st.radio("Choice", ["Yes", "No"])   # string