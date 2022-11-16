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
##### There is a correlation between Global distribution of Happiness and Log GDP per capita ranks !
##### This distribution correlation can give us a hint regards the connection between Happiness and Money.""")

with st.expander("Model Benefits"):
    st.write("""
        * ##### Identify Geographical distribution in a glance
        * ##### Key country info available with hovering
        """)
with st.expander("Model Features"):
    st.write(""" 
    * ##### Color scale: Green = High rank, Red = Low rank
    * ##### Key country info: Hover on country 
    * ##### Zoom: Scroll mouse
    * ##### Pan: Left click and drag
""")

with st.expander("Global Happiness Rank distribution"):
    st.write("""
        * ##### Highest rank: West Europe, North America, Australia
        * ##### Medium rank: Mid / South America, Mid / North Asia, East Europe
        * ##### Lowest rank: Africa, South Asia
        """)
h = open("C:/DS/Python/Projects/Happiness/figs/Map_Happiness rank.html")
components.html(h.read(),height=400,width=800)

with st.expander("Global Log GDP per Capita distribution"):
    st.write("""
        * ##### Correlated global distribution when comparing to Happiness Rank
        * ##### Highest rank: West Europe, North America, Australia
        * ##### Medium rank: Mid / South America, Mid / North Asia, East Europe
        * ##### Lowest rank: Africa, South Asia
""")

g = open("C:/DS/Python/Projects/Happiness/figs/Map_Log GDP per capita rank.html")
components.html(g.read(),height=400,width=800)

with st.expander("Code Example"):
    code = '''# In[]:

### World map 1 - Country by Happiness rank

v1='Happiness rank'
h1='Regional indicator'
h2='Log GDP per capita rank'

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
