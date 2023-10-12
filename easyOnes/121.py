from typing import Optional,List
def maxProfit( prices: List[int]) -> int:
    # max=0
    # for i in range(len(prices)):
    #     for j in range(i+1,len(prices)):
    #         if (prices[j] - prices[i]) > max:
    #             max = prices[j] - prices[i]
    # return max

    # 找到顺序的最大值与最小值
    # 先找最小值，再在最小值索引到结束的数组中找最大值;再找个最大值，然后往前找最小值；对比这两者的大小
    if len(prices)<=1:
        return 0
    max = prices[0]
    min = 10**5 + 1
    min_index = -1
    max_index = -1
    res1 = 0
    res2 = 0
    for i in range(len(prices)):
        if min>prices[i]:
            min = prices[i]
            min_index = i
        if max<prices[i]:
            max = prices[i]
            max_index = i
    for j in range(min_index+1,len(prices)):
        if res1 < (prices[j]-min):
            res1=prices[j]-min
    for j in range(0,max_index):
        if res2 < (max-prices[j]):
            res2=max-prices[j]
    if res1>res2:
        return res1
    else:
        return res2

maxProfit([2,4,1])