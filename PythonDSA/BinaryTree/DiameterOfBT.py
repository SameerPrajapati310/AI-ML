"""
Given the root of a binary tree, return the length of its diameter.

The diameter of a binary tree is the length of the longest path between any
two nodes in the tree. This path may or may not pass through the root.

The length of a path is the number of edges between the two nodes.

Example:

Input:
        1
       / \
      2   3
     / \
    4   5

Output:
3

Explanation:
The longest path is 4 -> 2 -> 1 -> 3 (or 5 -> 2 -> 1 -> 3),
which contains 3 edges.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- Node values are not necessarily unique.
"""

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find(self,root):
        if root == None:
            return 0

        left = self.find(root.left)
        right = self.find(root.right)

        return 1 + max(left,right)

    def diameter(self,root):
        if root == None:
            return 0

        left_h = self.find(root.left)
        right_h = self.find(root.right)

        dia = left_h + right_h

        left_dia = self.diameter(root.left)
        right_dia = self.diameter(root.right)

        return max(left_dia,right_dia,dia)