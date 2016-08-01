# bash completion for bxrun (/home/ecuomo/projects/bashx/bxrun)
_bxrun_lst() {
    echo 'abc bcd def'
}
_bxrun() {
    local cur
    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}
    COMPREPLY=( $( compgen -W '$( _bxrun_lst )' -- $cur  ) )
}
_bxrun_zsh() {
    compstate[insert]=menu # no expand
    compadd -U `_bxrun_lst`
}

# copied from fasd
#[ "$ZSH_VERSION" ] && emulate sh && setopt localoptions
#setopt MENU_COMPLETE
#setopt  NO_LIST_BEEP
if type compdef >/dev/null 2>/dev/null; then
    # zsh
    compdef _bxrun_zsh bxrun
#else if type complete >/dev/null 2>/dev/null; then
    ## bash
    #complete -F _bxrun bxrun
fi;
