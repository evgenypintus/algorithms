"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
 and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:

            current_index = len(result)-1

            # Empty list or not overlapping
            if not result or result[current_index][1] < i[0]:
                result.append(i)
            # End of the current interval is greater than the beginning of the next, merging
            else:
                result[current_index][1] = max(result[current_index][1], i[1])

        return result


if __name__ == '__main__':

    s= Solution()

    intervals =[[1,6],[1,2], [2,6], [1,4],[2,3],[8,10], [10,11],[15,18]]

    print(s.merge(intervals))