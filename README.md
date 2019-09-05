# i3-theme-manager
----

![](src/themes.gif)
_from various members of /r/unixporn_




`i3-theme-manager` is a simple script with an optional graphical interface to create loadable theme packages consisting of various theme components. A package consists of: 
* `i3` configuration 
* status bar configuration - ( `polybar` and `tint2` )
* terminal emulator configuration - ( `terminator` )
* `vim` configuration 
* GTK themes/icons/cursors
* `bash` configuration + aliases
* wallpaper configuration - ( supports `pywal` )
* `compton` configuration

For certain theme components like wallpaper setters and terminal emulators, `i3-theme-manager` currently only supports selected programs, but will soon support more in the future. 

**NOTE**: This project is pretty dead ( and a bit bloated from my personal dotfile packages ), so I most likely won't be fixing bugs for a while ( and I'm sure they're present ), so if you find any, I would welcome and appreciate any pull requests. 


### Getting Started

`i3-theme-manager` looks for theme components based on where they are specified in the config file.
On first run, `i3-theme-manager` will generate a configuration file located at `~/.config/i3packager/` 
with descriptions of all supported configuration options. Uncomment each desired entry to enable them for packaging 
and loading themes.


### Dependencies 

On first run, `i3-theme-manager` will verify and optionally install all dependencies required for basic operation,
and in addition can also install all theme component programs supported + `polybar` and/or `pywal` if specified. 

The complete list of dependencies are:

`python3`
`xfce4-screenshooter`
`xdotool`
`feh`
`pip3`
`fc-list`
`pyqt5` (`pip3` package)



### Installation

As long as dependencies are met, you can simply copy the files `i3-theme-manager` and `i3-theme-manager-qt` to
`~/bin` and execute them directly from the command line.



### Configuration

##### i3 Configuration File

Because `i3` does not support sourcing parts of the config file from other files, in order for
`i3-theme-manager` to package only theme specific elements of the config file, you should edit your `i3` config file by inserting markers surrounding the theme specific portion:

`# i3 THEME SECTION START`

and 

`# i3 THEME SECTION END`

This will allow the script to save and deploy only parts of your configuration that are theme 
specific, allowing you to keep non theme essential settings intact when switching themes, or 
deploying themes to a separate machine.






For supported theme component programs

**Status Bar** : `tint2` or `polybar`<br>
**Terminal Emulators** : `terminator`<br>
**Wallpaper Setters** : `nitrogen` , `pywal`, or `feh`<br>


### CLI Screenshots

![](http://i.imgur.com/snDad48.png)



### GUI Screenshots

![](http://i67.tinypic.com/opdbmh.gif)


### Issues

`i3-theme-manager` is ~under active development~ a bit dead. For bugs and other concerns, please open an issue at https://github.com/xdmtk/i3-theme-manager/issues , though I may not get to them in a timely matter. 
