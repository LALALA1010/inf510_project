#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


def data_visulization(processed_df):
    player_data_df = processed_df[0]
    team_data_df = processed_df[1]

    # plot salary distribution in nba players
    sns.set_style('darkgrid')
    plt.figure(figsize=(12,12))
    plt.subplot(3,1,1) 
    sns.distplot(player_data_df['Salary'])
    plt.xticks(np.linspace(0,40,9))
    plt.ylabel(u'$Salary$',size=10)

    # plot RPM distribution in nba players
    plt.subplot(3,1,2)
    sns.distplot(player_data_df['RPM'])
    plt.xticks(np.linspace(-10,10,9))
    plt.ylabel(u'$RPM$',size=10)

    # plot Height distribution in nba players
    plt.subplot(3,1,3)
    sns.distplot(player_data_df['Height'])
    plt.xticks(np.linspace(60,100,11))
    plt.ylabel(u'$Height$',size=10)
    plt.savefig('Distribution of NBA Players')
  
    # cut the height of nba players into three level for further visulization
    player_data_df['height_cut']=player_data_df.apply(lambda x: height_cut(x),axis=1) 

    # plot the relationship between salary, rpm, and height
    sns.set_style('darkgrid') 
    plt.figure(figsize=(8,8))
    plt.title(u'$RPM\ and\ SALARY$',size=15)
    
    X1 = player_data_df.loc[player_data_df.height_cut=='very tall'].Salary
    Y1 = player_data_df.loc[player_data_df.height_cut=='very tall'].RPM
    X2 = player_data_df.loc[player_data_df.height_cut=='tall'].Salary
    Y2 = player_data_df.loc[player_data_df.height_cut=='tall'].RPM
    X3 = player_data_df.loc[player_data_df.height_cut=='not tall'].Salary
    Y3 = player_data_df.loc[player_data_df.height_cut=='not tall'].RPM

    plt.plot(X1,Y1,'.')
    plt.plot(X2,Y2,'.')
    plt.plot(X3,Y3,'.')
    plt.xlim(0,30)
    plt.ylim(-8,8)

    plt.xlabel('Salary',size=10)
    plt.ylabel('RPM',size=10)
    plt.xticks(np.arange(0,30,3))

    plt.legend(['very tall','tall','not tall'])
    plt.savefig('Relationship Between Salary, RPM, and Height')

    # plot the relationship between team win/lost ratio, PTS, and team salary
    team_dat1 = team_data_df.loc[:,['Team_Salary','W_L_Ratio','PTS']]
    sns.pairplot(team_dat1)
    plt.savefig('Relationship Between Team Win_Lost Ratio, PTS, and Team Salary')
    
# the function to cut height
def height_cut(df):
    if df.Height < 76:
        return 'not tall'
    elif df.Height > 80:
        return 'very tall'
    else:
        return 'tall'


# In[6]:





# In[28]:





# In[ ]:





# In[ ]:




