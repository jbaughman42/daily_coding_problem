"""
dcp_5
Created February 01, 2022 by Jennifer Baughman

Description: cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair. For example, car(cons(3,
4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

Solution: pair()'s parameter f is, by definition, a function that takes two 
arguments. Therefore, the solution is to create a nested function that accepts 
two arguments and returns the first or last, as needed. pair() returns the 
output of the function passed.

A more elegant solution would be to create a helper function _unpack that
returns a, b as a tuple and have car() and cdr() return tuple[0] and [1]
respectively, but I wrote the functions this way to maintain the idiom
of cons().
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    
    return pair


def car(pair):
    def unpack(a, _):
        return a
    
    return pair(unpack)


def cdr(pair):
    def unpack(_, b):
        return b
    
    return pair(unpack)


def main():
    pair = cons(3, 4)
    print(car(pair))
    print(cdr(pair))


if __name__ == "__main__":
    main()
