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

def compile_64(path, nsis):
    os.chdir('%s' % path)
    if nsis:
        os.system('python scons/scons.py nsis -j8 BF_BITNESS=64')
    else:
        os.system('python scons/scons.py -j8 BF_BITNESS=64')
    
def compile_32(path, nsis):
    os.chdir('%s' % path)
    if nsis:
        os.system('python scons/scons.py nsis -j8 BF_BITNESS=32')
    else:
        os.system('python scons/scons.py -j8 BF_BITNESS=32')

def clean(path):	
    os.chdir('%s' % path)
    os.system('python scons\scons.py clean -j8')