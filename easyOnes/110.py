from typing import Optional,List
# 判断输入是否为平衡二叉树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        elif root.left == None or root.right==None:
            # history
            # return abs(self.get_height(root.left)-self.get_height(root.right)) <= 1 
            # right one , 除了当前节点，还需要确定左右节点是否平衡
            return abs(self.get_height(root.left)-self.get_height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) 
           
    
    def get_height(self,root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        return 1 + max(self.get_height(root.left),self.get_height(root.right))