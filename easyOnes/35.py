# 问题：输入定升序数组A，和数字B，若B存在于A则返回下标，不存在则返回B应该在A中的下标
# 思路：遍历数组A，记录第一个大于等于B的值的下标，如果不存在则直接返回自增到最后的下标
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        mark = 0
        for a in nums:
            if a >= target:
                return mark
            mark+=1
        return mark
        
