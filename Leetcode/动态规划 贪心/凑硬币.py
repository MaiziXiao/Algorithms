def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    coins.sort() #给硬币从小到大排序
    dp = {0:0} #生成字典dp，并且当总金额为0时，最少硬币个数为0
    for i in range(1,amount + 1):
        dp[i] = amount + 1 #因为硬币个数不可能大于amount，所以赋值amount + 1便于比较
        # f(i) = min{f(coin_1), f(coin_2) ...} + 1,  见知乎讲解 https://www.zhihu.com/question/23995189
        for j in coins:
            if j <= i:
                dp[i]=min(dp[i],dp[i-j]+1)
    #for i in range(1,amount + 1):
        #print('dp[%d]:'%(i), dp[i])
    if dp[amount] == amount + 1: #当最小硬币个数为初始值时，代表不存在硬币组合能构成此金额
        return -1
    else:

        return dp[amount]

print(coinChange([1,2,5], 152))