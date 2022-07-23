import streamlit as st

st.title("Widgets")

# Button
st.button("Subacribe")
# Button Functionality
# It returns True value if pressed
if st.button("Like"):
    st.write("Thankyou")

# Text Input
st.text_input("Write ")
# Text Input Functionality
name = st.text_input("Name")
st.write("Hello, Welcome",name)

# Text Area
address = st.text_area("Enter your address")
st.write(address)

# Date Input
st.date_input("Enter Date")

# Time Input
st.time_input("Enter tine")

# Checkbox
st.checkbox("You are Human") #value=True to keep the check default

if st.checkbox("You accept T&C"):
    st.write("Thank You")

# Radio Button
st.radio("Select a Colour",['r','g','b']) # index= to set default value

# Selectbox
st.selectbox("Select a Colour",['r','g','b'])

# can also save the options in a variable

o1 = st.radio("Colour",['A','B','C'])

o2 = st.selectbox('Colour',['A','B','C'])

st.write("Selected is: ",o1,o2)

# Select Multiple Options
st.multiselect("Colours",['r','g','b','y','w'])

# Slider
st.slider("Age",min_value=18, max_value=90) # Can also change step size using step=

# Number Input
st.number_input("Marks (CGPA)")

# Input Files Upload
st.file_uploader("Upload a file")
img = st.file_uploader("Upload a Image")
st.image(img)