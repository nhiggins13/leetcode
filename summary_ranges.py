class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return

        start = nums[0]
        curr_index = 0
        results = []

        while (curr_index < len(nums) - 1):
            curr = nums[curr_index]
            nxt = nums[curr_index + 1]

            if nxt != curr + 1:
                if curr == start:
                    results.append(str(start))
                    start = nxt
                else:
                    results.append("%d->%d" % (start, curr))
                    start = nxt

            curr_index += 1

        if start == nums[-1]:
            results.append(str(start))

        else:
            results.append("%d->%d" % (start, nums[-1]))

        return results