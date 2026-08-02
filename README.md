Decided to build a small script to count how many times a specific user agent or something
of the like visits my honeypot. There is definitely easier ways to accomplish what this does, but
I haven't been able to find an excuse to use python in a while. So I thought this would be a good 
excuse. Dropped the code below too.



# **Main.py**


```
from fileInteraction import file_manipulation
from fileInteraction import read_files
from fileInteraction import gather_agents









def main():

    

    user_dir = '/home/norwoodz/srv/log/'

    fileList = file_manipulation(user_dir).gather_files()

    fileContents = read_files(fileList).createContentsList()

    sortedUserAgents = gather_agents(fileContents, None, 'useragent', None).createSortedDict()

    libRedTailVisits = (len(sortedUserAgents['libredtail-http']))

    print(f" The libRedTail user agent visited {libRedTailVisits} times")

    libRedTailIPs = gather_agents(None, fileContents,  None, None).gatherIPs()

    totalIPS = len(libRedTailIPs)

    print(f" The libRedTail user agent used {totalIPS} IP addresses")

    for ip in libRedTailIPs.keys():

        print(ip)



if __name__ == "__main__":
    print("""
        +-+-+-+-+-+-+-+-+-+-+-+-+
        |h|o|n|e|y|_|p|a|r|s|e|r|
        +-+-+-+-+-+-+-+-+-+-+-+-+

        """)                             
    main()
```


# **fileInteraction.py**



```
from pathlib import Path #using pathlib due to personal preference 
import json

class file_manipulation:
    def __init__(self, directory,):
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

            # Fixed: changed encoding to 'utf-8' to prevent decoding failures
            with file.open(mode='r', encoding='utf-8') as openFile: #opens it
                

                for line in openFile:

                    jsonObject = json.loads(line.strip())
            

                    dictOfItems[entryCounter] = jsonObject #drops each line in the dictionary from the file

                    entryCounter += 1 # loops back again on a new key
                
    

        
        return dictOfItems #returns a dictionary of dictionaries


class gather_agents:
    def __init__(self, fileContents, dictOfJSON, key, dictKey):
        self.fileContents = fileContents
        self.dictOfJSON = dictOfJSON
        self.key = key
        self.dictKey = dictKey


    def createSortedDict(self):

        sortedDictionary = {}

        if self.dictKey:
            dictLength = self.dictKey
            entryPoint = self.dictKey

        else:
            dictLength = len(self.fileContents)
            entryPoint = 1


        
     
        for keyNumber in range(1, dictLength + 1):
            
            stringifiedLine = str(self.fileContents[keyNumber][self.key])

            # If we've already seen this agent before anywhere in the file
            if stringifiedLine in sortedDictionary:
                # Fixed: append keyNumber/reference tracker instead of appending the literal string repeatedly
                sortedDictionary[stringifiedLine].append(keyNumber)
            else:
                # First time seeing this agent: initialize a list with the keyNumber tracker
                sortedDictionary[stringifiedLine] = [keyNumber]
                entryPoint += 1



        return sortedDictionary

    def gatherIPs(self):

        ipsGathered = {}
        
        # Loop through your dictionary of records
        for dictKey in range(1, len(self.dictOfJSON) + 1):
            
            # Check if the useragent matches
            if self.dictOfJSON[dictKey].get('useragent') == 'libredtail-http':
                
                
                ip = self.dictOfJSON[dictKey].get('sip')
                
                if ip:
                    if ip in ipsGathered:
                        ipsGathered[ip].append(dictKey)
                    else:
                        ipsGathered[ip] = [ip]
                    
        return ipsGathered
```
        
        


            
        
