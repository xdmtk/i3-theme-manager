import os
import subprocess
import sys

MODE_PACKAGE = False
MODE_LOAD = False
MODE_CONFIG = False
ARG_FAIL = -1

I3_VIS_CONFIG = None
BASH_PROMPT_CONFIG = None


def main():
    if (parse_args() == ARG_FAIL):
        show_usage()
        quit()
    
    if MODE_PACKAGE is True:
        package()
    elif MODE_CONFIG is True:
        (I3_VIS_CONFIG, BASH_PROMPT_CONFIG) = config()
    elif MODE_LOAD is True:
        load()


def config():

    i3_config = None ; bash_config = None
    # Need to verify seperate files for i3 theme/visual configs
    while True:
        subprocess.call(['clear'])a
        print("Enter full path for i3 visual config:\n>>>", end="")
        i3_config = input()
        if not os.path.isfile(i3_config):
            print("Invalid path")
        else:
            break

    # Need to verify seperate files for bash prompt/themes
    while True:
        subprocess.call(['clear'])a
        print("Enter full path for bash prompt config:\n>>>", end="")
        bash_config = input()
        if not os.path.isfile(i3_config):
            print("Invalid path")
        else:
            break

    return (i3_config, bash_config)









def parse_args():
    global MODE_PACKAGE ; global MODE_LOAD

    # Check for config settings
    USER_HOME = 'home/' + os.getenv('USER') + '/'
    if not os.path.isdir(USER_HOME + '.config/i3packager'):
        os.mkdir(USER_HOME + '.config/i3packager')
        MODE_CONFIG = True
        print('[+] Configuration files not found... entering config mode')
        return


    # Parse args ( only  one ) 
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
config
    return ARG_FAIL


def show_usage():
    usage = '''
    
    * * * * * * * * * * * * *  i3-Gaps Theme Packaging Script * * * * * * * * * 

        usage: python i3-package.py [ -l (load) / -p (package) / -c (config) ] 

            For first use, run with arg -c to configure theme directories
'''
    print(usage)
        
    





