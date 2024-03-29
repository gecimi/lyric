
#!/usr/bin/python
#coding=utf-8

import sys
sys.path.append('./src')

from distutils.core import setup
from lyric import __version__

setup(name='lyric',
      version=__version__,
      description='Lyric API from gecimi.com',
      long_description=open('README.md').read(),
      author='solos',
      author_email='solos@solos.so',
      py_modules=['lyric'],
      scripts=['lyric.py'],
      license='MIT',
      platforms=['any'],
      url='https://github.com/solos/lyric')
