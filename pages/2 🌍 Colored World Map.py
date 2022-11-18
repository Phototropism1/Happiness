import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Colored World Map 🌍",
    page_icon="🌍"
)

st.markdown("## Colored World Map")
st.markdown("")

st.write("""
#### Key Findings
##### There is a correlation between Global distribution of Happiness Score and Log GDP per capita !
##### This distribution correlation can give us a hint regards the connection between Happiness and Money.""")

with st.expander("Model Benefits"):
    st.write("""
        * ##### Identify Geographical distribution in a glance
        * ##### Key country info available with hovering
        """)
with st.expander("Model Features"):
    st.write(""" 
    * ##### Color scale: Green = High Score, Red = Low Score
    * ##### Key country info: Hover on country 
    * ##### Zoom: Scroll mouse
    * ##### Pan: Left click and drag
""")

with st.expander("Global Happiness Score distribution"):
    st.write("""
        * ##### Highest Score: West Europe, North America, Australia
        * ##### Medium Score: Mid / South America, Mid / North Asia, East Europe
        * ##### Lowest Score: Africa, South Asia
        """)
h = open("figs/Map_Happiness Score.html")
components.html(h.read(),height=400,width=800)

with st.expander("Global Log GDP per Capita distribution"):
    st.write("""
        * ##### Correlated global distribution when comparing to Happiness Score
        * ##### Highest Score: West Europe, North America, Australia
        * ##### Medium Score: Mid / South America, Mid / North Asia, East Europe
        * ##### Lowest Score: Africa, South Asia
""")

g = open("figs/Map_Log GDP per capita.html")
components.html(g.read(),height=400,width=800)

with st.expander("Code Example"):
    code = '''# In[]:

### World map 1 - Country by Happiness Score

v1='Happiness Score'
h1='Regional indicator'
h2='Log GDP per capita'

np.random.seed(12)
gapminder = country
gapminder['country names'] = np.random.uniform(low=100000, high=200000, size=len(gapminder)).tolist()
fig = px.choropleth(gapminder, locations="Country name",
                    locationmode='country names',
                    color=v1, 
                    hover_name="Country name",title="World map - Country by " + v1,
                    hover_data=[h1,h2],
                    range_color=[20,80],  
                    color_continuous_scale='RdYlGn_r')

figure(figsize=(10, 16), dpi=80)
fig.write_html("C:/DS/Python/Projects/Happiness/figs/Map_"+v1+".html")
fig.show()
       '''
    st.code(code, language='python')
