"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def walk_tree(self, p, q):

        if not p and not q:
            return True

        if (p and not q) or (not p and q) or p.val != q.val:
            return False

        return self.walk_tree(p.left, q.left) and self.walk_tree(p.right, q.right)


    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        return self.walk_tree(p,q)


if __name__ == '__main__':

    s= Solution()

    p = TreeNode(1,TreeNode(2),TreeNode(3, TreeNode(4),  TreeNode(5)))
    q = TreeNode(1,TreeNode(2),TreeNode(3))

    print(s.isSameTree(p, q))