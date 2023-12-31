from typing import Optional,List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        whole = m+n-1
        m-=1
        n-=1
        while(m > -1 and n > -1):
            if nums1[m]>nums2[n]:
                nums1[whole] = nums1[m]
                m-=1
            else:
                nums1[whole] = nums2[n]
                n-=1
            whole -= 1
        if n>-1:
            nums1[0:n+1] =nums2[0:n+1] 