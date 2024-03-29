nfasd
=====

Autocomplete nvim recent files in command line

Installation
------------
Install the python package

.. code:: bash

    pip install nfasd

Add the following line in your :code:`~/.bashrc`

.. code:: bash

    eval "$(register-python-argcomplete-menu nfasd)"
 
    # use TAB to cycle through all possible matches
    # optional but highly recommended
    [[ $- = *i* ]] && bind TAB:menu-complete    

Alternatively, if you use zsh, add the following to :code:`~/.zshrc`

.. code:: bash

    eval "$(register-python-argcomplete-menu nfasd)"
    # stop shell from beeping for every complete
    # optional but highly recommended
    setopt NO_LIST_BEEP
 
For fish shell, you need to install

.. code:: bash

    pip install argcomplete
    register-python-argcomplete --shell fish my-favourite-script.py > ~/.config/fish/my-favourite-script.py.fish

Configuration
-------------

Add the following to :code:`~/.bashrc` or :code:`~/.zshrc`

.. code:: bash

    alias n='nfasd -e nvim'
    alias ny='nfasd -e nyaovim'

Then you can press :code:`n myPro<tab>`
to get :code:`n ~/myProject`

`-e` specifies which executable to open the file

If you want to exclude certain file patterns,
use the `--exclude` option, e.g.

.. code:: bash

    alias n=`nfasd -e nvim --exclude tmp`

Changelog
-------------
2.0 for nvim 0.6 new shada format

1.0 for python3

0.19 for python2

Tips
----
To increase the number of recent files to 1000, add the following line to your `~/.config/nvim/init.vim`

.. code:: bash

    set shada=!,'1000,<50,s10,h

Special Thanks
--------------
`fasd <https://github.com/clvv/fasd>`_ : the awesome command line tool
