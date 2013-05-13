#!/user/bin/env python
#-*- coding: utf-8 -*-

"""
    if
    ~~

    Experimentation to determine the best way to use conditionals
"""

from utils import ptimeit

# Prereq: Python 2.5+
ptimeit("x = 5 if False else 4", desc="inline if")

# Slightly less performant than inline or multiline
ptimeit("x = (5, 4)[False]", desc="tuple evaluation")

ptimeit("x = 5 if False else 4", """if False:
    x = 5
else:
    x = 4""",  desc="multi-line if")

