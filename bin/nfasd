#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argcomplete, argparse
import re     # regex module from standard library.
import os     # to execute nvim
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
    res = []
    if len(prefix):
      res = fuzzyfinder(prefix, history)
    else:
      res = history

    # can only return signal value, otherwise the terminal will only show the longest common prefix
    res = res[:1]

    # need to add prefix in zsh
    # otherwise, the terminal won't show anything (bash doesn't need it)
    return [ prefix + ' ' + x for x in res]

parser = argparse.ArgumentParser()
parser.add_argument("filepath").completer = nvim_recent_files

def my_validator(current_input, keyword_to_check_against):
    # warn('my_validator'+current_input+keyword_to_check_against)
    # Pass through ALL options even if they don't all start with 'current_input'
    return True

argcomplete.autocomplete(parser, validator=my_validator, always_complete_options=False) # don't complete annoying --help

# args = parser.parse_args()
args, unknown = parser.parse_known_args()

# print args.filepath
# print unknown

if len(unknown):
  path = unknown[0]
else:
  path = args.filepath
execStr = 'nvim ' + path

os.system(execStr)
