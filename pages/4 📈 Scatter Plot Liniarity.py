import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Scatter Plot linearity 📈",
    page_icon="📈"
)

st.markdown("## Scatterplot")
st.markdown("### Happiness score Vs each variable score")
st.markdown("")
st.markdown("#### Key Findings")
st.write("""
* ##### Results are reassuring the positive correlation between Happiness score and GDP per capita / Social support / Healthy life expectancy
* ##### Distribution of Freedom to make life choices scores decreases as Happiness score increases
* ##### The correlation between low perception of corruption and increased Happiness scores exist only in the happiest 20 countries
""")
with st.expander("Model Features"):
    st.write("""
    * ##### Each country represented by a dot
    * ##### Dot size: Log GDP per capita
    * ##### Regional indicator: by color, legend on the right
    * ##### Linearity: R^2 value in the header
    * ##### Hover to see country details
    * ##### Zoom: right click and drag
""")
with st.expander("Observations: Happiness (X) Vs Log GDP per Capita (Y), n=149"):
    st.write("""
    * ##### Overall, there is a linearity between Happiness and Log GDP per capita scores
    ##### When you have more money you will be probably happier (-;
    * ##### Strong correlation in the highest range X>30
""")

p = open("figs/Happiness Score_Vs_Log GDP per capita.html")
components.html(p.read(),height=500,width=1000)

with st.expander("Observations: Happiness (X) Vs Healthy life expectancy (Y), n=149"):
    st.write("""
    * ##### Overall, there is a linearity between Happiness and Healthy life expectancy
    * ##### Strong correlation in the highest range X>20
    * ##### Western Europe has the highest Y values
    * ##### Africa has the lowest Y values
    * ##### Significant outliers:
        * Hong Kong: X=77 Y=2
        * Singapore: X=32 Y=1
        * Ivory coast: X = 85 Y = 146
""")

p = open("figs/Happiness Score_Vs_Healthy life expectancy.html")
components.html(p.read(),height=500,width=1000)

with st.expander("Observations: Happiness (X) Vs Social support (Y), n=149"):
    st.write("""
    * ##### Overall, there is a linearity between Happiness and Social support scores
    * ##### Strong correlation in the highest range X>80
    * ##### High distribution in the lower range X<80
    * ##### Significant outliers:
        * Turkmenistan: X=97 Y=2
        * Benin: X=32 Y=1
        * Ivory coast: X = 99 Y = 148
""")

p = open("figs/Happiness Score_Vs_Social support.html")
components.html(p.read(),height=500,width=1000)

with st.expander("Observations: Happiness (X) Vs Freedom to make life choices (Y), n=149"):
    st.write("""
    * ##### The distribution of Freedom to make life choices decreases in dependency to the Happiness score
    * ##### Southeast Asia has the highest Y values
    * ##### Africa and the Middle east has the lowest Y values
""")

p = open("figs/Happiness Score_Vs_Freedom to make life choices.html")
components.html(p.read(),height=500,width=1000)

with st.expander("Observations: Happiness (X) Vs Perceptions of corruption (Y), n=149"):
    st.write("""
    * ##### The correlation between low perception of corruption and Happiness scores exist only in the happiest 20 countries
    * ##### Significant outliers:
    * Singapore: X=32 Y=149 (last on corruption rank)
    * Rwanda: X=147 Y=148 (one before last on the corruption rank, strange...)
    * Iceland: X=4 Y=111
    * Israel: X=12 Y=84
""")

p = open("figs/Happiness Score_Vs_Perceptions of corruption.html")
components.html(p.read(),height=500,width=1000)
