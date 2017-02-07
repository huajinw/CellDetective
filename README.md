# CellDetective
A python based simple software for microscopy image manupulation and analysis (for 15-112) 

To run it, you need python3.5 environment and some basic modules including: tkinter and Pillow. All  drawings and plotting are done with tkinter. The only use for Pillow is to open image formats that are not supported by tkinter (such as TIFF and JPEG) and to get pixel values. Everything else is written from scratch.  

No third party software is required.  

To run the program, you need to be able to have permission to read and write from your hard drive, since it is interactive. This is run on a Mac so its performance on Windows has not tested.  

This software has the following features: 
1) You will be able to read, write, and save images files of many formats (tested on .tif, .jpg, .gif, but should be able to do much more) 
2) You will be able to split and merge channels 
3) You will be able to apply thresholding method to generate masks and segment images.  
4) You will be able to inspect the histogram of images (pixel distribution) 
5) you will be able to use masks to quantify objects in the image, and correct for outliers.  




References: 
Sample images from https://imagej.nih.gov/ij/images/ 
and 
Murphy lab @ CMU CompBiol: http://murphylab.web.cmu.edu/data/#2DHeLa 

