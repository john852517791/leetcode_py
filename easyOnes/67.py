# 给定二进制两个值，相加后返回二进制结果
# 思路：转十进制？
def addBinary(a: str, b: str) -> str:
    # def to10(i:str)->int:
    #     res=0
    #     for q in range(len(i)):
    #         res+=int(i[-1-q]) * (2 ** q)
    #     return res
    # sum = to10(a) + to10(b)
    sum = int(a,2)+int(b,2)
    print(bin(sum)[2:])
    # 0b100
    
    return 0
addBinary("11","1")
        