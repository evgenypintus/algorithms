"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

"""
from collections import namedtuple


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    Height = namedtuple('Height', ['balance', 'height'])

    def tree_height_balance(self, p, height = 0):

        if not p:
            return self.Height(True, height)
        left, right = self.tree_height_balance(p.left, height+1),  self.tree_height_balance(p.right, height+1)

        balance = (left.balance and right.balance and abs(left.height - right.height)<=1)

        return self.Height(balance, max(left.height, right.height))

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.tree_height_balance(root).balance