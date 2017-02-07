
helpMsg = """
This is a tool to perform simple segmentation and analysis of microscopy images.

Before you begin:  
The default working directory is where the program is. 
Make sure you have permission to read and write in that directory. 

Follow the following pipe line: 
1. Click the "File" menu to manipute files. 
   Select "Open" to open a file. 
   You will be asked to enter a file name or directory.
   Click "Duplicate" to make a copy. 
   Click "Save as" to save the file as name and directory of user input. 

2. Click "Channels" menu to split or merge channels. 
   To split channels, the image must be in RGB mode. 
   To merge channels, images of r, g, or b channel must be in 8-bit gray mode.

3. Click "Segmentation" to perform image segmentation using varies algorithms.
   Click "Threashold" to segment image with simple threasholding method. 
   You will be asked to enter a file name or directory.
   Input files must be in 8-bit gray mode. 
   The threashold is determined by user input. Must be a value between 0-255. 

4. Click "Analysis" to analysze origianl and processed images.

"""
