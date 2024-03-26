"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def tree_height(self, p, height = 0):

        if not p:
            return height
        return max(self.tree_height(p.left, height+1), self.tree_height(p.right, height+1))


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return (not root) or ( self.isBalanced(root.left) and self.isBalanced(root.right) and
                               abs(self.tree_height(root.left) - self.tree_height(root.right)) <= 1)