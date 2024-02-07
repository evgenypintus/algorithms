"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

The guess API is already defined for you.
@param num, your guess
@return -1 if num is higher than the picked number
         1 if num is lower than the picked number
         otherwise return 0
def guess(num):
"""

GLOBAL_NUMBER = 586889
GLOBAL_N = 2**31 - 1

def guess(number):

    if number == GLOBAL_NUMBER:
        return 0
    elif number > GLOBAL_NUMBER:
        return -1
    else:
        return 1


def search_number(left=1, right=None):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if right is None:
        right = GLOBAL_N

    mid = (left + right) // 2

    print(mid)

    result_guess = guess(mid)
    if result_guess == 0:
        return mid

    if result_guess == 1:
        return search_number(mid+1, right)
    else:
        return search_number(left, mid-1)


print(search_number())
