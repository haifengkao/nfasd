nfasd
=====

Autocomplete nvim recent files in command line

Installation
------------
Install the python package
:: 
    pip install nfasd

Add the following line in your :code:`~/.bashrc`
::
    eval "$(register-python-argcomplete nfasd)"

Alternatively, if you are a zsh user, add the following to :code:`~/.zshrc`
::
    autoload bashcompinit
    bashcompinit
    eval "$(register-python-argcomplete nfasd)"

Configuration
-------------

Add the following to :code:`~/.bashrc` or :code:`~/.zshrc`
:: 
    alias n='nfasd -e nvim'
    alias ny='nfasd -e nyaovim'

Then you can press :code:`n myPro<tab>`
to get :code:`n ~/myProject`
