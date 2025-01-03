
# Script to make tutorial image
import linecache 
import random
import textwrap

# Image Libraries
from PIL import Image, ImageDraw, ImageFont

infoFileName = "Information.txt"  
splashTemplateName = "Reaper Splash.png"
editedSplashName = "Splash.png"

MarginWidth = 40

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
tutorialMessage = linecache.getline(infoFileName, SelectedLine)
print(tutorialMessage)

### Image Gen
# Open Splash Template, get its size
img = Image.open(splashTemplateName)

# Get the size
imgWidth, imgHeight = img.size 

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
# Add Text to an image

I1.text((imgWidth/10, imgHeight-imgHeight/10), tutorialMessage, fill=(255, 255 , 255), align = "center")
 
# Display edited image
img.show()
 
# Save the edited image
img.save(editedSplashName)
