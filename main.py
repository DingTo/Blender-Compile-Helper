# ##### BEGIN GPL LICENSE BLOCK #####
#
# Copyright 2012, Thomas Dinges
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import os
from subprocess import Popen

# Compile Helper Includes
import svn
import tools
import scons

# Path to the code folders
root_path = "D:/blender_dev/code/"

# Available checkouts
source_tree = ("trunk", "soc-2011-tomato", "cycles", "tile", "render25", "asset-browser")

def print_list():
    nr = 1
    for elem in source_tree:
        print ("%s: %s" % (nr, elem))
        nr += 1
    br_in = int(input("Tree: "))
    return (source_tree[br_in-1])

def sub_call(tree, path):
    os.system("title %s" % tree)
    while True:
        print("Operation \n---------\n")
        print("1: Compile a fresh build\n")
        print("10: Compile Release (Installer)\n")
        print("2: Update")
        print("3: Commit")
        print("4: Revert\n")
        print("5: Start Blender\n")
        print("6: Compile")
        print("7: Clean\n")
        print("0: Back to Main menu")
        print("")

        op = int(input(">> "))
        nsis = False
        
        if op == 1:
            bit = int(input("32 or 64 bit? "))
            svn.update(path)
            rev = svn.revision(path)
            os.system('D:/blender_dev/remove_install.bat')
            scons.clean(path)
            if bit == 32:
                scons.compile_32(path, nsis)
                tools.copy_libs_32(tree)
            elif bit == 64:
                scons.compile_64(path, nsis)
                tools.copy_libs_64(tree)
            else:
                continue
            tools.compress(tree, rev, bit)
        elif op == 10:
            bit = int(input("32 or 64 bit? "))
            svn.update(path)
            rev = svn.revision(path)
            os.system('D:/blender_dev/remove_install.bat')
            scons.clean(path)
            if bit == 32:
                scons.compile_32(path, nsis=True)
                #tools.copy_libs_32(tree)
            elif bit == 64:
                scons.compile_64(path, nsis=True)
                #tools.copy_libs_64(tree)
            else:
                continue
        elif op == 2:
            svn.update(path)
        elif op == 3:
            svn.commit(path)
        elif op == 4:
            svn.revert(path)
        elif op == 5:
            try:
                os.chdir('D:/blender_dev/install/%s' % tree)
                Popen('D:/blender_dev/install/%s/blender.exe' % tree)
            except:
                print ("No binary file found. Please recompile.")
        elif op == 6:
            bit = int(input("32 or 64 bit? "))
            if bit == 32:
                scons.compile_32(path, nsis)
            elif bit == 64:
                scons.compile_64(path, nsis)
        elif op == 7:
            scons.clean(path)
        elif op == 0:
            os.system('cls')
            start()

def start():  
    print ("Welcome to the Blender Compile Helper")
    
    #Variablen
    tree = print_list()
    full_path = str(root_path + tree)
    
    os.system('cls')
    sub_call(tree, full_path)

    
start()

