import os
import subprocess
import sys

MODE_PACKAGE = False
MODE_LOAD = False
MODE_CONFIG = False
ARG_FAIL = -1

def main():
    if (parse_args() == ARG_FAIL):
        show_usage()
        quit()
    
    if MODE_PACKAGE is True:
        package





def parse_args():
    global MODE_PACKAGE ; global MODE_LOAD

    # Check for config settings
    USER_HOME = 'home/' + os.getenv('USER') + '/'
    if not os.path.isdir(USER_HOME + '.config/i3packager'):
        os.mkdir(USER_HOME + '.config/i3packager')
        MODE_CONFIG = True
        print('[+] Configuration files not found... entering config mode')
        return



    if sys.argv > 1:
        for arg in sys.argv:
            if arg.find("p") != -1:
                MODE_PACKAGE = True
                return
            elif arg.find("l") != -1:
                MODE_PACKAGE = True
                return
            elif arg.find("c") != -1:
                MODE_CONFIG = True
                return
            else
                return ARG_FAIL 

    return ARG_FAIL

def show_usage():
    usage = '''
    
    * * * * * * * * * * * * *  i3-Gaps Theme Packaging Script * * * * * * * * * 

        usage: python i3-package.py [ -l (load) / -p (package) / -c (config) ] 

            For first use, run with arg -c to configure theme directories
'''
    print(usage)
        
    





