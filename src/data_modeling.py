#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[11]:


def data_model():
    processed_df = []
    
    ori_team_data_df = pd.read_csv('nba_team_info_data')
    ori_player_data_df = pd.read_csv('nba_player_info_data')

    team_data_df = ori_team_data_df.copy()
    player_data_df = ori_player_data_df.copy()

    # remove the row which doesn't contain information 
    player_data_df = player_data_df[player_data_df.astype(str).ne('None').all(1)] 
    
    player_data_df = player_data_df.replace(['SF', 'PF'], 'F')
    player_data_df = player_data_df.replace(['SG', 'PG'], 'G')
    
    
    # transfer the salary from str to float, and represent it in unit of million
    ori_salary_list = player_data_df['Salary'].tolist()
    
    salary_list = []
    
    for i in range(len(ori_salary_list)):
        temp = ori_salary_list[i].split(',')
        temp_str = ''
        for j in range(len(temp)):
            temp_str += temp[j]
        salary_list.append(round(float(temp_str)/1000000,4))
        
    player_data_df['Salary'] = salary_list
    
    # transfer the rpm list from str to float for further analysis
    ori_rpm_list = player_data_df['RPM'].tolist()

    for i in range(len(ori_rpm_list)):     
        ori_rpm_list[i] = float(ori_rpm_list[i])

    player_data_df['RPM'] = ori_rpm_list
    
    # transfer the type of height from str to float for further analysis
    ori_height_list = player_data_df['Height'].tolist()

    for i in range(len(ori_height_list)):     
        ori_height_list[i] = int(ori_height_list[i])

    player_data_df['Height'] = ori_height_list
    
    processed_df = [player_data_df, team_data_df]
    
    return processed_df


# In[ ]:





# In[ ]:




