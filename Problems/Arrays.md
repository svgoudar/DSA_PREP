
# ✅ Arrays/List

## 🟢 Easy

<details>
  <summary><span style="font-size:19px;"><strong>Two Sum - </strong><a href="https://leetcode.com/problems/two-sum/" target="_blank">#1</a></span></summary>

### 🧾 Input

- `nums`: List of integers (e.g., `[2, 7, 11, 15]`)
- `target`: Integer (e.g., `9`)

    ---

### 📤 Output

- A list of **two indices** `[i, j]` such that:

    ```python
    nums[i] + nums[j] == target
    ```

    ---

### ✅ Example

  ```py
  Input: nums = [2, 7, 11, 15], target = 9  
  Output: [0, 1]

  Explanation: nums[0] + nums[1] = 2 + 7 = 9
  ```

  <details>
      <summary><strong>Solution Code</strong></summary>

  ```py
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            has = {}
            for i, num in enumerate(nums):
                if target - num in has:
                    return has[target - num], i
                has[num] = i
  ```

  </details>

  <details>
        <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n) — single pass through the list, dictionary lookups are O(1) average
- **Space Complexity:** O(n) — dictionary stores at most n elements

    </details>

    </details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Remove Duplicates from Sorted Array - </strong><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/" target="_blank">#26</a></span></summary>

### 🧾 Input

- `nums`: Sorted list of integers (e.g., `[1,1,2]`)

### 📤 Output

- Return the **new length** after removing duplicates **in-place**, with unique elements at the start.

### ✅ Example

  ```py
  Input: nums = [1,1,2]
  Output: 2  
  Modified nums = [1,2,...]

  Explanation: The first two elements after modification are unique.
  ```

  <details>
      <summary><strong>Solution Code</strong></summary>

  ```py
  class Solution:
      def removeDuplicates(self, nums: List[int]) -> int:
          if not nums:
              return 0
          i = 0
          for j in range(1, len(nums)):
              if nums[j] != nums[i]:
                  i += 1
                  nums[i] = nums[j]
          return i + 1
  ```

  </details>

  <details>
        <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n) — single pass
- **Space Complexity:** O(1) — in-place

  </details>

  </details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Best Time to Buy and Sell Stock - </strong><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/" target="_blank">#121</a></span></summary>

### 🧾 Input

- `prices`: List of integers representing the stock price on each day (e.g., `[7,1,5,3,6,4]`)

  ---

### 📤 Output

- Maximum profit possible from a single buy-sell transaction.

  ---

### ✅ Example

  ```py
  Input: prices = [7,1,5,3,6,4]
  Output: 5

  Explanation: Buy on day 2 (price = 1), sell on day 5 (price = 6), profit = 6 - 1 = 5
  ```

  <details>
    <summary><strong>Solution Code</strong></summary>

  ```py
  class Solution:
      def maxProfit(self, prices: List[int]) -> int:
          min_price = float('inf')
          max_profit = 0
          for price in prices:
              if price < min_price:
                  min_price = price
              elif price - min_price > max_profit:
                  max_profit = price - min_price
          return max_profit
  ```

  </details>

  <details>
    <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

  </details>

  </details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Merge Sorted Array - </strong><a href="https://leetcode.com/problems/merge-sorted-array/" target="_blank">#88</a></span></summary>

### 🧾 Input

- `nums1`: First sorted list with extra space (e.g., `[1,2,3,0,0,0]`)
- `m`: Number of valid elements in `nums1`
- `nums2`: Second sorted list (e.g., `[2,5,6]`)
- `n`: Number of elements in `nums2`

---

### 📤 Output

- Merged sorted array in `nums1` in-place.

---

### ✅ Example

```py
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

- The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

<details>
  <summary><strong>Solution Code</strong></summary>

```py
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(m + n)
- **Space Complexity:** O(1)

</details>

</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Move Zeroes - </strong><a href="https://leetcode.com/problems/move-zeroes/" target="_blank">#283</a></span></summary>

### 🧾 Input

- `nums`: List of integers with zeroes (e.g., `[0,1,0,3,12]`)

---

### 📤 Output

- Rearranged list where all 0s are moved to the end, maintaining the order of non-zero elements.

---

### ✅ Example

```py
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

<details>
  <summary><strong>Solution Code</strong></summary>

```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

</details>

</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Valid Mountain Array - </strong><a href="https://leetcode.com/problems/valid-mountain-array/" target="_blank">#941</a></span></summary>

### 🧾 Input

- `arr`: List of integers representing elevation (e.g., `[0,3,2,1]`)

---

### 📤 Output

- Boolean indicating whether it's a valid mountain array.

---

### ✅ Example

```py
Input: arr = [0,3,2,1]
Output: True

Explanation: Strictly increasing then strictly decreasing.
```

<details>
  <summary><strong>Solution Code</strong></summary>

```py
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

</details>

</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Third Maximum Number - </strong><a href="https://leetcode.com/problems/third-maximum-number/" target="_blank">#414</a></span></summary>

### 🧾 Input

- `nums`: List of integers (e.g., `[3,2,1]`)

---

### 📤 Output

- The third distinct maximum number. If it does not exist, return the maximum number.

---

### ✅ Example

```py
Input: nums = [3,2,1]
Output: 1

Explanation: Third distinct max is 1
```

<details>
  <summary><strong>Solution Code</strong></summary>

```py
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = list(set(nums))
        if len(distinct) < 3:
            return max(distinct)
        distinct.sort(reverse=True)
        return distinct[2]
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n log n) due to sorting
- **Space Complexity:** O(n) to store distinct elements

</details>

</details>

---

## 🟡 Medium

---

<details>
  <summary><span style="font-size:19px;"><strong>3Sum - </strong><a href="https://leetcode.com/problems/3sum/" target="_blank">#15</a></span></summary>

### 🧾 Input

- `nums`: List of integers (e.g., `[-1,0,1,2,-1,-4]`)

  ---

### 📤 Output

- All unique triplets `[nums[i], nums[j], nums[k]]` such that they sum to 0.

  ---

### ✅ Example

  ```py
  Input: nums = [-1,0,1,2,-1,-4]
  Output: [[-1,-1,2],[-1,0,1]]
  ```

  <details>
    <summary><strong>Solution Code</strong></summary>

  ```py
  class Solution:
      def threeSum(self, nums: List[int]) -> List[List[int]]:
          nums.sort()
          result = []
          for i in range(len(nums)-2):
              if i > 0 and nums[i] == nums[i-1]:
                  continue
              left, right = i+1, len(nums)-1
              while left < right:
                  total = nums[i] + nums[left] + nums[right]
                  if total < 0:
                      left += 1
                  elif total > 0:
                      right -= 1
                  else:
                      result.append([nums[i], nums[left], nums[right]])
                      while left < right and nums[left] == nums[left+1]:
                          left += 1
                      while left < right and nums[right] == nums[right-1]:
                          right -= 1
                      left += 1
                      right -= 1
          return result
  ```

  </details>

  <details>
    <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1) (excluding output)

  </details>

  </details>

  ---

  <details>
    <summary><span style="font-size:19px;"><strong>Container With Most Water - </strong><a href="https://leetcode.com/problems/container-with-most-water/" target="_blank">#11</a></span></summary>

### 🧾 Input

- `height`: List of non-negative integers representing vertical lines

  ---

### 📤 Output

- Maximum area of water a container can store.

  ---

### ✅ Example

  ```py
  Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
  ```

  ![alt text](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

  <details>
    <summary><strong>Solution Code</strong></summary>

  ```py
  class Solution:
      def maxArea(self, height: List[int]) -> int:
          left, right = 0, len(height) - 1
          max_area = 0
          while left < right:
              width = right - left
              max_area = max(max_area, width * min(height[left], height[right]))
              if height[left] < height[right]:
                  left += 1
              else:
                  right -= 1
          return max_area
  ```

  </details>

  <details>
    <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

  </details>

  </details>

  ---

  <details>
    <summary><span style="font-size:19px;"><strong>Product of Array Except Self - </strong><a href="https://leetcode.com/problems/product-of-array-except-self/" target="_blank">#238</a></span></summary>

### 🧾 Input

- `nums`: List of integers (e.g., `[1,2,3,4]`)

  ---

### 📤 Output

- A list where each element is the product of all other elements except itself.

  ---

### ✅ Example

  ```py
  Input: nums = [1,2,3,4]
  Output: [24,12,8,6]
  ```

  <details>
    <summary><strong>Solution Code</strong></summary>

  ```py
  class Solution:
      def productExceptSelf(self, nums: List[int]) -> List[int]:
          n = len(nums)
          res = [1] * n
          left = 1
          for i in range(n):
              res[i] = left
              left *= nums[i]
          right = 1
          for i in range(n-1, -1, -1):
              res[i] *= right
              right *= nums[i]
          return res
  ```

  </details>

  <details>
    <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) (excluding output)

  </details>

  </details>

  ---

  <details>
    <summary><span style="font-size:19px;"><strong>Set Matrix Zeroes - </strong><a href="https://leetcode.com/problems/set-matrix-zeroes/" target="_blank">#73</a></span></summary>

### 🧾 Input

- `matrix`: 2D list of integers

  ---

### 📤 Output

- Modify matrix in-place to set entire row and column to 0 if an element is 0.

  ---

### ✅ Example

  ```py
  Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
  Output: [[1,0,1],[0,0,0],[1,0,1]]
  ```

  <details>
    <summary><strong>Solution Code</strong></summary>

  ```py
  class Solution:
      def setZeroes(self, matrix: List[List[int]]) -> None:
          rows, cols = len(matrix), len(matrix[0])
          first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
          first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

          for i in range(1, rows):
              for j in range(1, cols):
                  if matrix[i][j] == 0:
                      matrix[i][0] = matrix[0][j] = 0

          for i in range(1, rows):
              for j in range(1, cols):
                  if matrix[i][0] == 0 or matrix[0][j] == 0:
                      matrix[i][j] = 0

          if first_row_has_zero:
              for j in range(cols):
                  matrix[0][j] = 0

          if first_col_has_zero:
              for i in range(rows):
                  matrix[i][0] = 0
  ```

  </details>

  <details>
    <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(1)

  </details>

  </details>

  ---

<details>
  <summary><span style="font-size:19px;"><strong>Subarray Sum Equals K - </strong><a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank">#560</a></span></summary>

### 🧾 Input

- `nums`: List of integers
- `k`: Integer

---

### 📤 Output

- Return the total number of continuous subarrays whose sum equals `k`.

---

### ✅ Example

```py
Input: nums = [1,1,1], k = 2
Output: 2
```

<details>
  <summary><strong>Solution Code</strong></summary>

```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = {0: 1}
        for num in nums:
            current_sum += num
            count += prefix_sums.get(current_sum - k, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        return count
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

</details>

</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Spiral Matrix - </strong><a href="https://leetcode.com/problems/spiral-matrix/" target="_blank">#54</a></span></summary>

### 🧾 Input

- `matrix`: 2D list of integers

---

### 📤 Output

- Return all elements of the matrix in spiral order.

---

### ✅ Example

```py
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

<details>
  <summary><strong>Solution Code</strong></summary>

```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(1) (excluding output)

</details>

</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Sort Colors (Dutch National Flag) - </strong><a href="https://leetcode.com/problems/sort-colors/" target="_blank">#75</a></span></summary>

### 🧾 Input

- `nums`: List of integers with values `0`, `1`, or `2`

---

### 📤 Output

- Sort the array in-place so that elements of the same color are adjacent and in the order `0`, `1`, `2`.

---

### ✅ Example

```py
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

<details>
  <summary><strong>Solution Code</strong></summary>

```py
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

</details>

</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Insert Interval - </strong><a href="https://leetcode.com/problems/insert-interval/" target="_blank">#57</a></span></summary>

### 🧾 Input

- `intervals`: List of intervals sorted by start time
- `newInterval`: Interval to insert

---

### 📤 Output

- Merge `newInterval` and return the new list of intervals.

---

### ✅ Example

```py
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

<details>
  <summary><strong>Solution Code</strong></summary>

```py
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in intervals:
            if i[1] < newInterval[0]:
                res.append(i)
            elif newInterval[1] < i[0]:
                res.append(newInterval)
                newInterval = i
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        res.append(newInterval)
        return res
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

</details>

</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Find All Duplicates in an Array - </strong><a href="https://leetcode.com/problems/find-all-duplicates-in-an-array/" target="_blank">#442</a></span></summary>

### 🧾 Input

- `nums`: List of integers where each integer is in the range `[1, n]` and appears once or twice

---

### 📤 Output

- Return all elements that appear twice.

---

### ✅ Example

```py
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```

<details>
  <summary><strong>Solution Code</strong></summary>

```py
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] *= -1
        return res
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) (excluding output)

</details>

</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Maximum Product Subarray - </strong><a href="https://leetcode.com/problems/maximum-product-subarray/" target="_blank">#152</a></span></summary>

### 🧾 Input

- `nums`: List of integers

---

### 📤 Output

- Return the maximum product of a contiguous subarray.

---

### ✅ Example

```py
Input: nums = [2,3,-2,4]
Output: 6
```

<details>
  <summary><strong>Solution Code</strong></summary>

```py
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1
        for num in nums:
            if num == 0:
                curr_min, curr_max = 1, 1
                continue
            temp = curr_max * num
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(temp, num * curr_min, num)
            res = max(res, curr_max)
        return res
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

</details>

</details>

---

## 🔴 Hard

<details>
  <summary><span style="font-size:19px;"><strong>First Missing Positive - </strong><a href="https://leetcode.com/problems/first-missing-positive/" target="_blank">#41</a></span></summary>

### 🧾 Input

- `nums`: List of integers

### 📤 Output

- Smallest missing positive integer

### ✅ Example

```py
Input: nums = [3, 4, -1, 1]
Output: 2
```

<details>
  <summary><strong>Solution Code</strong></summary>

```python
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
```

</details>

  <details>
  <summary><strong>Complexity Analysis</strong></summary>

  **Time Complexity:** O(n)
  **Space Complexity:** O(1)

</details>
</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Trapping Rain Water - </strong><a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank">#42</a></span></summary>

### 🧾 Input

- `height`: List of non-negative integers

### 📤 Output

- Total amount of trapped water

### ✅ Example

```py
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

<details>
  <summary><strong>Solution Code</strong></summary>

```python
class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

</details>
</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Sliding Window Maximum - </strong><a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank">#239</a></span></summary>

### 🧾 Input

- `nums`: List of integers
- `k`: Size of the window

### 📤 Output

- Maximum of each sliding window

### ✅ Example

```py
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

<details>
  <summary><strong>Solution Code</strong></summary>

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        res = []
        for i in range(len(nums)):
            while q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
```

</details>
<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n)
- **Space Complexity:** O(k)

</details>
</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Merge k Sorted Arrays</strong> (Variation of <a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank">#23</a>)</span></summary>

### 🧾 Input

- `arrays`: List of k sorted arrays

### 📤 Output

- Single merged sorted array

### ✅ Example

```py
Input: arrays = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

<details>
  <summary><strong>Solution Code</strong></summary>

```python
import heapq

class Solution:
    def mergeKArrays(self, arrays):
        heap = []
        for i, arr in enumerate(arrays):
            if arr:
                heapq.heappush(heap, (arr[0], i, 0))
        res = []
        while heap:
            val, list_idx, element_idx = heapq.heappop(heap)
            res.append(val)
            if element_idx + 1 < len(arrays[list_idx]):
                next_tuple = (arrays[list_idx][element_idx + 1], list_idx, element_idx + 1)
                heapq.heappush(heap, next_tuple)
        return res
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(N log k)
- **Space Complexity:** O(k)
  *(N = total number of elements)*

</details>
</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Minimum Number of Swaps to Sort</strong> (Common Interview Question)</span></summary>

### 🧾 Input

- `arr`: List of integers

### 📤 Output

- Minimum number of swaps to sort

### ✅ Example

```py
Input: arr = [4, 3, 2, 1]
Output: 2
```

<details>
  <summary><strong>Solution Code</strong></summary>

```python
class Solution:
    def minSwaps(self, arr):
        n = len(arr)
        arrpos = list(enumerate(arr))
        arrpos.sort(key=lambda it: it[1])
        vis = [False] * n
        ans = 0
        for i in range(n):
            if vis[i] or arrpos[i][0] == i:
                continue
            cycle_size = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = arrpos[j][0]
                cycle_size += 1
            if cycle_size > 0:
                ans += cycle_size - 1
        return ans
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

</details>
</details>

---

<details>
  <summary><span style="font-size:19px;"><strong>Maximum Gap - </strong><a href="https://leetcode.com/problems/maximum-gap/" target="_blank">#164</a></span></summary>

### 🧾 Input

- `nums`: List of integers

### 📤 Output

- Maximum difference between successive elements after sorting

### ✅ Example

```py
Input: nums = [3,6,9,1]
Output: 3
```

<details>
  <summary><strong>Solution Code</strong></summary>

```python
class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])
        return max_gap
```

</details>

<details>
  <summary><strong>Complexity Analysis</strong></summary>

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1)

</details>
</details>

---
