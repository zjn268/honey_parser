Decided to build a small script to count how many times a specific user agent or something
of the like visits my honeypot. There is definitely easier ways to accomplish what this does, but
I haven't been able to find an excuse to use python in a while. So I thought this would be a good 
excuse. Dropped the code below too.

from fileInteraction import file_manipulation
from fileInteraction import read_files
from fileInteraction import gather_agents

Main.py

def main():

    

    user_dir = '/home/norwoodz/srv/log/'

    fileList = file_manipulation(user_dir).gather_files()

    fileContents = read_files(fileList).createContentsList()

    sortedUserAgents = gather_agents(fileContents).createSortedDict()

    libRedTailVisits = (len(sortedUserAgents['libredtail-http']))

    print(f" The libRedTail user agent visited {libRedTailVisits} times")



if __name__ == "__main__":
    print("""
        +-+-+-+-+-+-+-+-+-+-+-+-+
        |h|o|n|e|y|_|p|a|r|s|e|r|
        +-+-+-+-+-+-+-+-+-+-+-+-+

        """)                             
    main()

fileInteraction.py

from pathlib import Path #using pathlib due to personal preference 
import json

class file_manipulation:
    def __init__(self, directory):
        self.directory = directory

    
    def gather_files(self):

        directoryPath = Path(self.directory)
        
        try:  #function explicitly grabs json files from the directory I statically assigned in main
            
            if  directoryPath.is_dir():

                dirFiles = directoryPath.glob('*.json')
            
                files = sorted(dirFiles)
            
                listFiles = list(files)
            
                return listFiles  # returns the .json files as a list   
        
        except Exception as excepter:

            print(f'Its not working, try again {excepter}')



class read_files:
    def __init__(self, fileList):
        self.fileList = fileList

    def createContentsList(self):

        dictOfItems = {} # prepares a dictionary for my file contents
        entryCounter = 1 #makes the dictionary start at 1 and not 0 just personal preference

        for file in self.fileList: #grabs a file

            

            with file.open(mode='r', encoding='cp1252') as openFile: #opens it
                

                for line in openFile:

                    jsonObject = json.loads(line.strip())
            

                    dictOfItems[entryCounter] = jsonObject #drops each line in the dictionary from the file

                    entryCounter += 1 # loops back again on a new key
                
    

        
        return dictOfItems #returns a dictionary of dictionaries


class gather_agents:
    def __init__(self, fileContents):
        self.fileContents = fileContents

    def createSortedDict(self):

        sortedDictionary = {}
        entryPoint = 1

        dictLength = len(self.fileContents)
        

        
     
        for keyNumber in range(1, dictLength + 1):
            
            stringifiedLine = str(self.fileContents[keyNumber]['useragent'])

            # If we've already seen this agent before anywhere in the file
            if stringifiedLine in sortedDictionary:
                # Add it to its existing group list
                sortedDictionary[stringifiedLine].append(stringifiedLine)
            else:
                # First time seeing this agent: initialize a list with it
                sortedDictionary[stringifiedLine] = [stringifiedLine]
                entryPoint += 1



        return sortedDictionary
        
        


            
        
