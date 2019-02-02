# i3-theme-manager
----
![](http://i66.tinypic.com/11rvct3.gif)

`i3-theme-manager` is a simple script with an optional graphical interface to create loadable theme packages consisting
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


### Dependencies 

Both the CLI tool and GUI component require Python 3.

For the GUI component of `i3-theme-manager` to work correctly, you will need to have `pyqt5`
which can be installed by:

    `pip3 install pyqt5`


![](http://i.imgur.com/5xOYo9X.png)


For supported theme component programs
    
    **Status Bar** : `tint2` or `polybar`
    **Terminal Emulators** : `terminator`
    **Wallpaper Setters** : `nitrogen`

