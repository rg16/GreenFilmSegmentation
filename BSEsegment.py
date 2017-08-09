import cv2
import numpy as np


# Function : BSEsegment
# ---------------------
# This function finds the primary and secondary phase in the image using the thresholding function
# and arguments provided by fn and *args. 

def BSEsegment(data, outputDir):

  _, primaryMaskOT = cv2.threshold(data, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU);
  primaryMaskAT = cv2.adaptiveThreshold(data, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv2.THRESH_BINARY, 175, 0);

  primaryMask = cv2.bitwise_and(primaryMaskOT, primaryMaskAT); 
  primary = cv2.bitwise_and(data, primaryMask);

  inverted = cv2.bitwise_not(data);
  removed = cv2.bitwise_and(inverted, cv2.bitwise_not(primaryMask));
  equalized = cv2.equalizeHist(removed); 

  # Adaptive Thresholding:
  poreMaskAT = cv2.adaptiveThreshold(equalized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 25, -40); 
 
  # Otsu Thresholding:
  _, poreMaskOT = cv2.threshold(equalized, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU);

  # Basic Thresholding:
  _, poreMask = cv2.threshold(equalized, 210, 255, cv2.THRESH_BINARY);
    
  segment(data, primaryMask, poreMaskAT, outputDir + '/adaptive_output.tif');
  segment(data, primaryMask, poreMaskOT, outputDir + '/otsu_output.tif');
  segment(data, primaryMask, poreMask, outputDir + '/threshold_output.tif'); 


def segment(data, mask1, mask2, filename):

  primary = oneColor(mask1, 0, 2); 
  pores = oneColor(mask2, 1, 2);
  
  mask3 = cv2.bitwise_and(cv2.bitwise_not(mask1), cv2.bitwise_not(mask2)); 
  secondary = oneColor(mask3, 0, 1); 

  cv2.imwrite(filename, primary + secondary + pores); 


def oneColor(img, index1, index2):
 
  img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB);

  img[:,:,index1] = 0;
  img[:,:,index2] = 0;

  return img; 
