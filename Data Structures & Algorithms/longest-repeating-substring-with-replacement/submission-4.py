class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # T: O(n), S: O(1)
        res = 0
        count = {}  # char -> count
        l = 0

        for r, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res
