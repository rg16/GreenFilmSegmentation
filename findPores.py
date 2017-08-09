import os
import cv2
import string
import time
import sys

import fileManager as fm
import preprocess as pre

# Function : main
# ---------------
# This function primarily handles the task of finding pores in the image by delegating tasks to
# helper functions in other files. It does do some error handling and image writing, and takes
# care of writing to stdout so the user knows what's going on. 

def main():

  pathNames = fm.parseArgs();
  i = 1;
  total = len(pathNames);

  for p in pathNames:

    start = time.time()
    print "";
    print("Beginning [" + str(i) + "] of "+str(total)+" ... "),
    sys.stdout.flush();

    path = p[0];
    name = p[1];
  
    try:
      data = fm.safeRead(path);
    except TypeError as e:
      print e[0] + ' : \"' + e[1] +'\"';
      print "Continuing onto rest of files";
      continue;

    outputDir = fm.getOutputDir(p);
  
    cv2.imwrite(outputDir + '/original_data.tif', data);
    data = pre.cropBar(data); 

    data = cv2.GaussianBlur(data, (5,5), 0);
    data = cv2.Canny(data, 150, 300);

    cv2.imwrite(outputDir + '/preprocessed.tif', data);

    end = time.time();
    print("Done (time (s) : " + str(end-start) + ")");
   


if __name__ == '__main__':
  main();
  print"";

