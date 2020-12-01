class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = len(words), len(words)

        ans = len(words) - 1
        condition_flag = False
        for i, word in enumerate(words):

            if word == word1:
                idx1 = i
                ans = min(ans, abs(idx1 - idx2))
            elif word == word2:
                idx2 = i
                ans = min(ans, abs(idx1 - idx2))

        return ans