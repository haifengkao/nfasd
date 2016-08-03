from setuptools import setup

setup(name='nfasd',
      version='0.8',
      description='fasd for neovim',
      keywords='fasd neovim nvim nyaovim jumplist',
      url='http://github.com/haifengkao/nfasd',
      author='Hai Feng Kao',
      author_email='haifeng@cocoaspice.in',
      license='MIT',
      packages=['nfasd'],
      scripts=['bin/nfasd', 'bin/register-python-argcomplete-menu'],
      install_requires=[
          'argcomplete',
          'neovim',
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
