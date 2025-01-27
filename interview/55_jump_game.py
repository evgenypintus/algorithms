class Solution(object):
    visited = dict()


    def jump(self, nums, position):

        # reached the end
        if position == len(nums)-1:
            return True

        if nums[position] == 0:
            return False

        # Check all jump length
        for i in range (position+1, min(len(nums)-1, nums[position]+position)+1):

            if i not in self.visited:
                self.visited[i] = 1
                if self.jump(nums, i):
                    return True


        return False

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.visited = dict()

        return self.jump(nums, 0)

if __name__ == '__main__':
    s = Solution()

    nums = [1,2]
    print(s.canJump(nums))