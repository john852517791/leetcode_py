# 问题：输入A和B 输出B在A中匹配字符串的第一个字符的下标
# 思路：先判断A中是否存在B（in），用字符串切片


def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        # pass
        for a in range(len(haystack)):
            if (len(needle)+a) <= len(haystack):
                if haystack[a:len(needle)+a] == needle:
                    return a                    
    else:
        return -1

print(strStr("hello","ll"))