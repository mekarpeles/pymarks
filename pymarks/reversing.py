#!/user/bin/env python
#-*- coding: utf-8 -*-

"""
"""

import timeit

_setup = "ol = [1, 2, 3] * 1000"

def ptimeit(expr, setup="", n=100000, desc=""):
    t = timeit.timeit(expr, setup=setup, number=n)
    print "%s: %s loops, best of 3: %s usec per loop" % (desc, n, t)

# I ran this set of 100000 and came up with 11.2:
ptimeit("reversed(ol)", setup=_setup, desc="reversed")

# This shows the overhead of list()
ptimeit("list(reversed(ol))", setup=_setup, desc="list(reversed)")

# This is the result for reverse via -1 step slices
ptimeit("ol[::-1]", setup=_setup, desc="[::-1]")

# This shows the overhead of inplace reversal (mutations)
ptimeit("ol.reverse()", setup=_setup, desc="ol.reverse()")
