
# Script to make tutorial image
import linecache 
import random

# Image Libraries
from PIL import Image
from PIL import ImageDraw

infoFileName = "Information.txt"  
splashTemplate = "Reaper Splash.png"
editedSplashName = "Splash.png"
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
Tip = linecache.getline(infoFileName, SelectedLine)
print(Tip)

### Image Gen

# Open Splash Template
img = Image.open(splashTemplate)
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
 
# Add Text to an image
I1.text((28, 36), Tip, fill=(255, 0, 0))
 
# Display edited image
img.show()
 
# Save the edited image
img.save(editedSplashName)