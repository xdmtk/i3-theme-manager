import subprocess
import random
import os


colorScheme = random.choice(os.listdir("/home/nmartinez/.vim/colors/"))
ar = colorScheme.split(".")
colorSet = ar[0]


vimRc = '''



set number
set tabstop=4
set shiftwidth=4
set foldmethod=indent
syntax on

set foldcolumn=4
set mouse=v
set foldlevel=3

set showmatch
set ignorecase
set autowrite
set smartindent
set smarttab
set autoindent


colorscheme'''
vimRc = vimRc + " " + colorSet + "\n"

vimrcfile = open("/home/nmartinez/.vimrc", "w" )
vimrcfile.write(vimRc)
