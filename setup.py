from setuptools import setup

setup(name='nfasd',
      version='0.2',
      description='fasd for neovim',
      keywords='fasd neovim nvim nyaovim jumplist',
      url='http://github.com/haifengkao/nfasd',
      author='Hai Feng Kao',
      author_email='haifeng@cocoaspice.in',
      license='MIT',
      packages=['nfasd'],
      scripts=['bin/nfasd'],
      install_requires=[
          'argcomplete',
      ],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Shells',
      ],
      zip_safe=False)
