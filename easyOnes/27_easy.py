from typing import Optional,List
# class Solution:
def removeElement(nums: List[int], val: int) -> int:
        # 输入数组和一个数
        # 输出移除与输入数值相同后的数组长度
        # i=0
        # j=0
        # temp=0
        # count = 0
        # while(i<len(nums)):
        #     if nums[i]==val:
        #         j=i
        #         count+=1
        #         while(j<len(nums)-1):
        #             nums[j]=nums[j+1]
        #             j+=1
        #     i+=1
        # return len(nums)-count
        
        
        i=0
        while(i<len(nums)):
            if nums[i] == val and i == len(nums)-1:
                nums[0:len(nums)] = nums[0:len(nums)-1]
            elif nums[i] == val :
                nums[i:len(nums)] = nums[i+1:len(nums)]
            else:
                i+=1

# nm = [2,2,3]
# print(nm[0:len(nm)-1])
nums = [3,2,2,3]
removeElement(nums,3)
print(nums)