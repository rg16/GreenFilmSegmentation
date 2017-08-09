import os
import string
import argparse
import cv2

# Function : parseArgs
# --------------------
# This function prepares the input to be processed. The input should be an image or a directory 
# with images. If the directory contains other files that are not images, they are ignored. 
# But any .tif file in the directory will be considered as an input to the program, so be careful
# not to have any improper .tif files in the directory provided. This function returns a list 
# of filepaths of the images to be processed (if a single file was provided, the function returns
# a list with a single element), each file path paired with the name of the image (taken to be 
# the part of the filename before the .tif)

def parseArgs():

  parser = argparse.ArgumentParser();
  parser.add_argument('path', help='Path to image or directory to be processed');
  path = parser.parse_args().path; 
  
  if not os.path.exists(path):
    print("Error : provided path \"" + path +"\" does not exist.");
    exit(); 

  if os.path.isdir(path): 
 
    fps = []; 
    for name in os.listdir(path):

      fp = path + '/' + name;
      if '.tif' in name.lower() and os.path.isfile(fp):
        nm = string.split(name, '.tif')[0];
        fps.append((fp,nm));

    return fps;

  elif os.path.isfile(path):
    name = string.split(os.path.basename(path),'.tif')
    return [path];
       

# Function : safeRead
# -------------------
# This function takes a .tif file as input and reads it. If the file is not read correctly, it
# raises an error. Otherwise it returns the image data. 

def safeRead(f): 

  data = cv2.imread(f, cv2.CV_8UC1);
  if (data is None):
    raise TypeError('Unable to read file', f);
  return data;


# Function : getOutputDir
# -----------------------
# Given a path to a file, this function finds or creates an output directory in the same directory
# as the input file. 

def getOutputDir(p):

  d = os.path.dirname(p[0]);
  outputDir = d + '/Output/'+p[1];
  if not os.path.isdir(outputDir):
    os.makedirs(outputDir);
  return outputDir;

# Function : getDir
# -----------------
# This function just takes the beginning and ending part of a directory and combines them into 
# one full directory. If the directory doesn't already exist, it makes the directory. 

def getDir(dirname, basename):

  d = dirname +'/'+ basename;
  if not os.path.isdir(d):
    os.makedirs(d);
  return d;
