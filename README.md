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
        
