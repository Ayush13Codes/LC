class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # T: O(n), S: O(1)
        if t == "":
            return ""

        need = {}  # char -> count
        for c in t:
            need[c] = 1 + need.get(c, 0)

        window = {}
        have = 0
        req = len(need)

        res = [-1, -1]
        res_len = float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in need and window[c] == need[c]:
                have += 1

            while have == req:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                l_c = s[l]
                window[l_c] -= 1
                if l_c in need and window[l_c] < need[l_c]:
                    have -= 1
                l += 1

        l, r = res

        return "" if res_len == float("inf") else s[l : r + 1]
