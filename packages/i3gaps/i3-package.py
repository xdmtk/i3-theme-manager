import os
import subprocess
import sys

MODE_PACKAGE = False
MODE_LOAD = False
ARG_FAIL = -1

def main():
    if (parse_args() == ARG_FAIL):
        show_usage()




def parse_args():
    global MODE_PACKAGE ; global MODE_LOAD
    if sys.argv > 1:
        for arg in sys.argv:
            if arg.find("p") != -1:
                MODE_PACKAGE = True
                return
            elif arg.find("l") != -1:
                MODE_PACKAGE = True
                return
            else
                return ARG_FAIL 


