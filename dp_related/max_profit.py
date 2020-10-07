"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
"""
def maxProfit(prices):
    minprice = float('inf')
    maxprofit = 0
    for price in prices:
        minprice = min(minprice, price)
        maxprofit = max(maxprofit, price - minprice)
    return maxprofit

if __name__ == "__main__":
    price = [7, 1, 5, 3, 6, 4]
    result = maxProfit(price)
    print(result)
