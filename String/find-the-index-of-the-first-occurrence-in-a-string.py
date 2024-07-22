class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        mat = re.finditer(needle, haystack)
        po = [m.start() for m in mat]
        fi = po[0] if po else -1
        return fi
