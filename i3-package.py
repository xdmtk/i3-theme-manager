import time
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
NO_ARG = -1

USER_HOME = None
I3P_DIR = None
I3P_CONF = None
PACKAGE_NAME = ""
BASE_DIR = None
PACKAGE_DIR = None

DEBUG = 0

config_arg_list = {
        'bar_prog' : '',
        'terminal_prog' : '',
        'screenshot_prog' : '',
        'terminal_config_file' : '',
        'i3_config_file' : '',
        'bash_visual_file' : '',
        'bash_aliases_file' : '',
        'vimrc_file' : '',
        'nitrogen_dir' : '',
        'tint2_dir' : '',
        'polybar_dir' : '',
        'gtk_dir' : '',
        'themes_dir' : '',
        'icons_dir' : ''
}


def main():
    #pdb.set_trace()
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
            conf_arg = line.split('=')[1].replace('\n','') 
            conf_arg_name = line.split('=')[0]

            # Expand tilda
            conf_arg = conf_arg.replace('~', USER_HOME).replace('\n','')

            if len(conf_arg) != 0:
                if conf_arg.find('none') != -1:
                    config_arg_list[conf_arg_name] = NO_ARG 
                    continue
                # For program names, verify existence 
                elif conf_arg_name.find('prog') != -1:
                    if len(subprocess.check_output(['which', conf_arg])) != 0:
                        config_arg_list[conf_arg_name] = conf_arg
                        continue
                    else:
                        print("[-] Couldn't find program '" + conf_arg + "'")
                        config_arg_list[conf_arg_name] = NO_ARG
                        continue 


                # Make sure path is valid
                if not os.path.exists(conf_arg):
                    FAIL_FLAG = True
                    print("[-] Path '" + conf_arg + "' doesn't exist")
                    continue

                config_arg_list[conf_arg_name] = conf_arg
            else:
                # For empty args, show error and set failure flag
                print('[-] Missing parameter for ' + conf_arg_name)
                FAIL_FLAG = True
    
    
    if DEBUG:
        print(config_arg_list)
    if FAIL_FLAG is True:
        # Do not continue on fail flag
        quit()


def parse_args():
    global MODE_PACKAGE ; global MODE_LOAD ; global USER_HOME
    global PACKAGE_NAME  
    
    # Parse args ( only  one ) 
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode != "load" and mode != "package":
            print("[-] Invalid mode '" + mode + "' supplied")
            return ARG_FAIL
        else:
            if mode == "load":
                MODE_LOAD = True
            elif mode == "package":
                MODE_PACKAGE = True
        x = 1
        for x in range(1,len(sys.argv)):
            # Optional CLI package name specification
            if sys.argv[x].find("-o") != -1:
                PACKAGE_NAME = sys.argv[x+1]
                x += 1
                continue
        return
    else:
        return ARG_FAIL

                





def show_usage():
    usage = '''
    
    * * * * * * * * * * * * *  i3-Gaps Theme Packaging Script * * * * * * * * * 

        usage: python i3-package.py [ MODE ] [ OPTIONS ]
            
            Modes:
                load - Load and apply specified theme package
                package - Package current theme setup


            Options:
                -o [ PACKAGE NAME ] - Specify package name in argument over interactive stdin 


            First time use:
                i3-theme-manager will generate an empty config file in the standard user config directory,
                edit this file to specify directories for various theme components

'''
    print(usage)
        

def write_blank_config():

    print("Generating empty config file")
    with open(I3P_CONF , 'w') as config:
        # Write arg list into config file
        for arg in config_arg_list:
            config.write(arg + '=' + '\n')
        
    
def check_config():
    global USER_HOME ; global I3P_DIR ; global I3P_CONF 
    
    # Check for config settings
    USER_HOME = '/home/' + os.getenv('USER')
    I3P_DIR = USER_HOME + '/.config/i3packager/'
    I3P_CONF = I3P_DIR + 'config'

    if not os.path.isdir(I3P_DIR):
        print("[-] Configuration directory not found... creating config directory" 
                + "at '" + USER_HOME + "/.config/i3packager'" )
        os.mkdir(I3P_DIR)
        
    if not os.path.isfile(I3P_CONF):
        print("[-] Configuration file not found... creating config file" 
                + " at '" + USER_HOME + "/.config/i3packager/config'" )
        subprocess.call(['touch', I3P_CONF])
        write_blank_config()
        quit()

def package():
    
    global PACKAGE_NAME ; global PACKAGE_DIR ; global BASE_DIR
    BASE_DIR = str(subprocess.check_output(['pwd']))[2:-3]
    # Create tmp dir for package name
    if PACKAGE_NAME == "":
        print("Enter package name:\n>>>", end="")
        PACKAGE_NAME = input()

    take_screenshot()
    quit()
    PACKAGE_DIR = I3P_DIR + PACKAGE_NAME
    os.mkdir(PACKAGE_DIR)
    
    # CD to package directory
    os.chdir(PACKAGE_DIR)
   
    # Package bash files
    package_bash() 

    # Package vimrc
    package_vim()

    # Packaging nitrogen requires special handling of wallpaper files
    package_nitrogen()

    # Package terminator
    package_terminator()

    # Package I3 
    package_i3()
    
    # Package GTK 
    package_gtk()

    # Package Tint2/Polybar
    package_bar()
   


    print("\n\n[+] Successfully created package file at '" + package_dir)

def i3_msg(mode, args=False, t=0.1):
    if args is not False:
        subprocess.call(['i3-msg', mode, args])
        time.sleep(t)
        return
    subprocess.call(['i3-msg', mode])
    time.sleep(t)
    

def setup_workspace():
    
    pipe_arg = term_prog + ' -e "' + BASE_DIR + '/visual-scripts/pipes.sh ' + ' -t '
    i3_msg('workspace', '666')
    i3_msg('split', 'horizontal')
    i3_msg('exec', pipe_arg + ' 1"', .5)
    i3_msg('exec', pipe_arg + ' 3"', .5)
    i3_msg('split', 'vertical')
    i3_msg('exec', pipe_arg + ' 5"', .5)
    i3_msg('focus', 'left')
    i3_msg('split', 'vertical')
    i3_msg('exec', pipe_arg + ' 7"', .5)




def take_screenshot():
   
    
    # Jump to empty workspace and open some visual programs
    if len(subprocess.check_output(['which', 'i3-msg'])) == 0:
        print("[-] Screenshot requires i3-msg... how do you not have this?")
        return
    term_prog = config_arg_list['terminal_prog']
    os.chdir(BASE_DIR)

    setup_workspace()

    quit() 
    screenshot_prog = config_arg_list['screenshot_prog']
    
    # For now, only include logic/args for xfce4-screenshooter, maybe expand later..
    if screenshot_prog == "xfce4-screenshooter":
        tmp_ss_loc = subprocess.check_output([screenshot_prog, '-fo', 'ls'])
        subprocess.call(['mv', tmp_ss_loc, PACKAGE_DIR])






def package_bar():
    bar_prog = config_arg_list['bar_prog']
    if bar_prog == "polybar":
        subprocess.call(['cp', '-R', config_arg_list['polybar_dir'], '.'])
    elif bar_prog == "tint2":
        subprocess.call(['cp', '-R', config_arg_list['tint2_dir'], '.'])
    else:
        print("[-] Invalid bar program: " + bar_prog + " ..skipping")


def package_vim():


    print("\n[+] VIM files\n * * * * * * * * * * * * *")

    os.mkdir('vim')
    subprocess.call(['cp', config_arg_list['vimrc_file'], 'vim/'])
    print("[+] Copying: " + config_arg_list['vimrc_file'])



def package_bash():
    
    print("\n[+] Bash files\n * * * * * * * * * * * * *")

    os.mkdir('bash')
    subprocess.call(['cp', config_arg_list['bash_visual_file'], 'bash/'])
    subprocess.call(['cp', config_arg_list['bash_aliases_file'], 'bash/'])
    print("[+] Copying: " + config_arg_list['bash_visual_file'])
    print("[+] Copying: " + config_arg_list['bash_aliases_file'])


def package_gtk():
   
    print("\n[+] GTK files\n * * * * * * * * * * * * *")
    
    os.mkdir('gtk')
    os.mkdir('gtk/themes')

    gtk_dir = config_arg_list['gtk_dir']
    gtk_settings_file = gtk_dir + '/settings.ini'
    gtk_theme = None ; gtk_icons = None ; gtk_cursor = None
    
    subprocess.call(['cp',  gtk_settings_file , 'gtk/'])
    subprocess.call(['cp', gtk_dir + '/gtk.css', 'gtk/'])

    # Get theme info from settings file
    with open(gtk_settings_file, 'r') as config:
        for line in config:
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
    gtk_asset = gtk_asset.replace('\n','')
    # Attempt to locate themes referenced in settings.ini
    gtk_asset = gtk_asset.replace('\n','')
     
    themes_dir = config_arg_list['themes_dir']
    icons_dir = config_arg_list['icons_dir']

    sys_themes_dir = '/usr/share/themes'
    sys_icons_dir = '/usr/share/icons'
    dir_loc = None
    
    if os.path.isdir(themes_dir + '/' + gtk_asset):
        dir_loc = themes_dir + '/'+ gtk_asset
    elif os.path.isdir(sys_themes_dir + '/' + gtk_asset):
        dir_loc = sys_themes_dir + '/' + gtk_asset 
    elif os.path.isdir(sys_icons_dir + '/' + gtk_asset):
        dir_loc = sys_icons_dir + '/' + gtk_asset 
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
    print("\n[+] Nitrogen files\n * * * * * * * * * * * * *\n")


    os.mkdir('nitrogen')
    subprocess.call(['cp', '-R', config_arg_list['nitrogen_dir'], 'nitrogen/'])
   
    # Read bg-saved config to fetch wallpapers
    bg_saved_file = config_arg_list['nitrogen_dir']
    if bg_saved_file[len(bg_saved_file)-1] != '/':
        bg_saved_file += '/'
    bg_saved_file += 'bg-saved.cfg'
   
    # Copy wallpaper file into nitrogen package directory
    os.mkdir('nitrogen/wallpapers')
    with open(bg_saved_file, 'r') as config:
        for line in config:
            if line.find('file') !=  -1:
                wallpaper_path = line.split('=')[1].replace('\n','')
                print("[+] Copying:  " + wallpaper_path)
                subprocess.call(['cp', wallpaper_path, 'nitrogen/wallpapers'])

   

# Terminator package function to get config + compile font list
def package_terminator():

    print("\n[+] Terminator files\n * * * * * * * * * * * * *")

    font_list = [] 

    term_dir = config_arg_list['terminal_prog']
    os.mkdir(term_dir)

    subprocess.call(['cp', config_arg_list['terminal_config_file'], config_arg_list['terminal_prog']])
    print("[+] Copying: " + config_arg_list['terminal_config_file'])
    
    with open(config_arg_list['terminal_config_file'], 'r') as config:
        for line in config:
            if line.find('font') != -1:
                try: 
                    font_list.append(line.split('=')[1])
                except:
                    pdb.set_trace()

    
    subprocess.call(['touch', term_dir + '/font_list'])
    with open(term_dir + '/font_list', 'w') as fl:
        for font in font_list:
            fl.write(font + '\n')

        
# Workaround for i3 lack of include/source directives
def package_i3():

    print("\n[+] i3 files\n * * * * * * * * * * * * *")

    os.mkdir('i3')
    i3_theme_section = [] ; theme_section_set = False ; extracted = False
    i3_config = config_arg_list['i3_config_file']

    with open(i3_config, 'r') as config:
        for line in config:
            if line.find('i3 THEME SECTION START') != -1:
                theme_section_set = True
                extracted = True
            elif line.find('i3 THEME SECTION END') != -1:
                theme_section_set = False
            if theme_section_set is True:
                i3_theme_section.append(line)
    if extracted is True: 
        print("[+] Extracting theme section from i3 config")
        
        subprocess.call(['touch', 'i3/i3_theme_sec'])
        print("[+] Writing to file `i3_theme_sec`")
        with open('i3/i3_theme_sec', 'w') as config:
            for line in i3_theme_section:
                config.write(line)
    else:
        print("[+] No theme section found in i3 config file")

                









    


    
def load():
    quit()



main()
