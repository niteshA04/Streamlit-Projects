import streamlit as st

st.set_page_config(page_title='Registration Form')
st.title('Registration Form')

# Page Modification
# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden; }
#         footer {visibility: hidden;}
#         </style>
#         """
# st.markdown(hide_menu_style, unsafe_allow_html=True)

# First name and Last name
first,last = st.columns(2)
first_name = first.text_input("First Name")
last_name = last.text_input("Last Name")

# Email amd Phone Number
email,phone = st.columns([2,1])
email_id = email.text_input("Email Id")
phone_number = phone.text_input("Phone Number")

# College Name
st.text_input('College Name')

# College ID, Department and Division
clg,dep,div = st.columns(3)
clg_id = clg.text_input('College ID')
department = dep.text_input('Stream')
division = div.text_input('Division')

# Gender
gen,dob,old = st.columns([1,2,1])
gender = gen.radio('Gender',['Male','Female'])
date_of_birth = dob.date_input('Birthday')
age = old.text_input("Age")

# T&C and Submit
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
tc,blank,sub = st.columns([3,1,1])
ter_cond = tc.checkbox('I Accept T&C')
submit = sub.button('Submit')