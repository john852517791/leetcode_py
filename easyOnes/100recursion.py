from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # 思路：树相同的多种情况，1、都为空 2、其一为空 3、根节点值相同 4、子节点（递归点）值都相同
    # 错误！！！：值相同就返回true——导致没比完就返回，应该先考虑满足返回条件之外的其他情况
    
    
    # 判断是否都为空
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
        return self.isSameNode(p.left,q.left) and self.isSameNode(p.right,q.right)