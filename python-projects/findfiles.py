# Author: dropnfly23

import fnmatch
import os
rootPath = '/'
pattern = 'saved_img.jpg'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
       print( os.path.join(root, filename))
