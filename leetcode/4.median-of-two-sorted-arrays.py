#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = sorted(nums1 + nums2)
        if len(final) % 2 != 0:
            return final[(len(final) - 1) // 2]
        else:
            return (final[len(final) // 2] + final[(len(final) // 2) - 1]) / 2


# @lc code=end
