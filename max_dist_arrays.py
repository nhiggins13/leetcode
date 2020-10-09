class Solution:
    def maxDistance(self, arrays):
        mx = arrays[0][-1]
        mn = arrays[0][0]
        dist = 2**-32

        for i in range(1, len(arrays)):
            curr_mx = arrays[i][-1]
            curr_mn = arrays[i][0]

            dist = max(max(dist, abs(mx - curr_mn)), abs(curr_mx - mn))

            mx = max(mx, curr_mx)
            mn = min(mn, curr_mn)

        return dist


if __name__ == "__main__":
    input = [[1,2,3],[4,5],[1,2,3]]
    s = Solution()
    print(s.maxDistance(input))
