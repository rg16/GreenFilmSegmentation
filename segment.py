import os
import string
import cv2
import time
import sys

import fileManager as fm
import preprocess as pre
import BSEsegment as bse

# Function : main
# ---------------
# This function primarily handles the task of segmenting the image by delegating tasks to 
# functions in other files. 

def main():

  pathNames = fm.parseArgs(); 
  i = 1;
  total = len(pathNames);
  for p in pathNames:

    start = time.time(); 
    print "";
    print("Beginning ["+str(i)+"] of "+str(total)+" ... "),
    sys.stdout.flush();

    path = p[0];
    name = p[1];

    try:
      data = fm.safeRead(path);
    except TypeError as e:
      print e[0] + ' : \"' + e[1] + '\"';
      print "Continuing onto rest of files";
      continue;

    outputDir = fm.getOutputDir(p);

    cv2.imwrite(outputDir + '/original_data.tif', data);
    data = pre.cropBar(data); 
    data = pre.reduceShadows(data);
    cv2.imwrite(outputDir + '/preprocessed.tif', data);

    bse.BSEsegment(data, outputDir);
     
    end = time.time();
    print("Done (time (s) : "+str(end-start)+")");

if __name__ == '__main__':
  main(); 
  print "";
