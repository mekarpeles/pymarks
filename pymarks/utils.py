#!/user/bin/env python
#-*- coding: utf-8 -*-

"""
    utils
    ~~~~~

    Utilities for benchmarking different python operations
"""

import timeit

def ptimeit(expr, setup="", n=100000, desc=""):
    t = timeit.timeit(expr, setup=setup, number=n)
    print "%s: %s loops, best of 3: %s usec per loop" % (desc, n, t)
