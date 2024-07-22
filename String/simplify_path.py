class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        st = deque()
        for f in p:
            if f == "." or f == "":
                continue
            elif f == "..":
                if st:
                    st.pop()
            else:
                st.append(f)
        return "/" + "/".join(st)
