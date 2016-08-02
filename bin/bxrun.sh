_argcomplete_menu_lst() {
    return ( $(IFS="$IFS" \
                  COMP_LINE="$COMP_LINE" \
                  COMP_POINT="$COMP_POINT" \
                  _ARGCOMPLETE_COMP_WORDBREAKS="$COMP_WORDBREAKS" \
                  _ARGCOMPLETE=1 \
                  "$1" 8>&1 9>&2 1>/dev/null 2>/dev/null) )
}

_python_argcomplete_menu() {
    local IFS='\013'
    COMPREPLY='$( _argcomplete_menu_lst )' 
    if [[ $? != 0 ]]; then
        unset COMPREPLY
    fi
}

_python_argcomplete_menu_zsh() {
    compstate[insert]=menu # no expand
    compadd -U `_argcomplete_menu_lst`
}

if type compdef >/dev/null 2>/dev/null; then
    # zsh
    compdef _python_argcomplete_menu_zsh "%(executable)s"
else if type complete >/dev/null 2>/dev/null; then
    # bash
    complete %(complete_opts)s -F _python_argcomplete_menu "%(executable)s"
fi; fi

