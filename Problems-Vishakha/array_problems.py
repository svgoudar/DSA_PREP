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

#using two pointer technique:

def two_sums(arr,target):

    left, right = 0,len(arr)-1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return True
        elif sum > target:
            right -=1
        else:
            left +=1
            
    return False
        
    

#Remove duplicates in place-> two pointer technique
#https://leetcode.com/problems/remove-duplicates-from-sorted-array

arr = [0,0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    i = 0
    
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i += 1
            arr[i] = arr[j]
    return i+1
      
print(removeDuplicates(arr))
