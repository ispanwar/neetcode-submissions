class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        r = 0
        maxlen = 0
        st = set()
        while r<n:
            while s[r] in st:
                st.discard(s[l])
                l += 1
            st.add(s[r])
            maxlen = max(maxlen,len(st))
            r += 1
    
        return maxlen