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
    compadd -U `_bxrun_lst`
}
if type compdef >/dev/null 2>/dev/null; then
    # zsh
    compdef _bxrun_zsh bxrun
else if type complete >/dev/null 2>/dev/null; then
    # bash
    complete -F _bxrun bxrun
fi;
