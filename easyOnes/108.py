# Definition for a binary tree node.

from typing import Optional,List
import math
# 把有序数组转换为二叉搜索树
# 换算二叉树高度，
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if (len(nums)==0):
            return None
        mid = int(len(nums)/2)
        root = TreeNode(nums[mid])
        nums_left = nums[0:mid-1]
        nums_right = nums[mid+1:len(nums)]
        root.left = self.sortedArrayToBST(nums_left)
        root.right = self.sortedArrayToBST(nums_right)
        return root
        return self.build(nums,0,len(nums)-1)

    # def build(self,nums: List[int],l,r):
    #     if (l>r):
    #         return None
    #     mid = (l+r)//2
    #     root = TreeNode(nums[mid])
    #     root.left = self.build(nums,l,mid-1)
    #     root.right = self.build(nums,mid+1,r)
    #     return root
        