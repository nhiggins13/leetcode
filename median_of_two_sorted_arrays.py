from math import inf


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        low = 0
        high = len(nums1)

        half = (len(nums1) + len(nums2) + 1) // 2

        while (high >= low):
            part_x = (high + low) // 2

            part_y = half - part_x

            x_left_max = -inf if part_x == 0 else nums1[part_x - 1]
            x_right_min = inf if part_x >= len(nums1) else nums1[part_x]

            y_left_max = -inf if part_y == 0 else nums2[part_y - 1]
            y_right_min = inf if part_y >= len(nums2) else nums2[part_y]

            if x_left_max <= y_right_min and y_left_max <= x_right_min:
                if (len(nums1) + len(nums2)) % 2:
                    return max(x_left_max, y_left_max)
                else:
                    return (max(x_left_max, y_left_max) + min(x_right_min, y_right_min)) / 2
            elif x_left_max > y_right_min:
                high = part_x - 1
            else:
                low = part_x + 1