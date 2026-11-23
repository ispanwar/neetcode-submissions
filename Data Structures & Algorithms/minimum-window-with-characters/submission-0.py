class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)
        window = {}
        
        have, required = 0, len(need)
        res_len = float("inf")
        res_start = 0
        left = 0

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            # Shrink window from the left while it remains valid
            while have == required:
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res_start = left

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1

        return "" if res_len == float("inf") else s[res_start : res_start + res_len]