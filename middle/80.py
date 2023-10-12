# 
from typing import Optional,List
# a: List[int] = [1,2,3,4,5]
# print(a)
# a[2:len(a)] = a[3:len(a)]
# print(a)

def removeDuplicates(nums: List[int]) -> int:
        # 标记——重复超过2
        # temp——当前重复元素值
        # 
        # 找到第三个重复元素的下标给a 👉 找下一个不同元素的下标或者遍历结束 给b 👉 覆盖且更新当前下标b
        if len(nums)<=2:
            return len(nums)
        temp = nums[0]
        index = 1
        mark1 = False
        mark2 = False
        fooo = -1
        while(index<len(nums)):
            if temp==nums[index] and mark1 == True:
                mark2 = True
                fooo = index
                print("重复元素下标",fooo+1)
            if temp==nums[index] and mark1 == False:
                mark1 = True
            if temp!=nums[index]:
                temp = nums[index]
                mark1 = False
                mark2 = False
            if fooo!=-1:
                index+=1
                # 找下一个不同元素
                while(index<len(nums) and temp ==nums[index]):
                    index += 1                  
                # print("chon",index+1)
                if index<len(nums):
                    nums[fooo:len(nums)] = nums[index:len(nums)]
                    temp = nums[fooo]
                    index = fooo + 1
                    fooo = -1
                    mark1 = False
                    mark2 = False
                else:
                    nums = nums[0:fooo]
                
            else:
                index+=1
            print(nums,"and",index)
        return len(nums)

# removeDuplicates([0,0,1,1,1,1,2,3,3,3])
# print("zz")
removeDuplicates([1,1,1,2,2,3])
# removeDuplicates([1,1,1])