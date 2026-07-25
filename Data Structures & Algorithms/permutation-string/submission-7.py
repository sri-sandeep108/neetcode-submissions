class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = {}
        for c in s1:
            need[c] = need.get(c,0) +1
        window = {}
        wlen = len(s1)
        for r in range(len(s2)):
            c = s2[r]
            window[c] = window.get(c, 0) + 1
            l = r - wlen + 1
            if l > 0:
                temp = s2[l-1]
                window[temp] -= 1
                if window[temp] == 0:
                    del window[temp]
            if l >= 0 and window == need:
                return True
        return False    