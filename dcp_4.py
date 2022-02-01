"""
dcp_4
Created January 31, 2022 by Jennifer Baughman

Description: Given an array of integers, find the first missing positive
integer in linear time and constant space. In other words, find the lowest
positive integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2,
0] should give 3.
You can modify the input array in-place.

"""


def missing_integer(nums):
    # sorts and removes duplicate and negative numbers
    pos_nums = sorted([i for i in set(nums) if i > 0])

    # once sorted, the last value in the list will help us set a range
    highest = pos_nums[-1]
    
    # highest+2 catches cases with no gaps in the array
    # eg [1, 2] ==> 3
    return [i for i in range(pos_nums[0], highest + 2) if i not in pos_nums][0]


def main():
    pass


if __name__ == "__main__":
    main()
