from setuptools import setup
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='nfasd',
      version='2.0',
      description='fasd for neovim',
      keywords='fasd neovim nvim nyaovim jumplist',
      url='http://github.com/haifengkao/nfasd',
      author='Hai Feng Kao',
      author_email='haifeng@cocoaspice.in',
      license='MIT',
      long_description=long_description,
      long_description_content_type="text/x-rst",
      packages=['nfasd'],
      scripts=['bin/nfasd', 'bin/register-python-argcomplete-menu'],
      install_requires=[
          'argcomplete',
          'msgpack-python',
      ],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Shells',
        'Topic :: Utilities',
      ],
      zip_safe=False)
