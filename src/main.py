#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas as pd
import warnings

import data_scraping as scrap
import data_storing as store
import data_modeling as model
import data_visulization as visual


# In[ ]:





# In[2]:


def main(argv):
    
    if(len(argv) == 2):
        if(argv[1] == '-source=local'):
            print("Loading data from disk and Modeling..")
            processed_df = model.data_model()        
            print('Modeling Done!')
            print('Visualizing...')
            visual.data_visulization(processed_df)
            print('All Done!')

        elif(argv[1] == '-source=remote'):
            print("Scraping data from web...")
            all_data = scrap.scrap_all_data()
            print("Storing data into disk...")
            store.store_all_data(all_data)
            print('Starting modeling data..')
            processed_df = model.data_model()
            print('Visualizing...')
            visual.data_visulization(processed_df)
            print('All Done!')     
    else:
        print('The parameter is invalid')
        print('Please enter a valid parameter: -source=remote or -source=local')
        


# In[ ]:





# In[ ]:


if __name__ == '__main__':
    main(sys.argv)

