# 输入n，输出多个1、2的组合数量，要求组合的和为n
# class Solution:
import math
def climbStairs(n: int) -> int:
    num2 = int(n / 2)
    res = 0
    for i in range(num2):
        # 2的数量
        n2=i+1
        # 1的数量
        n1=n-2*n2
        if (i+1)==num2 and n%2==0:
            res+=1
        else:
            # n1个1和n2个2能有多少种组合
            res+=math.factorial(n2 + n1) / (math.factorial(n1) * math.factorial(n2))
    return int(res)+1 #全1的情况

print(climbStairs(6))