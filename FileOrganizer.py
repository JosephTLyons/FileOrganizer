#!/usr/bin/python
import os
import sys

if (len (sys.argv) <= 1):
    currentDirectory = os.getcwd()

else:
    currentDirectory = sys.argv[1]

if not os.path.exists (currentDirectory):
    print ("Path specified does not exist.")

else:
    print ("\n")

    for subdir, dirs, files in os.walk (currentDirectory):
        for file in files:
            pathToFile = os.path.join (currentDirectory, file)

            if os.path.isfile (pathToFile):
                # If file is THIS file, skip
                if os.path.basename (__file__) != file:
                    # Ignore hidden files
                    if not file.startswith ('.'):
                        # Get only text from file extension and capitalize
                        extension = os.path.splitext (file)[1].replace ('.', '')
                        # Check to make sure file has an exension (if not, its an empty string)
                        if (len (extension) <= 0):
                            extension = "MISC"

                        pathToNewDirectory = os.path.join (currentDirectory, extension)

                        if not os.path.exists (pathToNewDirectory):
                            os.mkdir (pathToNewDirectory)

                        os.rename (pathToFile, os.path.join (pathToNewDirectory, file))

                        print (file + " -> " + os.path.join (extension, file))
