import streamlit as st

st.title('Hello World')

st.header("This is Header")

st.subheader("This is Subheader")

st.text("This is a text")

st.markdown(""" # This is a h1 header
## This is h2 header
:moon:<br>
:fire:<br>
:sunglasses:<br>
**This is Bold**<br>
_This is italic_<br>
""", True)

st.latex(st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)
     '''))

st.write("Nitesh","Addagatla","Data Scientist")
st.write('# Nitesh')
st.write(sum)

d = {
    'name':'Nitesh',
    'job':'Data Scientist'
}

st.write(d)