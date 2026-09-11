class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T: O(m * n), S: O(m)
        res = defaultdict(list)  # 10010... -> list of anagrams

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())
