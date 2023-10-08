class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 输入数组和一个数
        # 输出移除与输入数值相同后的数组长度
        i=0
        j=0
        temp=0
        count = 0
        while(i<len(nums)):
            if nums[i]==val:
                j=i
                count+=1
                while(j<len(nums)-1):
                    nums[j]=nums[j+1]
                    j+=1
            i+=1
        return len(nums)-count
             labels = [
            [0,0],
            [0,0],
            [0,0]
        ]
        length = len(s)
        i=0
        while(i<length):
            if s[i]=='(':
                labels[0][0]+=1
            if s[i]==')':
                labels[0][1]+=1
            if s[i]=='{':
                labels[1][0]+=1
            if s[i]=='}':
                labels[1][1]+=1
            if s[i]=='[':
                labels[2][0]+=1
            if s[i]==']':
                labels[2][1]+=1
            i+=1
        if (labels[0][0]==labels[0][1] && labels[1][0]==labels[1][1] &&labels[2][0]==labels[2][1]) :