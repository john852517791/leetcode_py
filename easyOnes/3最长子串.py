def sameinit(s:str)->bool:
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return False
        else:
            continue
    return True
def lengthOfLongestSubstring(s: str) -> int:
        # 遍历取出某个长度的字符串
        # max = 1
        # for i in range(len(s)):
        #     for j in range(len(s)-i):
        #         short = s[j:i+1+j]
        #         if sameinit(short):
        #             max = i+1
        #             break
        max,pastend = 0,0
        front = 0
        end = 1
        while(end!=len(s)-1):
            short = s[front:end] 
            if sameinit(short):
                max += 1
                end+=1
            else:
                front+=1
                        
            
                        
        return max
    
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))

print(sameinit("abca"))
print(sameinit("abc"))