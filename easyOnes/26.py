from typing import Optional,List
def removeDuplicates( nums: List[int]) -> int:
        i = 1
        if len(nums)<=1:
            return len(nums)
        temp = nums[0]
        while(i<len(nums)):
            if temp == nums[i] and i == len(nums)-1:
                nums[0:len(nums)] = nums[0:len(nums)-1]
            elif temp == nums[i]:
                nums[i:len(nums)] = nums[i+1:len(nums)]
            else:
                temp = nums[i]
                i+=1
        return len(nums)