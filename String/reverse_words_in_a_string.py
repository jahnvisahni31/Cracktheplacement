class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = ' '.join(s.split())
        words = s.split()
        reversed_words = words[::-1]
        result = ' '.join(reversed_words)
        return result
