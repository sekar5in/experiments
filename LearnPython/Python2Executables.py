# Convert the urllibscript.py script into executables using cx_Freeze 3rd party module.

from cx_Freeze import Executable, setup


setup(name='urlParse',
      version='0.1',
      description='Parse Stuff',
      executables=[Executable('urllibscript.py')])

# Procedure to run this to enable the exe is : python Python2Executables.py build  in command line.
# It builds and build directory is created with all files and exe.

