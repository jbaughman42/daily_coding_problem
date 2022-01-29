"""
dcp_1
Created January 28, 2022 by Jennifer Baughman

Description: Given a list of numbers and a number k, return whether any two
numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
`
"""


def add_to_k(num_list, k):
    """Returns whether any two numbers from the list add up to k
    
    Args:
        num_list: (list) list of numbers
        k: sum value

    Returns: (bool) True if two numbers add to k, False otherwise

    """
    # This purges any numbers greater than k, since by definition
    # a number greater than k can't add up to k
    nums = [x for x in num_list if x <= k]
    for n in nums:
        x = k - n
        if x in nums:
            return True
    return False


def main():
    num_list = [10, 15, 3, 7]
    k = 17
    print(add_to_k(num_list, k))


if __name__ == "__main__":
    main()
