#!/usr/local/bin/python3

# This is just a script to provide the steps to install modules in python3.

currentError = '''
i@raspberrypi ~ $ python3
Python 3.4.2 (default, Oct 19 2014, 13:31:11)
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>> import matplotlib
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'matplotlib'
>>>

Currently NO modules present as matplotlib
'''

moduleInstall = '''

pi@raspberrypi ~ $ sudo apt-get install python-matplotlib
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following extra packages will be installed:
  fonts-lyx libglade2-0 libjs-jquery-ui python-dateutil python-glade2 python-imaging python-matplotlib-data python-mock python-nose python-pyparsing python-tz
Suggested packages:
  libjs-jquery-ui-docs python-gtk2-doc dvipng ghostscript inkscape ipython python-cairocffi python-configobj python-excelerator python-matplotlib-doc python-qt4 python-scipy python-sip python-tornado
  python-traits python-wxgtk3.0 texlive-extra-utils texlive-latex-extra ttf-staypuft python-mock-doc python-coverage python-nose-doc
The following NEW packages will be installed:
  fonts-lyx libglade2-0 libjs-jquery-ui python-dateutil python-glade2 python-imaging python-matplotlib python-matplotlib-data python-mock python-nose python-pyparsing python-tz
0 upgraded, 12 newly installed, 0 to remove and 0 not upgraded.
Need to get 7,813 kB of archives.
After this operation, 22.7 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
0% [Connecting to mirrordirector.raspbian.org]
'''


print(currentError)
print(moduleInstall)


