# library import
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# page config
st.set_page_config(
    page_title="Heat Map 🗺️",
    page_icon="🗺️"
)


image = Image.open('figs/Yakov Agam.jpg')

st.image(image, caption='Artist - Yakov Agam,  Window Masterpiece', width=400)

# mardown

st.markdown("## Heat Map")
st.markdown("")
st.markdown("### Methodology")
st.write("""
##### Although Heat Map is one of the most intensive data infographics model it is one of the most informative
##### Heat Map contains all the variables for all the samples, while the color gradient emphasize the value
##### In this case I chose the Heat Map to be ordered by the Happiness Rank as it provide our reference variable
""")
with st.expander("Model Features"):
    st.write("""
    * ##### X = Rank
    * ##### Y = Variable, ordered by Happiness rank
    * ##### Color scale: Blue = High rank, Red = Low rank
""")
with st.expander("Observations"):
    st.write("""
    * ##### Results are reassuring the positive correlation between Happiness score and GDP per capita / Social support / Healthy life expectancy
    * ##### Generosity rank is distributed evenly
    * ##### Perception of corruption has a cluster of low ranks in the Happiest 25 countries, and distributed pretty evenly in the rest
""")

# get html
p = open("figs/Heat_Map.html")
components.html(p.read(),height=400,width=1000)

with st.expander("Click for Python code here"):
    code = '''# https://plotly.com/python/heatmaps/

## Interactive Heat Map - Rank by color 

### import libraries
import plotly.express as px
import xarray as xr
import pandas as pd


# dataframe
df = pd.read_csv('2021.csv')
df_rank=df[['Happiness rank','Log GDP per capita rank','Social support rank','Healthy life expectancy rank','Freedom to make life choices rank','Generosity rank', 'Perceptions of corruption rank']]

fig = px.imshow(df_rank.T, color_continuous_scale='RdBu_r', origin='lower')
fig.write_html("C:/DS/Python/Projects/Happiness/figs/Interactive_Heat_Map.html")
fig.show()
    '''
    st.code(code, language='python')
