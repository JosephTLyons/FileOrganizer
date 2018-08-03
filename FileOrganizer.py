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
                    # Get just text from file extension and capitalize
                    extension = os.path.splitext (file)[1].replace ('.', '').upper()
                    if not os.path.exists (extension):
                        os.mkdir (extension)
                    os.rename (os.path.join (currentDirectory, file), os.path.join (currentDirectory, extension, file))

# TODO: Add rules to README and update README to mention that this is like my Script version, but in Python
        # Doesn't move this file, doesn't change already in place directories, doesn't move files in those directories
        # Doesn't move hidden files,
