#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datascience import *
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

from urllib.request import urlopen 
import re
def read_url(url): 
    return re.sub('\\s+', ' ', urlopen(url).read().decode())


# In[2]:


little_women_url = 'https://www.inferentialthinking.com/data/little_women.txt'
little_women_text = read_url(little_women_url)
chapters = little_women_text.split('CHAPTER ')[1:]


# In[3]:


Table().with_column('Text', chapters)


# In[4]:


np.char.count(chapters, 'Christmas')


# In[5]:


np.char.count(chapters, 'Jo')


# In[6]:


Table().with_columns(
    'Jo', np.char.count(chapters, 'Jo'),
    'Meg', np.char.count(chapters, 'Meg'),
    'Amy', np.char.count(chapters, 'Amy'),
    'Beth', np.char.count(chapters, 'Beth'),
    'Laurie', np.char.count(chapters, 'Laurie')
)


# <br><br><br><br><br><br><br>

# ## Visualization

# In[ ]:


Table().with_columns(
    'Jo', np.char.count(chapters, 'Jo'),
    'Meg', np.char.count(chapters, 'Meg'),
    'Amy', np.char.count(chapters, 'Amy'),
    'Beth', np.char.count(chapters, 'Beth'),
    'Laurie', np.char.count(chapters, 'Laurie')
).cumsum().plot()


# <br><br><br><br><br><br><br>

# ## Visualizing chapter length vs number of periods

# In[ ]:


Table().with_columns([
        'Chapter Length', [len(c) for c in chapters],
        'Number of Periods', np.char.count(chapters, '.'),
    ]).scatter('Number of Periods')

