# pymarks

Various benchmarks for common operations in python

* Reversing lists
* conditionals, single line 

## Identicality

Testing if all items in a list are identical:

    $ python identicality.py 
    A list of 1100, 1's (all ones)
    set: 100000 loops, best of 3: 2.58085799217 usec per loop
    min: 100000 loops, best of 3: 4.85045599937 usec per loop
    all: 100000 loops, best of 3: 8.8568110466 usec per loop
    !any: 100000 loops, best of 3: 8.82808494568 usec per loop
    A list of 1100, first half 1's
    set: 100000 loops, best of 3: 3.46082782745 usec per loop
    min: 100000 loops, best of 3: 4.93469214439 usec per loop
    all: 100000 loops, best of 3: 4.47458219528 usec per loop
    !any: 100000 loops, best of 3: 4.48427581787 usec per loop
    A list of 1100, latter half 1's
    set: 100000 loops, best of 3: 3.47670006752 usec per loop
    min: 100000 loops, best of 3: 4.89735507965 usec per loop
    all: 100000 loops, best of 3: 0.0880379676819 usec per loop
    !any: 100000 loops, best of 3: 0.0908908843994 usec per loop
    A list of 1100 values, all unique
    set: 100000 loops, best of 3: 3.61140394211 usec per loop
    min: 100000 loops, best of 3: 4.95152592659 usec per loop
    all: 100000 loops, best of 3: 0.0881590843201 usec per loop
    !any: 100000 loops, best of 3: 0.0902299880981 usec per loop

### Conclusions

* all() outperforms set() == 1 only when (due to short circuiting) a non-identical value is present early in the list.
* overall, unless you can prove your list of elements has such a uniformity that using all will be more performant (see special case below), set() in general is the most performant construct for testing list element uniqueness.
* If testing uniqueness is desireable an all elements are expected to have/be hashable types, consider using set() to begin with (as your original data structure), instead of a list.