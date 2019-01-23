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
        'terminal_config_file' : '',
        'i3_config_file' : '',
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
    subprocess.call(['cp', config_arg_list['bash_visual_file'], 'bash/'])
    subprocess.call(['cp', config_arg_list['bash_aliases_file'], 'bash/'])
    print("[+] Copying: " + config_arg_list['bash_visual_file'])
    print("[+] Copying: " + config_arg_list['bash_aliases_file'])

    # Package vimrc
    os.mkdir('vim')
    subprocess.call(['cp', config_arg_list['vimrc_file'], 'vim/'])
    print("[+] Copying: " + config_arg_list['vimrc_file'])

    # Packaging nitrogen requires special handling of wallpaper files
    package_nitrogen()

    # Package terminator
    package_terminator()


    # Package I3 
    package_i3()
    
    # Package GTK 
    package_gtk()

    # Package Tint2/Polybar
    bar_prog = config_arg_list['bar_prog']
    if bar_prog == "polybar":
        subprocess.call(['cp', '-R', config_arg_list['polybar_dir'], '.'])
    elif bar_prog == "tint2":
        subprocess.call(['cp', '-R', config_arg_list['tint2_dir'], '.'])


def package_gtk():
   
    os.mkdir('gtk')
    os.mkdir('gtk/themes')

    gtk_dir = config_arg_list['gtk_dir']
    gtk_settings_file = gtk_dir + '/settings.ini'
    gtk_theme = None ; gtk_icons = None ; gtk_cursor = None
    
    subprocess.call(['cp',  gtk_settings_file , 'gtk/'])
    subprocess.call(['cp', gtk_dir + '/gtk.css', 'gtk/'])

    # Get theme info from settings file
    with open(gtk_settings_file, 'r') as config:
        for line in f:
            if line.find("gtk-theme-name") != -1:
                gtk_theme = line.split("=")[1]
            elif line.find("gtk-icon-theme-name") != -1:
                gtk_icons = line.split("=")[1]
            elif line.find("gtk-cursor-theme-name") != -1:
                gtk_cursors = line.split("=")[1]
   
    get_gtk_assets(gtk_theme)
    get_gtk_assets(gtk_icons)
    get_gtk_assets(gtk_cursors)


def get_gtk_assets(gtk_asset):
    # Attempt to locate themes referenced in settings.ini
    themes_dir = config_arg_list['themes_dir']
    sys_themes_dir = '/usr/share/themes'
    dir_loc = None

    if os.path.isdir(themes_dir + '/' + gtk_asset):
        dir_loc = themes_dir + '/'+ gtk_asset
    elif os.path.isdir(sys_themes_dir + '/' + gtk_asset):
        dir_loc = sys_themes_dir + '/' + gtk_asset 
    else:
        # If can't find theme directory, prompt user until valid location is found
        while True:
            print("[-] Couldn't locate directory for GKT theme: " + 
                    gtk_asset + ". Please enter location\n>>> ", end="")
            dir_loc = input()
            if os.path.isdir(dir_loc):
                break
    
    subprocess.call(['cp', '-R', dir_loc, 'gtk/themes'])
    print("[+] Recursively copying " + dir_loc)    
    



def package_nitrogen():

    # Package nitrogen
    os.mkdir('nitrogen')
    subprocess.call(['cp', '-R', config_arg_list['nitrogen_dir'] + '/*', 'nitrogen/'])
   
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
            subprocess.call(['cp', wallpaper_path, 'nitrogen/wallpapers'])

   

# Terminator package function to get config + compile font list
def package_terminator():

    font_list = [] 

    term_dir = config_arg_list['terminal_prog']
    os.mkdir(term_dir)

    subprocess.call(['cp', config_arg_list['terminal_config_file'], config_arg_list['terminal_prog']])
    print("[+] Copying: " + config_arg_list['terminal_config_file'])
    
    with open(term_dir + '/' + config_arg_list['terminal_config_file'], 'r') as config:
        for line in config:
            if line.find('font'):
                font_list.append(line.split('=')[1])

    
    subprocess.call(['touch', term_dir + '/font_list'])
    with open(term_dir + '/font_list', 'w') as fl:
        for font in font_list:
            fl.write(font + '\n')

        
# Workaround for i3 lack of include/source directives
def package_i3():

    os.mkdir('i3')
    i3_theme_section = [] ; theme_section_set = False
    i3_config = config_arg_list['i3_config_file']

    with open(i3_config, 'r') as config:
        for line in config:
            if line.find('i3 THEME SECTION START') != -1:
                theme_section_set = True
            elif line.find('i3 THEME SECTION END') != -1:
                theme_section_set = False
            if theme_section_set is True:
                i3_theme_section.append(line)
    
    subprocess.call(['touch', 'i3/i3_theme_sec'])
    with open('i3/i3_theme_sec', 'w') as config:
        for line in i3_theme_section:
            config.write(line)

                









    


    
def load():
    quit()



main()
