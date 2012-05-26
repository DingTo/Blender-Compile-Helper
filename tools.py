import os

def compress(tree, rev, bit):
    os.system('C:/7-Zip/7z.exe a D:/blender_dev/archives/%s_win%s_%s.7z D:/blender_dev/install/%s' % (tree, bit, rev, tree))

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
    