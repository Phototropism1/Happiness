# WebApp-Happiness content
import streamlit as st


st.set_page_config(
    page_title="Intro",
    page_icon="🌻"
)
st.markdown("# Intro 🌻")
st.write("""

##### Why did I chose "World Happiness 2021 Index" as my first analysis topic:
* ##### It is an important topic !
* ##### The analysis outcome has a potential to be insightful
* ##### It has interest for the general public
* ##### It is pretty easy to analyze, 8 variables (columns) for 149 countries (rows)

### Data visualization models that were used:
* ##### World Map with color gradient: Visualize score rank for each country
* ##### Principle Component Analysis (PCA): Evaluate the variability between the variables
* ##### Scatter Plot: Evaluate linearity and distribution of Happiness Score Vs each of the other variables
* ##### Heat Map: Visualize clusters and distribution for all data points

##### Hope you will enjoy my analysis...
""" )