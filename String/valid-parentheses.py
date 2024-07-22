class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {")": "(", "]": "[","}": "{"}
        st = []
        for c in s:
            if not st:
                st.append(c)
                continue
            if c in p_map and p_map[c] == st[-1]:
                st.pop()
            else:
                st.append(c)
        return False if st else True
      
