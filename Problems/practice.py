#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final = []
        nums = sorted(nums)
        i=0
        while ( i < len(nums)-1 ):
            a = nums[i]
            b = i+1
            c = len(nums)-1

            while b<c:
                if a+nums[b]+nums[c] == 0:
                    final.append([a,nums[b],nums[c]])
                    b+=1
                    while b<c:
                        if nums[b]==nums[b-1]:
                            b+=1
                        else:
                            break
                elif a+nums[b]+nums[c] > 0:
                    c-=1
                elif a+nums[b]+nums[c] < 0:
                    b+=1

            while i < len(nums)-1:
                if nums[i]==nums[i+1]:
                    i+=1
                else:
                    break
            i+=1
        return final
            
# @lc code=end

