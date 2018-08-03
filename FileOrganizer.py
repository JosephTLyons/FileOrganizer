#!/usr/bin/python
import os

rootDir = "/Users/josephlyons/Desktop/test"

for subdir, dirs, files in os.walk (rootDir):
    for file in files:
        # Will need to change back to "if os.path.isfile (file):" after completion
        if os.path.isfile (os.path.join (subdir, file)):
            # If file is THIS file, skip
            if ("FileOrganizer.py" != file):
                print ("doggy")

                # if this is a hidden file, skip

                # else
                    #print (file)
                    # Delete line above
                    # Make directory based on files extension: example .txt -> TXT
                    # Move file

# TODO: Delete comments and remove the absolute file path to just relative
# TODO: Add rules to README and update README to mention that this is like my Script version, but in Python
        # Doesn't move this file, doesn't change already in place directories, doesn't move files in those directories
        # Doesn't move hidden files,
