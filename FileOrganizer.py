#!/usr/bin/python
import os

currentDirectory = os.getcwd()

for subdir, dirs, files in os.walk (currentDirectory):
    for file in files:
        if os.path.isfile (file):
            # If file is THIS file, skip
            if os.path.basename (__file__) != file:
                # Ignore hidden files
                if not file.startswith ('.'):
                    # Get only text from file extension and capitalize
                    extension = os.path.splitext (file)[1].replace ('.', '').upper()
                    # Check to make sure file has an exension
                    if (len (os.path.splitext (file)[1])) <= 0:
                        extension = "MISC"
                    if not os.path.exists (extension):
                        os.mkdir (extension)
                        os.rename (os.path.join (currentDirectory, file),
                                   os.path.join (currentDirectory, extension, file))
