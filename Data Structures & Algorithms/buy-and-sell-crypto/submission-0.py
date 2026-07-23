class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = prices[0]
        for r in prices:
            if l > r :
                l = r
            else:
                best = max(r-l, best)
        return best