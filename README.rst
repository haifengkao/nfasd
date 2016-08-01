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

    # use TAB to cycle through all possible matches
    # optional but highly recommended
    [[ $- = *i* ]] && bind TAB:menu-complete    

Alternatively, if you use zsh, add the following to :code:`~/.zshrc`
::
    eval "$(register-python-argcomplete nfasd)"

Configuration
-------------

Add the following to :code:`~/.bashrc` or :code:`~/.zshrc`
:: 
    alias n='nfasd -e nvim'
    alias ny='nfasd -e nyaovim'

Then you can press :code:`n myPro<tab>`
to get :code:`n ~/myProject`

Special Thanks
--------------
`fasd <https://github.com/clvv/fasd>`_ : the awesome command line tool
