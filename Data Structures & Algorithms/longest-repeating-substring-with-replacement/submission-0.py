class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # T: O(n), S: O(1)
        char_count = {} # char -> count
        res, l, max_freq = 0, 0, 0
        
        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            max_freq = max(max_freq, char_count[s[r]])

            while (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res