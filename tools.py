# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Copyright 2012, Thomas Dinges
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

def compress(root, tree, rev, bit):
    os.system('C:/7-Zip/7z.exe a %s/archives/%s_win%s_%s.7z %s/install/%s' % (root, tree, bit, rev, root, tree))

def copy_libs_32(tree):
    txt = open('D:/blender_dev/copy_msvc_libs_32.bat', 'w')
    txt.write("@echo on\n")
    txt.write("D:\n")
    txt.write("cd\ \n")
    txt.write("cd blender_dev\msvc_libs_32\n")
    txt.write("copy *.* ..\install\%s" % (tree))
    txt.close()
    os.system('D:/blender_dev/copy_msvc_libs_32.bat')
    
def copy_libs_64(tree):
    txt = open('D:/blender_dev/copy_msvc_libs_64.bat', 'w')
    txt.write("@echo on\n")
    txt.write("D:\n")
    txt.write("cd\ \n")
    txt.write("cd blender_dev\msvc_libs_64\n")
    txt.write("copy *.* ..\install\%s" % (tree))
    txt.close()
    os.system('D:/blender_dev/copy_msvc_libs_64.bat')
    