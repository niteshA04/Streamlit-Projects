import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.title("Displaying Plots and Media")
data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

st.dataframe(data)

# Charts
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

#Plots
plt.scatter(data['a'],data['b'])
plt.title("SCATTER")
st.pyplot()

chart = alt.Chart(data).mark_circle().encode(
    x = 'a',
    y = 'b',
    tooltip=['a','b']
)
st.altair_chart(chart, use_container_width=True)

# Flowchart
st.graphviz_chart("""
digraph{
    watch -> like
    like -> share
    share -> subscribe
    subscribe -> watch
}
""")

# Map
city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})
st.map(city)

# Media
st.image('gh.jpg')#can also adjust height and width

st.audio('crazyFrog.mp3')

st.video('video (12).mp4')
st.video('https://www.youtube.com/watch?v=D7eFpRf4tac')