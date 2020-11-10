class Solution:
    def twoSumLessThanK(self, A, K):
        if not A:
            return -1

        ordered = sorted(A)

        l = 0
        r = len(ordered) - 1
        mx = -1
        while (l < r):
            if ordered[l] >= (K - 1) / 2:
                return mx

            if ordered[l] + ordered[r] >= K or ordered[l] == ordered[r]:
                r -= 1
            else:
                mx = max(mx, ordered[l] + ordered[r])
                l += 1

        return mx

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSumLessThanK([389,998,493,376,474,296,487,515,980,139,934,304,514,329,184,708,918,290,858,967,837,265,829,152,523,341,557,62,13,786,961,424,772,526,446,111,681,860,596,111,35,756,791,866,50,161,951,996,720,146]
,2000))