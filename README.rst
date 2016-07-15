nfasd
=====

Open nvim recent files fast.


Installation
------------
Install the python package

.. code:: bash 
    pip install nfasd

Add the following line in your ~/.bashrc
.. code:: bash 
    eval "$(register-python-argcomplete nfasd)"

Alternately, if you are a zsh user, add the following to ~/.zshrc
.. code:: bash 
    autoload bashcompinit
    bashcompinit
    eval "$(register-python-argcomplete nfasd)"

Configuration
-------------

Add the following to ~/.bashrc or ~/.zshrc
.. code:: bash 
    alias n='nfasd -e nvim'
    alias ny='nfasd -e nyaovim'

Then you can press `n myPro<tab>` to make it `n ~/myProject`
