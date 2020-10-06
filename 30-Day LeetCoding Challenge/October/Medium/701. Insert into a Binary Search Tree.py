# https://leetcode.com/problems/insert-into-a-binary-search-tree/
    
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        r = root
        while root:
            if root.val < val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    return r
            elif root.left:
                root = root.left
            else:
                root.left = TreeNode(val)
                return r
        return TreeNode(val)
