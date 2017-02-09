# CellDetective
A python based simple software for microscopy image manupulation and analysis (for 15-112) 

To run it, you need python3.5 environment and some basic modules including: tkinter and Pillow. All  drawings and plotting are done with tkinter. The only use for Pillow is to open image formats that are not supported by tkinter (such as TIFF and JPEG) and to get pixel values. Everything else is written from scratch.  

No third party software is required.  

To run the program, you need to have permission to read and write from the hard drive. This version is tested on Mac OS X.  Its performance on Windows has not tested.  

This software has the following features: 
1) File manipulation: read, write, and save image files of many formats (tested on .tif, .jpg, .gif, but should be able to do much more) 
2) Channel manipulation: split and merge channels 
3) Perform image segmentation using thresholding method 
4) Inspect the histogram of images (pixel distribution) 
5) Use masked image to quantify objects in the image, and correct for outliers




References: 
Sample images from https://imagej.nih.gov/ij/images/ 
and 
Murphy lab @ CMU CompBiol: http://murphylab.web.cmu.edu/data/#2DHeLa 

