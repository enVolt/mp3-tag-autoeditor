from os import name as os_name, system as os_system


def log(s):
    '''
    Make log of whatever you want for debugging
    '''
    f = open("log.txt", "a+")
    f.write(s+"\n")
    f.close()


def cls():
    ''' clears the terminal '''
    if os_name == 'nt':
        os_system("cls")
        return None
    os_system("clear")


def clearlog():
    '''
    Overwrite log.txt (empties)
    '''
    f = open("log.txt", "w+")
    f.close()
