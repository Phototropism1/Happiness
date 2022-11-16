# In[]:


# In[]:

## World Map - color by country
### Libraries

import pandas as pd
import numpy as np
import os
import plotly.express as px
from matplotlib.pyplot import figure
# In[]:

## directory + Import data
os.chdir('C:/DS/Python/Projects/Happiness')
# import csv
country = pd.read_csv('2021.csv')

# In[]:

### World map 1 - Country by Happiness rank

v1='Happiness rank'
h1='Log GDP per capita rank'

np.random.seed(12)
gapminder = country
gapminder['country names'] = np.random.uniform(low=100000, high=200000, size=len(gapminder)).tolist()
fig = px.choropleth(gapminder, locations="Country name",
                    locationmode='country names',
                    color=v1, 
                    hover_name="Country name",title="World map - Country by " + v1,
                    hover_data=[h1],
                    range_color=[20,80],  
                    color_continuous_scale='RdYlGn_r')

figure(figsize=(10, 16), dpi=80)
fig.show()
# In[]:

## World map 2 - Country by Log GDP per capita rank

v1='Log GDP per capita rank'
h1='Happiness rank'

np.random.seed(12)
gapminder = country
gapminder['country names'] = np.random.uniform(low=100000, high=200000, size=len(gapminder)).tolist()
fig = px.choropleth(gapminder, locations="Country name",
                    locationmode='country names',
                    color=v1, 
                    hover_name="Country name",title="World map - Country by " + v1,
                    hover_data=[h1],
                    range_color=[20,80],  
                    color_continuous_scale='RdYlGn_r')

figure(figsize=(10, 16), dpi=80)
fig.write_html("C:/DS/Python/Projects/Happiness/figs/Map_"+v1+".html")
fig.show()
# In[]:

##PCA

### Import libraries
import pca
from pca import pca
from plotly import plotly.io

# In[9]:

### Define columns
df = pd.read_csv('2021.csv')
X=df[['Happiness Score','Log GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption']]
# In[10]:

# Initialize
model = pca(n_components=2, normalize=True)

# Fit transform
out= model.fit_transform(X)

# PCA vectors
fig=plt, ax = model.biplot(cmap=None, 
                       label=False, legend=False)
                       
figure(figsize=(10, 16), dpi=80)
plt.savefig('C:/DS/Python/Projects/Happiness/figs/PCA.png')

# In[]:

## Scatter

### import libraries
import os # importing module
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px # interactive Scatter plot
from scipy import stats # curve calculations


# In[]:

### Scatter 1 - Hapiness Score Vs Hapiness rank
v1='Happiness Score'
v2='Happiness rank'
x=df[v1]
y=df[v2]
h1='Country name'
h2='Happiness rank'
h3='Log GDP per capita rank'
c='Regional indicator'
s='Log GDP per capita'

res = stats.linregress(x, y)
r2=f"R-squared: {res.rvalue**2:.6f}"

fig = px.scatter(df, x, y,
                 title= (v1 + " Vs " + v2 +
                 '<br>' + str(r2)),
                 color=df[c], size=df[s], size_max=10,
                 trendline="ols", trendline_scope="overall",
                 hover_data=[h3,h1])
fig.write_html("C:/DS/Python/Projects/Happiness/figs/"+ v1 + "_Vs_" + v2 + ".html")

fig.show()
# In[]:

# In[]:

### Scatter 2 - Hapiness Score Vs Log GDP per capita
v1='Happiness Score'
v2='Log GDP per capita'
x=df[v1]
y=df[v2]
h1='Country name'
h2='Happiness rank'
h3='Log GDP per capita rank'
c='Regional indicator'
s='Log GDP per capita'

res = stats.linregress(x, y)
r2=f"R-squared: {res.rvalue**2:.6f}"

fig = px.scatter(df, x, y,
                 title= (v1 + " Vs " + v2 +
                 '<br>' + str(r2)),
                 color=df[c], size=df[s], size_max=10,
                 trendline="ols", trendline_scope="overall",
                 hover_data=[h3,h2, h1])
fig.write_html("C:/DS/Python/Projects/Happiness/figs/"+ v1 + "_Vs_" + v2 + ".html")

fig.show()
# In[]:

### Scatter 3 - Hapiness Score Vs Social support
v1='Happiness Score'
v2='Social support'
x=df[v1]
y=df[v2]
h1='Country name'
h2='Happiness rank'
h3=v2+" rank"
c='Regional indicator'
s='Log GDP per capita'

res = stats.linregress(x, y)
r2=f"R-squared: {res.rvalue**2:.6f}"

fig = px.scatter(df, x, y,
                 title= (v1 + " Vs " + v2 +
                 '<br>' + str(r2)),
                 color=df[c], size=df[s], size_max=10,
                 trendline="ols", trendline_scope="overall",
                 hover_data=[h3,h2, h1])
fig.write_html("C:/DS/Python/Projects/Happiness/figs/"+ v1 + "_Vs_" + v2 + ".html")

fig.show()
# In[]:

### Scatter 4 - Hapiness Score Vs Healthy life expectancy
v1='Happiness Score'
v2='Healthy life expectancy'
x=df[v1]
y=df[v2]
h1='Country name'
h2='Happiness rank'
h3=v2+" rank"
c='Regional indicator'
s='Log GDP per capita'

res = stats.linregress(x, y)
r2=f"R-squared: {res.rvalue**2:.6f}"

fig = px.scatter(df, x, y,
                 title= (v1 + " Vs " + v2 +
                 '<br>' + str(r2)),
                 color=df[c], size=df[s], size_max=10,
                 trendline="ols", trendline_scope="overall",
                 hover_data=[h3,h2, h1])
fig.write_html("C:/DS/Python/Projects/Happiness/figs/"+ v1 + "_Vs_" + v2 + ".html")

fig.show()
# In[]:

### Scatter 5 - Hapiness Score Vs Freedom to make life choices
v1='Happiness Score'
v2='Freedom to make life choices'
x=df[v1]
y=df[v2]
h1='Country name'
h2='Happiness rank'
h3=v2+" rank"
c='Regional indicator'
s='Log GDP per capita'

res = stats.linregress(x, y)
r2=f"R-squared: {res.rvalue**2:.6f}"

fig = px.scatter(df, x, y,
                 title= (v1 + " Vs " + v2 +
                 '<br>' + str(r2)),
                 color=df[c], size=df[s], size_max=10,
                 trendline="ols", trendline_scope="overall",
                 hover_data=[h3,h2, h1])
fig.write_html("C:/DS/Python/Projects/Happiness/figs/"+ v1 + "_Vs_" + v2 + ".html")

fig.show()
# In[]:

### Scatter 6 - Hapiness Score Vs Perceptions of corruption
v1='Happiness Score'
v2='Perceptions of corruption'
x=df[v1]
y=df[v2]
h1='Country name'
h2='Happiness rank'
h3=v2+" rank"
c='Regional indicator'
s='Log GDP per capita'

res = stats.linregress(x, y)
r2=f"R-squared: {res.rvalue**2:.6f}"

fig = px.scatter(df, x, y,
                 title= (v1 + " Vs " + v2 +
                 '<br>' + str(r2)),
                 color=df[c], size=df[s], size_max=10,
                 trendline="ols", trendline_scope="overall",
                 hover_data=[h3,h2, h1])
fig.write_html("C:/DS/Python/Projects/Happiness/figs/"+ v1 + "_Vs_" + v2 + ".html")

fig.show()
# In[]:

## Tabular data - Rank by color

### import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import HTML

#In[]
df = pd.read_csv('2021.csv')
df_rank=df[['Country name','Regional indicator','Happiness rank','Log GDP per capita rank','Social support rank','Healthy life expectancy rank','Freedom to make life choices rank','Generosity rank', 'Perceptions of corruption rank']]

# Set CSS properties for th elements in dataframe
th_props = [
  ('font-size', '11px'),
  ('text-align', 'center'),
  ('font-weight', 'bold'),
  ('color', '#6d6d6d'),
  ('background-color', '#f7f7f9')
  ]

# Set CSS properties for td elements in dataframe
td_props = [
  ('font-size', '11px')
  ]

# Set table styles
styles = [
  dict(selector="th", props=th_props),
  dict(selector="td", props=td_props)
  ]

# Set colormap
cm = sns.color_palette('Greens_r', as_cmap=True)

(df_rank.style
  .background_gradient(cmap=cm, subset=['Happiness rank','Log GDP per capita rank','Social support rank','Healthy life expectancy rank','Freedom to make life choices rank','Generosity rank', 'Perceptions of corruption rank'])
  .set_caption('Hapiness rank Vs variable rank')
  .set_table_styles(styles))

#In[]

#https://www.python-graph-gallery.com/heatmap/

##Heat map - Rank by color 

### import libraries
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

# dataframe
df = pd.read_csv('2021.csv')
df_rank=df[['Happiness rank','Log GDP per capita rank','Social support rank','Healthy life expectancy rank','Freedom to make life choices rank','Generosity rank', 'Perceptions of corruption rank']]
df = df_rank.set_index('Generosity rank')
 
# Default plot
sns.clustermap(df)

# Show the graph
plt.show()
#In[]

# https://plotly.com/python/heatmaps/

## Interactive Heat Map - Rank by color 

### import libraries
import plotly.express as px
import xarray as xr
import pandas as pd


# dataframe
df = pd.read_csv('2021.csv')
df_rank=df[['Happiness rank','Log GDP per capita rank','Social support rank','Healthy life expectancy rank','Freedom to make life choices rank','Generosity rank', 'Perceptions of corruption rank']]

fig = px.imshow(df_rank.T, color_continuous_scale='RdBu_r', origin='lower')



fig.write_html("C:/DS/Python/Projects/Happiness/figs/Heat_Map.html")
fig.show()
# %%
