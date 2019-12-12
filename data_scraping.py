#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from bs4 import BeautifulSoup, Comment
import json


# In[9]:


# the webpage we need to scrap salary data of nba players in 2018-2019
def nba_salary_web(page_number): 
    
    if page_number == 1:
        url = 'http://www.espn.com/nba/salaries/_/year/2019'
    else:
        url = f'http://www.espn.com/nba/salaries/_/year/2019/page/{page_number}' 
        
    return url

# scrap the name, position, team, and salary information of nba players. It is ranked by the amount of salary. 
# and return it as a list
def nba_salary(): 
    
    salary_table = []

    rank_list = []
    name_list = []
    position_list = []
    team_list = []
    salary_list = []
    
    for i in range(13):
        url = nba_salary_web(i+1)
    
        try: 
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e)

        soup = BeautifulSoup(response.content, 'lxml')

        main_table = soup.find_all('td')


        for i in range(len(main_table)):
            if (i % 4 == 0 and i % 11 != 0):
                rank_list.append(main_table[i].text)
            elif (i % 4 == 1 and i % 11 != 1):
                name_list.append(main_table[i].find('a').text)
                position_list.append(main_table[i].text.split(',')[1].strip()) 
            elif (i % 4 == 2 and i % 11 != 2):
                team_list.append(main_table[i].text)
            elif (i % 4 == 3 and i % 11 != 3):
                salary_list.append(main_table[i].text[1:])
                
    salary_table.append(rank_list)
    salary_table.append(name_list)
    salary_table.append(position_list)
    salary_table.append(team_list)
    salary_table.append(salary_list)
    
    return salary_table


# In[ ]:





# In[2]:


# the webpage we need to scrap Real Plus-Minus data of nba players in 2018-2019
def nba_rpm_web(page_number):  
    
    if page_number == 1:
        url = 'http://www.espn.com/nba/statistics/rpm/_/year/2019'
    else:
        url = f'http://www.espn.com/nba/statistics/rpm/_/year/2019/page/{page_number}' 
        
    return url

# scrap the name, and rpm information of nba players. 
def nba_rpm(): 
    
    name_list = []
    rpm_list = []
    rmp_dict = {}
    
    for i in range(13):
        
        url = nba_rpm_web(i+1)
    
        try: 
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e)

        soup = BeautifulSoup(response.content, 'lxml')

        main_table = soup.find_all('td')
        
        for i in range(len(main_table)):
            if (i % 9 == 7 and i != 7):
                rpm_list.append(main_table[i].text)
            elif(i % 9 == 1 and i != 1):
                name_list.append(main_table[i].find('a').text)
                
    for i in range(len(name_list)):
        rmp_dict[name_list[i]] = rpm_list[i]
          
    return rmp_dict


# In[ ]:





# In[3]:


def nba_player_api(page_number):   
    
    url = f'https://www.balldontlie.io/api/v1/players?page={page_number}&per_page=100'
    
    return url

def player_height():
    
    height_dict = {}
    
    total_pages = 33 # got this information from metadata
    
    for page in range(total_pages):
        
        try: 
            url = nba_player_api(page+1)
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e)
            
        soup = BeautifulSoup(response.content, 'lxml')

        response_dict = response.json()


        for i in range(len(response_dict['data'])):
            if response_dict['data'][i]['height_feet'] != None and response_dict['data'][i]['height_inches'] != None:
                height_key = response_dict['data'][i]['first_name'] + " " + response_dict['data'][i]['last_name'] 
                height_value = str(response_dict['data'][i]['height_feet']) + " " + str(response_dict['data'][i]['height_inches'])           
                height_dict[height_key] = height_value
                
    return height_dict


# In[ ]:





# In[13]:


# the webpage we need to scrap data of nba teams in 2018-2019
def require_nba_team_info():
    
    nba_team_url = 'https://www.basketball-reference.com/leagues/NBA_2019.html'   
    
    try: 
        response = requests.get(nba_team_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        
    soup = BeautifulSoup(response.content, 'lxml')
    
    return soup

# scrap the team name, win lost ratio and pts of nba teams in 2019. 
# and return it as a dictionary
def team_info(): 
    
    soup = require_nba_team_info()
    
    nba_team_dict = {}

    team_list = []
    win_lost_ratio_list = []
    pts_list = []
    
    team_name_col = soup.find_all('th', attrs = {'data-stat':'team_name'})
    win_loss_pct_col = soup.find_all('td', attrs = {'data-stat':'win_loss_pct'})
    pts_col = soup.find_all('td', attrs = {'data-stat':'pts_per_g'})

    for i in range(len(team_name_col)):
        if i > 0 and i != 16 and i < 32 :
            if '*' in team_name_col[i].text:
                team_list.append(team_name_col[i].text.split('*')[0].split(' ')[-1])
            else:
                team_list.append(team_name_col[i].text.split('(')[0].strip().split(' ')[-1])

    for i in range(len(win_loss_pct_col)):
        if i < 30:
            win_lost_ratio_list.append(win_loss_pct_col[i].text)
        
    for i in range(len(pts_col)):
        if i < 30:
            pts_list.append(pts_col[i].text)
    
    index = 0
    for team in team_list:
        temp_list = []
        temp_list.append(win_lost_ratio_list[index])
        temp_list.append(pts_list[index])
        nba_team_dict[team] = temp_list
        index += 1
        
    return nba_team_dict


# In[ ]:


def scrap_all_data():
    
    all_data = []
    
    # combine all data together inorder to store and analyze them further
    all_data = [nba_salary(), nba_rpm(), player_height(), team_info()]
    
    return all_data
    
    


# In[ ]:




