import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Sidebar and Navbar")

plt.style.use("ggplot")

data = {
    'num':[x for x in range(1,11)],
    'square':[x**2 for x in range(1,11)],
    'twice':[x*2 for x in range(1,11)],
    'thrice':[x*3 for x in range(1,11)]
}
df = pd.DataFrame(data=data)

rad = st.sidebar.radio("Navigation",['Single Select','Multi Select'])

if rad == 'Single Select':
    st.write("Single Select")
    col = st.sidebar.selectbox("Select a Column",df.columns)
    plt.plot(df['num'],df[col])
    st.pyplot()

if rad == 'Multi Select':
    st.write("Multi Select")
    col = st.sidebar.multiselect("Multiselect Column",df.columns)
    plt.plot(df['num'],df[col])
    st.pyplot()

st.title("Progress Bar")
prog = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    prog.progress(i+1)

st.balloons()