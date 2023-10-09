from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # def height(root: Optional[TreeNode]):
        #     if root==None:
        #         return 0
        #     return 1+max(height(root.left),height(root.right))
        
        # def lorR(l: Optional[TreeNode],r: Optional[TreeNode]):
        #     if r==None and l!=None:
        #         return True
        #     if r!=None and l==None:
        #         return False
        #     if height(l)<height(r):
        #         return True
        #     return False
        
        # if root==None:
        #     return 0
        # if root.left==None and root.right ==None:
        #     return 1
        
        # if lorR(root.left,root.right):
        #     return 1+self.minDepth(root.left)
        # else:
        #     return 1+self.minDepth(root.right)
        
        # 情况1：判断是否为叶子————左右子节点是否为none     直接返回1即可
        # 情况2：左右子节点存在一个，且另一个为none，需要走非空的子树   递归输入非空子树根
        # 1、2合并，1————左右节点都为none即为0，2————左右节点有一个为空即为0
        # 情况3：左右子节点都存在，需要走高度较矮的子树     递归输入矮子树根
        
        # 和求树的高度类似 ，只是划为最小高度
        
        
        if root==None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if root.left==None or root.right==None :
            return left+right+1 
        else:
            return min(left,right)+1