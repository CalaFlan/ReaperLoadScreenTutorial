

# Script to make tutorial image

import linecache 
import random

infoFileName = "Information.txt"  

# on script start 
# open file and get a random line
# open the splash image template
# print the selected line on an image using the right format
# save the image to the location of the splash image

# Get number of lines
with open(infoFileName, 'r') as fp:
    for numOfLines, line in enumerate(fp):
        pass

    # Chose a random Line
print(numOfLines+1)
SelectedLine = random.randint(0, numOfLines+1)

# Print a random Line
print(linecache.getline(infoFileName, SelectedLine))