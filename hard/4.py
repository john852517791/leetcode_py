from typing import Optional,List
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # 中位数，如果总数为单数，中位数下标就是whole/2+1，如果为双数，下标则有两个，whole/2和whole/2+1
    # 记录whole/2和whole+1
            whole = len(nums1)+len(nums2)
            i=0
            j=0
            mark=0
            temp=-1
            a=-1
            b=-1
            while(i<len(nums1) and j<len(nums2)):
                if nums1[i]< nums2[j]:
                    temp = nums1[i]
                    i+=1
                    mark += 1
                else:
                    temp = nums2[j]
                    j+=1              
                    mark += 1
                if mark == int(whole/2):
                    a = temp
                if mark == int(whole/2)+1:
                    b=temp
            while(i<len(nums1) and (a==-1 or b==-1)):
                temp = nums1[i]
                i+=1
                mark += 1
                if a==-1 and mark == int(whole/2):
                    a = temp
                if b==-1 and mark == int(whole/2)+1:
                    b=temp
            while(j<len(nums2) and (a==-1 or b==-1)):
                temp = nums2[j]
                j+=1
                mark += 1
                if a==-1 and mark == int(whole/2):
                    a = temp
                if b==-1 and mark == int(whole/2)+1:
                    b=temp
            if (whole%2==0):
                return (a+b)/2.0
            else:
                return b
print(findMedianSortedArrays([],[1]))