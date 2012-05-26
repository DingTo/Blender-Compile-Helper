import os
from subprocess import Popen

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