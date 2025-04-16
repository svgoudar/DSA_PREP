#https://leetcode.com/problems/two-sum/description/


nums =[2,7,11,15]
target = 9

def two_sums(arr,target):
    n = len(arr)
    count_nums = {}
    for i in range(n):
        diff = target - arr[i]
        if diff in count_nums:
            return [count_nums[diff],i]
        count_nums[arr[i]] = i
    return
        
        
print(two_sums(nums,target))
