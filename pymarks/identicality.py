#!/user/bin/env python
#-*- coding: utf-8 -*-

"""
    identicality
    ~~~~~~~~~~~~

    Performance metrics for checking if all items in a list are the
    same
"""

from utils import ptimeit

setups = [("lst = [1] * 1100",
           "A list of 1100, 1's (all ones)"),
          ("lst = ([1] * 549) + range(551)",
           "A list of 1100, first half 1's"),
          ("lst = range(551) + ([1] * 549)",
           "A list of 1100, latter half 1's"),
          ("lst = range(1100)",
           "A list of 1100 values, all unique")]

for _setup, desc in setups:
    print desc

    # Prereq: Python 2.5+
    ptimeit("len(set(lst)) == 1", setup=_setup, desc="set")
    
    # Prereq: Python 2.5+
    ptimeit("min(lst) == max(lst)", setup=_setup, desc="min")
    
    # Slightly less performant than inline or multiline
    ptimeit("all(x == lst[0] for x in lst)", setup=_setup, desc="all")

    # Slightly less performant than inline or multiline
    ptimeit("any(x != lst[0] for x in lst)", setup=_setup, desc="!any")
