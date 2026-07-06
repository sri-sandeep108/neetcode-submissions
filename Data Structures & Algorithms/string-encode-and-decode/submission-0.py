class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        num = 0
        while (i < len(s)):
            if s[i] == "#":
                i += 1
                decoded.append("".join(s[i:i+num]))
                i += num
                num = 0
            else:
                num *= 10
                num += int(s[i])
                i += 1
        return decoded