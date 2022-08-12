# picture_conmpression
This script is dedicated to boost the website loading speed by compress picture sizes
## Basic Information
Creator: Phoenix(Jiayu)
Version: Python 3.6
Purpose: Compress the size of pictures, so the website loading speed can be approved
Files: **Picture_Compressor_All.py, Picture_Compressor_Yesterday.py, bak_deletion.py**
Required library: PIL, datetime, shutil, pathlib
Optional library: argparse

## Description
1. The script will loop through the directory and look for all pictures inside the directory. No need to run multiple times for different directories.
2. This script will only compress pictures in **jpg, jpeg and png** formats.
3. Files will be compressed under 300kb.
4. Files **under 100 kb** will not be compressed.
5. The original pictures will be stored as .bak files for further needs. You can delete the .bak files with **bak_deletion** if you do not need them.
6. The date of the file is determined by **Createion Date** instead of modified date.

### Instruction
1. Run the Picture_Compressor_All.py first to compress all pictures thats already on the server.
2. Setup a schedule which runs Picture_Compressor_Yesterday.py at the very beginning of the day to compress new pictures uploaded
3. Delete bak files if needed with bak_deletion.py

WARNING: DO not run the Picture_Compressor_All.py twice, and do not run Picture_Compressor_Yesterday.py twice in a day

Two types of operating senario:
1. Run script in normal Python IDE: 
 run all defs, and call the compressor_main function with file directory inside
  
  e.g.: compressor_main('C:/test')


2. Under the linux command system: install all the required libraries first then run the script, uncommend the last section of the code.
  
  e.g.: python3 Picture_Compressor_All.py -d "enter your directory here"
