# 左右括号，正确顺序闭合，如"([])"正确，但"([)]"错误
# 思路：左括号入栈，符合就出栈，最后判断栈内是否有元素

def isValid( s: str) -> bool:
    def left(t:str) -> bool:
        if t=="{" or t=="[" or t=="(":
            return True
        else:
            return False
    def match(a:str,b:str)->bool:
        if a=="{" and b=="}":
            return True
        elif a=="(" and b==")":
            return True
        elif a=="[" and b=="]":
            return True
        else:
            return False
    stack = []
    # mark = True
    index = -1
    for i in range(len(s)):
        if left(s[i]):
            stack.append(s[i])
            index+=1
        elif index!=-1:
            if match(stack[index],s[i]):
                del stack[index]
                index-=1
            else:
                return False
        else:
            return False
    if index==-1:
        return True
    else:
        return False
    
p="([)]"
print(isValid(p))