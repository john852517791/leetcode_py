from typing import Optional
# 轴对称————只需要判断左右子树左节点是否等于右节点即可
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameNode(p: Optional[TreeNode],q: Optional[TreeNode]) -> bool:
    if p == None and q == None:
        return True
    # 判断其一为空
    elif p == None or q == None:
        return False
    # 判断值相同
    elif p.val != q.val:
        return False
    # 判断子节点
    else:
        return isSameNode(p.left,q.right) and isSameNode(p.right,q.left)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return isSameNode(root.left,root.right)
        
         