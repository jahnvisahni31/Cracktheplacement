class Solution:
    def isNumber(self, s: str) -> bool:
        def validate(val, integer=False):
            cnt = Counter(val)
            if integer and cnt['.'] > 0:
                return False
            if cnt['.'] > 1:
                return False
            if '+' in val[1:]:
                return False
            if '-' in val[1:]:
                return False
            hasDigits = False
            for ch in val:
                if ch == '+' or ch == '-' or ch == '.':
                    continue
                if '0' <= ch <= '9':
                    hasDigits = True
                    continue
                return False
            if not hasDigits:
                return False
            return True
        s = s.lower()
        c = Counter(s)

        if c['e'] > 1:
            return False
        
        if c['e'] == 1:
            first, last = s.split('e', 1)
            if len(first) == 0 or len(last) == 0:
                return False
            if not validate(first):
                return False
            if not validate(last, True):
                return False
            return True
        return validate(s)
