class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []

        for i in freq[::-1]:
            for s in i:
                res.append(s)
                if len(res) == k:
                    return res