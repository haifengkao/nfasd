#!/usr/bin/env python

def index_map(user_input, string):
  indices = {}
  for ch in user_input:
    if not indices.has_key(ch):
      indices[ch] = []

  for i, ch in enumerate(string):
    if indices.has_key(ch):
      index = indices[ch]
      index.append(i)

  return indices

# for file name partial matching
def dist(user_input, string):
  if len(user_input) <= 0:
    # are you kidding me?
    return 0

  max_cost = len(user_input) + 1
  indices = index_map(user_input, string)

  # first line
  distances = []
  for i in indices[user_input[0]]:
    distances.append((i, 0)) # index, cost

  for ch in user_input[1:]:
    if len(distances) <= 0:
      break
    distances_ = []
    for i in indices[ch]:
      min_cost = max_cost
      for t in distances:
        # TODO: binary search?
        if (t[0] >= i):
          continue

        if t[0] != i - 1:
          # non-consecutive matching
          # cost++
          # e.g. compare 'aa' against 'aba'
          cost = t[1] + 1
        else:
          # consecutive matching
          # e.g. compare 'aa' against 'aa' or 'baa' or 'aab'
          cost = t[1]
        if cost < min_cost:
          min_cost = cost

      distances_.append((i, min_cost))
    distances = distances_

  if len(distances) > 0:
    return distances[-1]
  else:
    return None # user_input is not a subsequence of string


if __name__ == "__main__":
  print dist('aa', 'aa')                  # =>(1, 0)
  print dist('aa', 'aab')                 # =>(1, 0)
  print dist('aa', 'baa')                 # =>(2, 0)
  print dist('aa', 'bbaa')                # =>(3, 0)
  print dist('aa', 'aabb')                # =>(1, 0)
  print dist('aa', 'abba')                # =>(3, 1)
  print dist('aaa', 'ababa')              # =>(4, 2)
  print dist('init', 'ing/install.sh')    # =>(7, 2)
  print dist('init', 'ing/nvim/init.vim') # =>(12, 0)
  print dist('init', 'ing/insitall.sh')   # =>(8, 1)
  print dist("foo",  "foobar")            # =>(2, 0)
  print dist("foo",  "FooBar")            # =>None
  print dist("fb",  "foobar")             # =>(3, 1)
  print dist("",  "foo bar")              # =>0
  print dist("",  "")                     # =>0
  print dist("f",  "")                    # =>None


















