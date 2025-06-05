#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums [i -1]:
                nums.pop()
                nums.append("_")
            else:
                i +=1
        return nums

        
# @lc code=end

