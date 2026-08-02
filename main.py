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
        
