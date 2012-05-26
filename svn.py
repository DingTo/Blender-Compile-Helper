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

def update(path):
    os.chdir('%s' % path)
    os.system('svn up')
    
def commit(path):
    Popen('TortoiseProc.exe /command:commit /path:%s /closeonend:0' % path)
    
def revert(path):
    Popen('TortoiseProc.exe /command:revert /path:%s /closeonend:0' % path)

# Read SVN Revision
def revision(path):
    os.system('SubWCRev.exe %s D:/blender_dev/revision.tmpl D:/blender_dev/revision.txt' % path)
    svn_revision = open('D:/blender_dev/revision.txt', 'r')
    rev = svn_revision.read()

    return rev