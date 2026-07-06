class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            sorted_str = str(sorted(s))
            if sorted_str in hmap:
                hmap[sorted_str].append(s)
            else:
                hmap[sorted_str] = [s]
        return list(hmap.values())
