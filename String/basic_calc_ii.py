class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace('-', '+-')
        items = s.split('+') 

        for index, word in enumerate(items):
            nums = []
            curr = ""
            for c in word:
                if c == '*':
                    nums.append(curr.strip())
                    nums.append(c)
                    curr = ""
                elif c == '/':
                    nums.append(curr.strip())
                    nums.append(c)
                    curr = ""
                else:
                    curr += c
            nums.append(curr.strip())

            if len(nums) > 1:
                p = int(nums[0])
                i = 1
                while i < len(nums):
                    oper = nums[i]
                    p2 = int(nums[i+1])
                    if oper == '*':
                        p = p * p2
                    else:
                        p = math.trunc(p / p2)
                    i += 2
                items[index] = str(p)

        finalsum = 0
        for prod in items:
            finalsum += int(prod)

        return finalsum
