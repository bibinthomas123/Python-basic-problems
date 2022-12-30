import json
import os

# goes to all the directories in the rootDirs[] and then displays the content 
#and then stores the data in the object :{
#                                      image:"nameOfTheFile",
#                                      tag:"name of the dir"
#                                        }

# Set the array of directories you want to loop through
rootDirs = ['brand', 'digital', 'event','exhibition','outdoor','pop','photography']
images = []
data = {}
objects = []
count=0
# Loop through the array of directories
for rootDir in rootDirs:
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        for fname in fileList:
           print('\t%s' % fname)
           with open(os.path.join(dirName, fname), 'r') as f:
                # Add the data from the file to the JSON object
                    images.append(fname)
                    obj = {"image":fname , "tag": dirName}
                    objects.append(obj)

    print(objects)



# # Write the JSON object to a file
with open('data.json', 'w+') as f:
    json.dump(objects, f)


# shuffling the data in the data.json


import random
import json

# Read the array from the file
with open('data.json', 'r') as f:
    arr = json.load(f)

# Shuffle the array
random.shuffle(arr)

# Write the shuffled array back to the file
with open('array.json', 'w') as f:
    json.dump(arr, f)
