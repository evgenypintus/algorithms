"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def isSymmetric(self, p):

        if p.left and p.right:
            if p.left.val != p.right.val:
                return False

        return self.isSameTree(p.left, p.right)


    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p and not q:
            return True

        if (p and not q) or (not p and q) or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)


if __name__ == '__main__':

    s= Solution()
    [1, 2, 2, 3, 4, 4, 3]

    p = TreeNode(1,TreeNode(2),TreeNode(3, TreeNode(4),  TreeNode(5)))

    print(s.isSymmetric(p))