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

    def __init__(self):
        self.all_paths = []

    def find_sum(self, p, sum, cur_path, cur_sum):

        if not p:
            return

        cur_path.append(p.val)
        cur_sum += p.val
        if not p.left and not p.right:

            if cur_sum == sum:
                self.all_paths.append(list(cur_path))
            cur_sum = 0

        self.find_sum(p.left, sum, cur_path, cur_sum)
        self.find_sum(p.right, sum, cur_path, cur_sum)
        del cur_path[-1]

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.find_sum(root, targetSum, [], 0)
        return self.all_paths

if __name__ == '__main__':

    s = Solution()

    root = TreeNode(5,
                    TreeNode(4,
                             TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(7))))

    targetSum = 22

    print(s.pathSum(root, targetSum))
