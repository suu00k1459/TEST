#!/usr/bin/env python
# coding: utf-8

# In[1]:

# 'pip install openpyxl'
# 'pip install matplotlib pandas'


# In[38]:
import os
from pathlib import Path


import matplotlib.pyplot as plt
import pandas as pd


# In[ ]:


# data path

current_file = Path(__file__).resolve()
base_dir = current_file.parent

file_path_onoff = (base_dir / "../raw_data/01_rawdata/On-track and off-track countries.xlsx").resolve()
birth_path      = (base_dir / "../raw_data/01_rawdata/WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT_REV1.xlsx").resolve()
value_path      = (base_dir / "../raw_data/01_rawdata/GLOBAL_DATAFLOW_2018-2022.xlsx").resolve()



# In[ ]:


# data read

onoff_data = pd.read_excel(file_path_onoff, sheet_name='Sheet1')

birth = pd.read_excel(birth_path, sheet_name='Projections',  skiprows=16,  header=0, index_col=0) 

value_df = pd.read_excel(value_path)


# # DATA

# ### 1. on off data

# In[ ]:


# data col add
# onoff_data['ISO3_Official'] = onoff_data['ISO3Code'] + ': ' + onoff_data['OfficialName']
onoff_data['track'] = onoff_data.apply(lambda x : "Off_track" if x['Status.U5MR']=='Acceleration Needed' else "On_track", axis=1)
print(onoff_data.head())

# 



# In[4]:


print("<count of data>")
print(len(onoff_data), "\n")
print("<unique number of data>")
print(onoff_data.nunique())


# ### 2. 2022 year projection birth

# In[ ]:


birth.head(3)


# In[5]:


birth = birth.loc[:,['Region, subregion, country or area *','ISO3 Alpha-code','Births (thousands)','Year']]
birth.head(3)


# In[6]:


birth = birth.dropna(subset=['ISO3 Alpha-code'])


# In[7]:


print(birth['ISO3 Alpha-code'].nunique())


# In[9]:


birth_2022 = birth[birth['Year']==2022]
print(birth_2022.head(3),"\n")
print(len(birth_2022)) # every countries have 2022 data


# ### ANC4 & SBA

# In[ ]:


value_df.head(3)


# In[11]:


value_df = value_df.loc[:,["Geographic area","Indicator", "TIME_PERIOD", "OBS_VALUE"]]
print( value_df.head())


# In[21]:


# distinguish ANC4 and SBA

has_ANC4 = value_df[value_df['Indicator'].str.contains('4')]
has_SBA = value_df[value_df['Indicator'].str.contains('Skilled')]


# In[ ]:


print(len(value_df))
print(len(has_ANC4) + len(has_SBA))


# In[ ]:


## ANC4 :most latest data by countries 

ANC4 = has_ANC4.drop('Indicator', axis = 1)

latest_idx_ANC4 = ANC4.groupby('Geographic area')['TIME_PERIOD'].idxmax() 
ANC4 = ANC4.loc[latest_idx_ANC4].reset_index(drop=True) 

len(ANC4)


# In[22]:


ANC4.head()


# In[23]:


## SBA :most latest data by countries 


SBA = has_SBA.drop('Indicator',axis = 1)

latest_idx_SBA = SBA.groupby('Geographic area')['TIME_PERIOD'].idxmax()
SBA = SBA.loc[latest_idx_SBA].reset_index(drop=True)



# In[24]:


SBA.head(3)


# In[17]:


## merge on,off track with 2022 birth data


merged_onoff = pd.merge(
    onoff_data,
    birth_2022,
    left_on='ISO3Code',
    right_on = "ISO3 Alpha-code",
    how='right'
)

merged_onoff.dropna(subset=['Status.U5MR'], inplace= True)


# In[18]:


merged_onoff.head(3)


# In[19]:


## merge on,off track and 2022 birth data with ANC4


merged_anc4 = pd.merge(
    ANC4,
    merged_onoff,
    left_on='Geographic area',
    right_on = "OfficialName",
    how='left'
)

merged_anc4.dropna(subset=['track'] , inplace= True)


# In[25]:


## merge on,off track and 2022 birth data with SBA


merged_sba = pd.merge(
    SBA,
    merged_onoff,
    left_on='Geographic area',
    right_on = "OfficialName",
    how='left'
)

merged_sba.dropna(subset=['track'] , inplace= True)


# In[26]:


merged_sba.head(3)


# ## ANC4

# In[32]:


def weighted_avg(group):
    return (group[val_col] * group[weight_col]).sum() / group[weight_col].sum()


# In[33]:


val_col = 'OBS_VALUE'
weight_col = 'Births (thousands)'
group_col = 'track'


# In[36]:


# ANC4 avg

anc4_weighted_avg = merged_anc4.groupby(group_col).apply(weighted_avg)
anc4_weighted = anc4_weighted_avg.reset_index()
anc4_weighted.columns = ['track', 'weighted_avg']
print(anc4_weighted)


# In[46]:


# visualization

plt.figure(figsize=(8,5))
plt.bar(anc4_weighted['track'], anc4_weighted['weighted_avg'], color=["#C74239", '#1CABE2'] )

plt.title("ANC4 Coverage: On-track vs Off-track")
plt.xlabel("Track Category")
plt.ylabel("Weighted Average Coverage (%)")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig(base_dir/"../output/images/ANC4_coverage_comparison.png")
plt.show()


# ## SBA

# In[47]:


SBA_weighted_avg = merged_sba.groupby(group_col).apply(weighted_avg)
SBA_weighted = SBA_weighted_avg.reset_index()
SBA_weighted.columns = ['track', 'weighted_avg']
print(SBA_weighted)


# In[50]:


# visualization of SBA

plt.figure(figsize=(8,5))
plt.bar(SBA_weighted['track'], SBA_weighted['weighted_avg'], color=["#C74239", '#1CABE2'] )


plt.title("SBA Coverage: On-track vs Off-track")
plt.xlabel("Track Category")
plt.ylabel("Weighted Average Coverage (%)")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig(base_dir/"../output/images/SBA_coverage_comparison.png")
plt.show()

