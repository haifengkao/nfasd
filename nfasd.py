#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argcomplete, argparse
import re     # regex module from standard library.
from neovim import attach
# from argcomplete import warn # logging

def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*?'.join(user_input)   # Converts 'djm' to 'd.*?j.*?m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        match = regex.search(item)   # Checks if the current item matches the regex.
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]

# no need to validate
def novalidator(completion, prefix):
    # return TRUE
    return completion.startwith(prefix)

nvim = attach('child', argv=["nvim", "--embed"])
nvim.command('let nfasd_history = v:oldfiles')
history = nvim.vars['nfasd_history']

def nvim_recent_files(prefix, parsed_args, **kwargs):
    if len(prefix):
      return fuzzyfinder(prefix, history)
    return history


parser = argparse.ArgumentParser()
parser.add_argument("-f", help="nvim recent files").completer = nvim_recent_files

argcomplete.autocomplete(parser, validator=None)
# argcomplete.autocomplete(parser)
args = parser.parse_args()

