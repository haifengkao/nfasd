#!/usr/bin/env python
import os     # to execute nvim

# for file name partial matching
def dist(user_input, string):
  if len(user_input) > len(string):
    # impossible matching, return highest possible cost
    return len(user_input)

    distances = range(len(user_input) + 1)
    for i2, c2 in enumerate(string):
        distances_ = [i2+1]
        for i1, c1 in enumerate(user_input):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


if __name__ == "__main__":
  print dist('aa', 'abba')

