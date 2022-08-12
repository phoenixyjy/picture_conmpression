#!/usr/bin/env python
# coding: utf-8

# In[5]:


### Author: Phoenix(Jiayu) Yan
### Python Version: 3.6
### Usage: input the file directory right after calling the function
### e.g.: python3 resize.py -d Images, where Images is the directory of the file folder



import os
from PIL import Image
from PIL import ImageFile
from pathlib import Path
import datetime
from datetime import time
import shutil
import argparse


def copy_creator(directory):
    copy_directory = directory + '.bak'
    shutil.copy(directory,copy_directory)
    
def jpg_compression(root, directory, file, a_list):
    
    copy_creator(directory)
    
    picture = Image.open(directory).convert('RGB')
    
    w,h = picture.size
    
    picture = picture.resize((int(w*0.8),int(h*0.8)), Image.ANTIALIAS)
    
    print("Picture Compressed: %s"%(file))
    
    picture.save(directory, optimize=True, progressive=True, quality=50)
    
    recrusive_compression(directory, file, a_list)
    
    return a_list



def png_compression(root, directory, file, a_list):
    
    picture = Image.open(directory).convert('RGB')
    
    w,h = picture.size

    picture = picture.resize((int(w*0.8),int(h*0.8)), Image.ANTIALIAS)

    new_name = file.replace('.png','.jpg')
    
    save_directory = Path(os.path.join(root,new_name)).as_posix()

    picture.save(save_directory, optimize=True, progressive=True, quality=50)

    recrusive_compression(save_directory, file, a_list)
    
    os.rename(directory,(directory+'.bak'))

    os.rename(save_directory,directory)
    
    print("Picture Compressed: %s"%(file))
    
    return a_list




def recrusive_compression(directory,file,a_list):
    
    new_size = os.path.getsize(directory)
    
    i = 0
    
    for i in range(0,2):
    
        if new_size > 300000 and new_size <= 800000:
            picture = Image.open(directory)
            w,h = picture.size
            picture = picture.resize((int(w*0.5),int(h*0.5)), Image.ANTIALIAS)
            picture.save(directory, optimize=True, progressive=True, quality=40)
            new_size = os.path.getsize(directory)
            i += 1
            print("Advanced Picture Compression for: %s,attemps %s "%(file,i))
            print(i)
        
        elif new_size > 800000:
            picture = Image.open(directory)
            w,h = picture.size
            picture = picture.resize((int(w*0.2),int(h*0.2)), Image.ANTIALIAS)
            picture.save(directory, optimize=True, progressive=True, quality=40)
            new_size = os.path.getsize(directory)
            i += 1
            print("Advanced Picture Compression for: %s,attemps %s "%(file,i))
            print("Identifier %s"%i)
        else:
            break
        
        if i == 2:
            a_list.append(directory.replace('.png','').replace('.jpg',''))
    return a_list



def compressor_main(path_of_the_directory):
    # comtainer of cautiousness
    a_list = []
    # unlimit picture size, and skip broken pictures
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    Image.MAX_IMAGE_PIXELS = None
    
    # loop through diretory 
    for root, dirs, files in os.walk(path_of_the_directory):
        for file in sorted(files):
            # correct the directory formate, specific for Windows system
            picture_directory = Path(os.path.join(root,file)).as_posix()
            # check file size
            size = os.path.getsize(picture_directory)
            file_lower = file.lower()
                # process jpg, jpeg
            if file_lower.endswith(('jpg','jpeg')):
                if size >= 100000:
                    print("%s : file size %s"%(picture_directory,size))
                    jpg_compression(root,picture_directory,file,a_list)

                # process png files
            elif file_lower.endswith('png'):
                if size >= 100000 :
                    print("%s : file size %s"%(picture_directory,size))
                    png_compression(root,picture_directory,file,a_list)
                
    # check if there are extreme large files required for manual operations
    if len(a_list) != 0:
        print("The following files require manually check: ")
        for each in a_list:
            print(each)
    else:
        print('All pictures has been compressed normally')
    return a_list



# parser = argparse.ArgumentParser(description='Image Compressor')
# parser.add_argument('--directory', '-d', help='directory, required, no default values, enter break to quit', required = True)
# args = parser.parse_args()

# while True:
#     path_of_the_directory = args.directory
    
#     if os.path. exists(path_of_the_directory):
#         result = compressor_main(path_of_the_directory)
#         break
#     elif path_of_the_directory == 'break':
#         break
#     else:
#         print('Invalid Path!')
#         continue


# In[7]:


compressor_main('C:/test")


# In[ ]:




