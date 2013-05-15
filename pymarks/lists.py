#!/user/bin/env python
#-*- coding: utf-8 -*-

"""
    lists
    ~~~~~

    Experimentation to determine the best way to perform various tasks
    with lists, including concatenation/resizing, etc.
"""

from utils import ptimeit

lst = "lst = range(50000000)"

setups = [
    ("""%s
def _resize_list(x, newsize):
    if len(x) < newsize:
        x += [None] * (newsize - len(x))
""" % lst, "+="),
    ("""%s
def _resize_list(lst, newsize):
    if len(lst) < newsize:
        lst.extend(None for _ in xrange(newsize - len(lst)))
""" % lst, "extend w/ generator"),
    ("""%s
def _resize_list(lst, newsize):
    if len(lst) < newsize:
        lst.extend([None] * (newsize-len(lst)))
""" % lst, "extend w/ [None] * size_delta")
    ]

for _setup, _desc in setups:
    ptimeit("_resize_list(lst, 200000)", setup=_setup, desc=_desc, n=1000000)
