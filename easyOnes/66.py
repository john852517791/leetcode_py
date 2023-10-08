# 数组表示数字，完成数字+1然后返回数字数组
# 思路：还原数字，+1，还原数组，返回
from typing import List
def plusOne(digits: List[int]) -> List[int]:
    number=0
    for i in range(len(digits)):
        number += digits[-1-i] * (10 ** i)
    number+=1
    result = []
    for j in range(len(str(number))):
        result.append(int(str(number)[j]))
    return result

