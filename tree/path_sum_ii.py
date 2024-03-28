"""
113. Path Sum II


Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where
 the sum of the node values in the path equals targetSum.
 Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
if __name__ == '__main__':

    s= Solution()

    nums = [3,5,0,3,4]

    print(s.find132pattern(nums))