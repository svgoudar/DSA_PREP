#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start,end = 0,len(nums) -1
        result = -1
        while start <= end:
            mid = (start + end) // 2 
            if nums[mid] == target:
                result = mid
            elif nums[mid] > nums[end]:
                start = mid +1
            else:
                end = mid -1
        return result
            

# @lc code=end

