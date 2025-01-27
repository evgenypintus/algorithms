class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        cur_max = 0

        buy = 0
        sell = 1

        while sell < len(prices):
            max = prices[sell] - prices[buy]

            if prices[sell] > prices[buy]:
                if max > cur_max:
                    cur_max = max
            else:
                buy = sell

            sell += 1

        return cur_max


if __name__ == '__main__':
    s = Solution()
    prices = [7,1,5,3,6,4]

    print(s.maxProfit(prices))