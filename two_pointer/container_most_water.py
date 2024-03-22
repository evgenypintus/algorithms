"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxwater, i, j = 0, 0, len(height) - 1  # Initialize maxwater and two pointers
        while i < j:  # Iterate until the two pointers meet or cross each other
            maxwater = max(maxwater, (j - i) * min(height[i], height[j]))  # Calculate the current area and update maxwater
            if height[i] < height[j]:  # Move the pointer with smaller height towards the other pointer
                i += 1
            else:
                j -= 1
        return maxwater  # Return the maximum water area

if __name__ == '__main__':

    sol= Solution()

    height = [1,1]

    print(sol.maxArea(height))