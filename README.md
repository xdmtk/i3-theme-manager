# i3-theme-manager
----
![](https://i.ibb.co/hCbrR12/themes.gif)

`i3-theme-manager` is a simple script with an optional graphical interface to create loadable theme packages consisting of
the various components of your chosen theme. A package consists of: 
1. i3 configuation 
2. status bar configuation
3. terminal emulator configuration 
4. vim configuartion
5. gtk themes/icons/cursors
6. bash configuaration + aliases
7. wallpaper configuartion

For certain theme components like wallpaper setters and terminal emulators, `i3-theme-manager` only supports selected programs,
but will eventually support more in the future. 

### Getting Started

`i3-theme-manager` looks for theme components based on where they are specified in the config file.
On first use, run the CLI application before the GUI application. This will generate a blank
config file in the standard config directory `~/.config/i3packager`

#### i3 Configuration File

Because i3 does not supported sourcing parts of the config file from other files, in order for
`i3-theme-manager` to package only theme specific elements of the config file, you need to edit 
your configuration file by surrounding the theme specific portion of your config with the lines

`# i3 THEME SECTION START`

and 

`# i3 THEME SECTION END`

This will allow the script to save and deploy only parts of your configuration that are theme 
specific, allowing you to keep non theme essential settings intact when switching themes, or 
deploying themes to a seperate machine.



### Dependencies 

Both the CLI tool and GUI component require Python 3.

For the GUI component of `i3-theme-manager` to work correctly, you will need to have `pyqt5`
which can be installed by:

`pip3 install pyqt5`



For supported theme component programs

**Status Bar** : `tint2` or `polybar`<br>
**Terminal Emulators** : `terminator`<br>
**Wallpaper Setters** : `nitrogen`<br>


### CLI Screenshots

![](http://imgur.com/ooh9OEgl.png)



### GUI Screenshots

![](http://i.imgur.com/5xOYo9X.png)

