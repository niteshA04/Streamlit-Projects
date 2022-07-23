import imp
import streamlit as st
import numpy as np
import pandas as pd
st.title('Data Integration')

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape(2,4)
d = {
    'Name':["Nitesh"],
    'City':["Mumbai"],
    'College':["VPPCOE"]
}

df = pd.read_csv('Salary_Data.csv')
print(df)

st.dataframe(a)
st.dataframe(n)
st.dataframe(nd)
st.dataframe(d)
st.dataframe(df)

# Second Method
st.table(df)
st.table(d)
st.table(nd)
st.table(n)
st.table(a)

# Third Method
st.json(d)

