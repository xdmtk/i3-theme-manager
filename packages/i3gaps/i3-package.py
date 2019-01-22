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
    i3_config = None ; bash_config = None ; gtk_config = None
    bar_config = None ; term_config = None ; wallpaper_config = None

def write_blank_config():
    config_arg_list = [
            'bar_prog',
            'terminal_prog',
            'i3_visual_config',
            'bash_visual_config',
            'nitrogen_dir',
            'tint2_dir',
            'polybar_dir',
            'gtk_dir',
            'themes_dir'
    ]
    with open(USER_HOME + '.config/i3packager/config', 'w') as config:
        for arg in config_arg_list:
            config.write(arg + '=' + '\n')
        



def parse_args():
    global MODE_PACKAGE ; global MODE_LOAD ; global USER_HOME

    # Check for config settings
    USER_HOME = '/home/' + os.getenv('USER') + '/'
    if not os.path.isdir(USER_HOME + '.config/i3packager'):
        os.mkdir(USER_HOME + '.config/i3packager')
        print('[+] Configuration file not found... creating blank configuration file ' 
                + 'at ~/.config/i3packager')
        subprocess.call(['touch', USER_HOME + '.config/i3packager/config'])
        write_blank_config()
        quit()



    # Parse args ( only  one ) 
    if sys.argv > 1:
        for arg in sys.argv:
            if arg.find("p") != -1:
                MODE_PACKAGE = True
                return
            elif arg.find("l") != -1:
                MODE_PACKAGE = True
                return
            else:
                return ARG_FAIL 
    return ARG_FAIL


def show_usage():
    usage = '''
    
    * * * * * * * * * * * * *  i3-Gaps Theme Packaging Script * * * * * * * * * 

        usage: python i3-package.py [ -l (load) / -p (package) ] 

            Edit config file at ~/.config/i3packager/config to specify theme components

'''
    print(usage)
        
    




main()
