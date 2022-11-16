# In[]:
import PIL
import streamlit  as st


# In[]:
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Principal Component Analysis (PCA) ↭",
    page_icon="↭"
)
st.markdown("### Principal Component Analysis (PCA)")
st.markdown("### Two dimensional variable vector map")
st.markdown("")
st.markdown("### Methodology")
st.write("""
    ###### Principle Component Analysis (PCA) is a great model to reduce multiple dimensions into few dimensions (in this case two: x and y axis)
    ###### The dimension distance between each vector (variable) represent the linear difference between the variables
    ###### In this analysis 7 variables are represented as vectors in the PCA plot
    """)
with st.expander("Observations"):
    st.write("""
    * ###### The Happiness vector is in the same direction as the Log GDP per capita / Social support / Healthy life expectancy cluster !
    ###### Meaning that the vectors are correlated, maybe a hint to the Money and happiness / health connection ?!
    * ###### Generosity vector is far from the above cluster (not necessary for Happiness ?)
    * ###### Perception of corruption vector is far from them all !
    ###### Model explains 74.3% of data variability: X axis= 55.9%, Y axis = 18.4%
""")

image = Image.open('C:/DS/Python/Projects/Happiness/figs/R-PCA.png')

st.image(image, caption='Sunrise by the mountains',width=600)

with st.expander("Click for R code here"):
    code = '''
    library(ggplot2)
    library(factoextra)
    library(tidyverse)
    library(stats)
    library(plotly)
    library(ggpubr)
    library(ggpmisc)
    library(devtools)
    library(ggbiplot)


    setwd("C:/DS/Python/Projects/Happiness")
    happy.2021 <-read.csv("2021-PCA.csv")

    ## df
    df <- select (happy.2021, c("Happiness.Score","Log.GDP.per.capita","Social.support","Healthy.life.expectancy","Freedom.to.make.life.choices","Generosity","Perceptions.of.corruption"))

    ##http://www.sthda.com/english/articles/31-principal-component-methods-in-r-practical-guide/118-principal-component-analysis-in-r-prcomp-vs-princomp/

    happy.pca <- df
    res.pca <- prcomp(happy.pca, scale=TRUE)
    fviz_pca_var(res.pca,
                col.var = "contrib", # Color by contributions to the PC
                gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07"),
                repel = TRUE     # Avoid text overlapping
    )
    happy.pca


    '''
    st.code(code, language='python')
