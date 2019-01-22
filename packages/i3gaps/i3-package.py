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
        'i3_visual_file' : '',
        'bash_visual_file' : '',
        'bash_aliases_file' : '',
        'nitrogen_dir' : '',
        'tint2_dir' : '',
        'polybar_dir' : '',
        'gtk_dir' : '',
        'themes_dir' : '',
        'vimrc_file' : ''
}


def main():
    # Check if config file exists
    check_config()
    if (parse_args() == ARG_FAIL):
        # Show usage if no valid args
        show_usage()
        quit()
   
    # Parse config files for theming directories
    parse_config()
    
    if MODE_PACKAGE is True:
        package()
    elif MODE_LOAD is True:
        load()


def parse_config():
    FAIL_FLAG = False
    with open(I3P_CONF, "r") as config:
        for line in config:
            # Load config args into dictionary `config_arg_list`
            if len(line.split('=')[1]) != 0:
                config_arg_list[line.split('=')[0]] = line.split('=')[1]
            else:
                # For empty args, show error and set failure flag
                print('Missing parameter for ' +  line.split('=')[1])
                FAIL_FLAG = True
    
    
    if DEBUG:
        print(config_arg_list)
    if FAIL_FLAG is True:
        # Do not continue on fail flag
        quit()


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
        # Write arg list into config file
        for arg in config_arg_list:
            config.write(arg + '=' + '\n')
        
    
def check_config():
    global USER_HOME ; global I3P_DIR ; global I3P_CONF 
    
    # Check for config settings
    USER_HOME = '/home/' + os.getenv('USER') + '/'
    I3P_DIR = USER_HOME + '.config/i3packager/'
    I3P_CONF = I3P_DIR + 'config'

    if not os.path.isdir(I3P_DIR):
        os.mkdir(I3P_DIR)
        print('[+] Configuration file not found... creating blank configuration file ' 
                + 'at ~/.config/i3packager')
        
    if not os.path.isfile(I3P_CONF):
        subprocess.call(['touch', I3P_CONF])
        write_blank_config()
    quit()

def package():

    # Create tmp dir for package name
    print("Enter package name:\n>>>", end="")
    package_name = input()
    package_dir = I3P_DIR + package_name
    os.mkdir(package_dir)
    
    # CD to package directory
    os.chdir(package_dir)
   
    # Package bash files
    os.mkdir('bash')
    subprocess.call(['cp', config_arg_list['bash_visual_file'], 'bash/']])
    subprocess.call(['cp', config_arg_list['bash_aliases_file'], 'bash/']])
    print("[+] Copying: " + config_arg_list['bash_visual_file'])
    print("[+] Copying: " + config_arg_list['bash_aliases_file'])

    # Package vimrc
    os.mkdir('vim')
    subprocess.call(['cp', config_arg_list['vimrc_file'], 'vim/']])
    print("[+] Copying: " + config_arg_list['vimrc_file'])

    # Packaging nitrogen requires special handling of wallpaper files
    package_nitrogen()








def package_nitrogen():

    # Package nitrogen
    os.mkdir('nitrogen')
    subprocess.call(['cp', '-R', config_arg_list['nitrogen_dir'] + '/*', 'nitrogen/']])
   
    # Read bg-saved config to fetch wallpapers
    bg_saved_file = config_arg_list['nitrogen_dir']
    if bg_saved_file[len(bg_saved_file)-1] != '/':
        bg_saved_file += '/'
    bg_saved_file += 'bg-saved.cfg'
   
    # Copy wallpaper file into nitrogen package directory
    os.mkdir('nitrogen/wallpapers')
    with open(bg_saved_file, 'r') as config:
        if line.find('file') !=  -1:
            wallpaper_path = line.split('=')[1]
            print("[+] Copying:  " + wallpaper_path)
            subprocess.call(['cp', wallpaper_path, 'nitrogen/wallpapers')

    







    


    
def load():
    quit()


``

main()
