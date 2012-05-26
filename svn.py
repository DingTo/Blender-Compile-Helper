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