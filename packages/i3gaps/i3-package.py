import os
import subprocess
import sys
import curses
import signal
import pdb

MODE_PACKAGE = False
MODE_LOAD = False
MODE_CONFIG = False
ARG_FAIL = -1

USER_HOME = None
I3_VIS_CONFIG = None
BASH_PROMPT_CONFIG = None


def main():

    if (parse_args() == ARG_FAIL):
        show_usage()
        quit()
    
    if MODE_PACKAGE is True:
        package()
    elif MODE_CONFIG is True:
        config()
    elif MODE_LOAD is True:
        load()


def config():

    #pdb.set_trace()
    #os.mkdir(USER_HOME + '.config/i3packager')
    # Curses init
    

    i3_config = None ; bash_config = None ; gtk_config = None
    bar_config = None ; term_config = None ; wallpaper_config = None

    # Need to verify seperate files for i3 theme/visual configs
    while True:
        print("Enter full path for i3 visual config:\n>>>", end="")
        
        i3_config = input()
        if not os.path.isfile(i3_config):
            print("Invalid path")
            
        else:
            break

    # Need to verify seperate files for bash prompt/themes
    while True:
        print("Enter full path for bash prompt config:\n>>>", end="")
        
        bash_config = input()
        if not os.path.isfile(bash_config):
            print("Invalid path")
            
        else:
            break

   
    # Find GTK settings
    print("Searching for gtk config files.")
    if os.path.isdir(USER_HOME + '.config/gtk-3.0'):
        print("Found GTK-3.0 settings in config folder")
        gtk_config = (USER_HOME + '.config/gtk-3.0')
        
    else:
        print("Unable to locate GTK-3.0 settings.. please enter" +
                " full path for GTK-3.0 folder:\n>>>", end="")
        

    while True:
        gtk_config = input()
        if not os.path.isdir(gtk_config):
            print("Invalid path")
            
        else:
            break

    
    # Verify terminal program ( For now, default to Termiantor )
    print("Please specify default terminal:")
    print(" >> Terminator ")
    
    term_prog = "terminator"

    if os.path.isdir(USER_HOME + '.config/' + term_prog):
        print("Found " + term_prog + "  settings in config folder")
        term_config = (USER_HOME + '.config/' + term_prog)
    else:
        print("Unable to locate " + term_prog + 
                " settings.. please enter full path for " + term_prog + " folder" + 
                "\n>>>", end="")

    
    while True:
        term_config = input()
        if not os.path.isdir(term_config):
            print("Invalid path")
        else:
            break







    










def parse_args():
    global MODE_PACKAGE ; global MODE_LOAD ; global MODE_CONFIG 
    global USER_HOME

    # Check for config settings
    USER_HOME = 'home/' + os.getenv('USER') + '/'
    if not os.path.isdir(USER_HOME + '.config/i3packager'):
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
            else:
                return ARG_FAIL 
    return ARG_FAIL


def show_usage():
    usage = '''
    
    * * * * * * * * * * * * *  i3-Gaps Theme Packaging Script * * * * * * * * * 

        usage: python i3-package.py [ -l (load) / -p (package) / -c (config) ] 

            For first use, run with arg -c to configure theme directories
'''
    print(usage)
        
    




main()
