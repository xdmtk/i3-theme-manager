# i3-theme-manager
----

![](.idea/themes.gif)
_from various members of /r/unixporn_



`i3-theme-manager` is a simple script with an optional graphical interface to create loadable theme packages consisting of
the various components of your chosen theme. A package consists of: 
1. i3 configuation 
2. status bar configuation - ( `polybar` and `tint2` )
3. terminal emulator configuration - ( `terminator` )
4. vim configuartion
5. gtk themes/icons/cursors
6. bash configuaration + aliases
7. wallpaper configuartion - ( supports `pywal` )
8. compton configuartion

For certain theme components like wallpaper setters and terminal emulators, `i3-theme-manager` only supports selected programs,
but will eventually support more in the future. 

### Getting Started

`i3-theme-manager` looks for theme components based on where they are specified in the config file.
On first run, `i3-theme-manager` will generate a configuration file located at `~/.config/i3packager/` 
with descriptions of all supported configuration options. Uncomment each desired entry to enable them for packaging 
and loading themes.


### Dependencies 

Both the CLI tool and GUI component require Python 3.

For the GUI component of `i3-theme-manager` to work correctly, you will need to have `pyqt5`
which can be installed by:

`pip3 install pyqt5`

The screenshot feature of `i3-theme-manager` currently depends on `xfce4-screenshooter`, but 
will soon be implemented to use `scrot` instead.


### Installation

As long as dependencies are met, you can simply copy the files `i3-theme-manager` and `i3-theme-manager-qt` to
`~/bin` and execute them directly from the command line.


#### i3 Configuration File

Because i3 does not support sourcing parts of the config file from other files, in order for
`i3-theme-manager` to package only theme specific elements of the config file, you should edit your config file by inserting markers surrounding the theme specific portion:

`# i3 THEME SECTION START`

and 

`# i3 THEME SECTION END`

This will allow the script to save and deploy only parts of your configuration that are theme 
specific, allowing you to keep non theme essential settings intact when switching themes, or 
deploying themes to a seperate machine.






For supported theme component programs

**Status Bar** : `tint2` or `polybar`<br>
**Terminal Emulators** : `terminator`<br>
**Wallpaper Setters** : `nitrogen` , `pywal`, or `feh`<br>


### CLI Screenshots

![](http://imgur.com/ooh9OEgl.png)



### GUI Screenshots

![](http://i.imgur.com/ybD2Viy.png)

