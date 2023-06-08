# Enter in folder location and regex to be searched.
# Program will print out the file path and text in file.
import glob
import re

def regexSearch (folderLocation, searchRegex):
    txtFiles = glob.glob(folderLocation + '/*.txt')
    for file in txtFiles:
        fileToSearch = open(file).read()
        if searchRegex.search(fileToSearch):
            print(file)
            print(fileToSearch)
        
    
    
regexSearch('folderlocation', re.compile(r'regex'))