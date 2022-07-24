# Importing Streamlit Library
import streamlit as st

# Page Icon and Name
st.set_page_config(page_title='Registration Form | BlueFireTechnologies',page_icon='logo.png')

# Company Banner
st.image('companyBanner.png')

# Page Ttile
st.title('Registration Form')


# Page Modification
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

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

# Gender, Date of Birth and Age
gen,dob,old = st.columns([1,2,1])
gender = gen.radio('Gender',['Male','Female'])
date_of_birth = dob.date_input('Birthday')
age = old.text_input("Age")

# Address
address = st.text_input("Address")
ci,pin,cou = st.columns(3)
city = ci.text_input('City')
pinCode = pin.text_input('Pin Code')
country = cou.text_input('Country')

# Experience
tit,yr,mn = st.columns([3,1,1])
title = tit.selectbox('Title',['Fresher','Experienced'])
year = yr.number_input('Year/s',step=1)
month = mn.number_input('Month/s',step=1)

# Photo and Resume
pho,res = st.columns(2)
photo = pho.file_uploader('Upload Your Photo')
resume = res.file_uploader('Upload Your Resume')

# T&C and Submit
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
tc,blank,sub = st.columns([3,1,1])
ter_cond = tc.checkbox('I Accept T&C')
submit = sub.button('Submit')

# Footer
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
st.markdown("") # Just for creating vacant space
bl1,foot,bl2 = st.columns(3)
footer = foot.write("Made with ❤️ by [Nitesh](https://www.linkedin.com/in/nitesh-addagatla)",)