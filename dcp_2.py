"""
dcp_2
Created January 29, 2022 by Jennifer Baughman

Description: Given an array of integers, return a new array such that each
element at index i of the new array is the product of all the numbers in the
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [
120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
be [2, 3, 6].

Follow-up: what if you can't use division?
"""

from operator import mul
from itertools import accumulate


def calc_mult_array(array):
    """Calculate multiples of input array values not including the value at
    each index. Does not use division.
    
    :param array:
    :return:
    """
    output = []
    for index, value in enumerate(array):
        working = array[0:index] + array[index + 1:]
        output.insert(index, list(accumulate(working, mul))[-1])
    return output


def main():
    print(calc_mult_array([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
