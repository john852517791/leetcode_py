def lengthOfLongestSubstring( s: str) -> int:
    index = 1
    a=0
    b=1
    max = 0
    if len(s) == 1:
        return 1
    if len(s)==0:
        return 0
    while(index<len(s)):
        # 滑动窗————默认归到[a：b]第一个字符temp，判断下一个字符是否在temp中，如果在则更新temp以及index，如果不在则更新a=1+a;b=a+1;index=b
        temp = s[a:b]
        if s[index] in temp:
            a+=1
            b=a+1
            index = b
        else:
            b+=1
            index+=1
        if max<len(s[a:b]):
            max = len(s[a:b])
    return max
print(lengthOfLongestSubstring("abcabcbb"))