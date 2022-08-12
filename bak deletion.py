#!/usr/bin/env python
# coding: utf-8

# In[63]:


import os
import argparse
from pathlib import Path


# In[64]:


def delete_bak(path):
    for root, directory, files in os.walk(path):
        for file in sorted(files):
            file_path = Path(os.path.join(root,file)).as_posix()
            file_lower = file.lower()
            if file_lower.endswith(('.jpg.bak','.jpeg.bak','png.bak')):
                print('%s has been deleted'%file)
                os.remove(file_path)
    print('All ".bak" files has been deleted')


# In[65]:


# parser = argparse.ArgumentParser(description='backup picture deletion')
# parser.add_argument('--directory', '-d', help='directory, required, no default values, enter "break" to quit', required = True)
# args = parser.parse_args()

# while True:
#     path_of_the_directory = args.directory
    
#     if os.path. exists(path_of_the_directory):
#         delete_bak(path_of_the_directory)
#         break
#     elif path_of_the_directory == 'break':
#         break
#     else:
#         print('Invalid Path! Try Again')
#         continue


# In[66]:


delete_bak('C:/Users/phoen/OneDrive/Desktop/test')


# In[ ]:




