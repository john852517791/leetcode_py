from typing import Optional,List
# 杨辉三角
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<=0:
            return [[]]
        else:
            res = []

        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                temp = []
                for j in range(i+1):
                    if j==0 or j==i:
                        temp.append(1)
                    else:
                        temp.append(res[i-1][j]+res[i-1][j-1])
                res.append(temp)
        return res