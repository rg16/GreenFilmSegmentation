import cv2
import numpy as np


# Function : preprocess
# ---------------------
# This function crops out the black bar with imaging information at the bottom of the BSE and
# SE images

def cropBar(data):
  
  # Crop out bottom black bar
  shape = np.shape(data);
  data = data[:shape[0]-79,:];
  return data;

# Function : reduceShadows
# ------------------------
# This function reduces the effect of shadows in the image by subtracting a blurred version of
# the image from itself. 

def reduceShadows(data):
  # Subtract a scaled blurred copy of the image from itself:

  copy = data.copy();
  copy = cv2.GaussianBlur(copy, (75,75), 0);
  
  data = cv2.addWeighted(data, 1.0, copy, -.8, cv2.CV_8UC1); 
  return data;


