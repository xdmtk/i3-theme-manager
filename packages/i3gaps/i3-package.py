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
I3P_DIR = None
I3P_CONF = None

DEBUG = 1

config_arg_list = {
        'bar_prog' : '',
        'terminal_prog' : '',
        'i3_visual_config' : '',
        'bash_visual_config' : '',
        'nitrogen_dir' : '',
        'tint2_dir' : '',
        'polybar_dir' : '',
        'gtk_dir' : '',
        'themes_dir' : ''
}


def main():
    check_config()
    if (parse_args() == ARG_FAIL):
        show_usage()
        quit()
    
    parse_config()
    
    if MODE_PACKAGE is True:
        package()
    elif MODE_LOAD is True:
        load()


def parse_config():
    with open(I3P_CONF, "r") as config:
        for line in config:
            config_arg_list[line.split('=')[0]] = line.split('=')[1]
    if DEBUG:
        print(config_arg_list)


def parse_args():
    global MODE_PACKAGE ; global MODE_LOAD ; global USER_HOME
    
    # Parse args ( only  one ) 
    if len(sys.argv) > 1:
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
        

def write_blank_config():
    with open(I3P_CONF , 'w') as config:
        for arg in config_arg_list:
            config.write(arg + '=' + '\n')
        
    
def check_config():
    global USER_HOME ; global I3P_DIR ; global I3P_CONF 
    
    # Check for config settings
    USER_HOME = '/home/' + os.getenv('USER') + '/'
    I3P_DIR = USER_HOME + '.config/i3packager'
    I3P_CONF = I3P_DIR + '/config'

    if not os.path.isdir(I3P_DIR):
        os.mkdir(I3P_DIR)
        print('[+] Configuration file not found... creating blank configuration file ' 
                + 'at ~/.config/i3packager')
        
        subprocess.call(['touch', I3P_CONF])
        write_blank_config()
        quit()

def package():
    quit()

    
def load():
    quit()




main()
