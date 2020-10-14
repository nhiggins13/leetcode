def maxSubArray(self, nums: List[int]) -> int:
    mx = nums[0]
    curr = nums[0]

    for i in range(1, len(nums)):
        curr = max(curr + nums[i], nums[i])
        mx = max(curr, mx)

    return mx