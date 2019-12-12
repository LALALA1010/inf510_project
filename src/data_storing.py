#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# process the data we scrap from website and API, and combine them into one list
def process_player_data(salary_table, nba_rpm, player_height): 
    
    height_dict = player_height
    rpm_dict = nba_rpm
    
    length = len(salary_table[0])
    height_list = []
    rpm_list = []

    for player in salary_table[1]:
        if player in height_dict:
            height = height_dict[player]
            height_inch = int(height.split(" ")[0]) * 12 + int(height.split(" ")[1])
            height_list.append(height_inch)
        else:
            height_list.append('None')
            
        if player in rpm_dict:
            rpm_list.append(rpm_dict[player])
        else:
            rpm_list.append('None')
            
    player_info = salary_table
    player_info.append(height_list)
    player_info.append(rpm_list)
     
    return player_info


# In[ ]:





# In[5]:


# store the information of player into .csv file
# includes player name, position, team, salary information, and height information
def store_player_information(player_info):
    
    player_dataframe = pd.DataFrame({'Rank': player_info[0], 'Name': player_info[1], 'Position': player_info[2], 'Team': player_info[3], 'Salary':player_info[4], 'Height': player_info[5], 'RPM': player_info[6]})
    player_dataframe.to_csv("nba_player_info_data", index = False, sep = ',')
    
    return player_dataframe


# In[ ]:


def sorted_salary():
    
    money_int = lambda x: "".join(filter(str.isdigit, x))
    team_name = lambda x: x.split(' ')[-1]

    salary = pd.read_csv('nba_player_info_data', usecols=['Team', 'Salary'], converters={'Salary': money_int, 'Team': team_name})

    salary['Salary'] = salary['Salary'].astype(np.int)
    salary = salary.groupby(['Team'], as_index=False).sum()
    salary_sorted = salary.sort_values('Salary',ascending=False)

    return salary_sorted


# In[ ]:


def team_sorted_by_array():
    
    salary_sorted = sorted_salary()
    team_salary = np.array(salary_sorted).tolist()
    
    return team_salary


# In[ ]:


def process_team_data(team_info):
    #return team name, win lost ratio and pts as dictionary
    #dict_key is team name, dict_value is list including win lost ratio and pts
    nba_team_dict = team_info 
    team_salary = team_sorted_by_array()

    for item in team_salary:
        if item[0] in nba_team_dict:
            item.append(nba_team_dict[item[0]][0])
            item.append(nba_team_dict[item[0]][1])
            
    return team_salary 


# In[ ]:


def store_team_data(team_salary):

    team_info = []
    
    team_name_list = []
    team_salary_list = []
    team_w_l_ratio = []
    team_pts = []
    
    for item in team_salary:
        team_name_list.append(item[0])
        team_salary_list.append(item[1])
        team_w_l_ratio.append(item[2])
        team_pts.append(item[3])

    team_info.append(team_name_list)
    team_info.append(team_salary_list)
    team_info.append(team_w_l_ratio)
    team_info.append(team_pts)
    
    team_dataframe = pd.DataFrame({'Team_Name': team_info[0], 'Team_Salary': team_info[1], 'W_L_Ratio': team_info[2], 'PTS': team_info[3]})
    team_dataframe.to_csv("nba_team_info_data", index = False, sep = ',')
    
    return team_dataframe


# In[ ]:


def store_all_data(all_data):

    player_info = process_player_data(all_data[0], all_data[1], all_data[2])
    store_player_information(player_info)
    
    team_salary = process_team_data(all_data[3])
    store_team_data(team_salary)
    

