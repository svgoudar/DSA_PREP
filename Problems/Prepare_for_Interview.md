Great — here's a **refined list of top LeetCode problems focused only on Lists/Arrays** (no trees, graphs, or strings) that are **frequently asked in top companies like Amazon, Google, Microsoft, etc.**:

---

## ✅ **Top LeetCode Array/List Problems (All Levels)**

## Arrays

<details>
  <summary>
    <span style="font-size: 18px; font-weight: bold; "> Easy
    </span>
  </summary>
<details>
<summary>
<span style="font-size: 18px; font-weight: bold;"> Two Sum – <a href="https://leetcode.com/problems/two-sum/" target="_blank">#1</a>
</span>
</summary>

### 🧾 Input

- `nums`: List of integers (e.g., `[2, 7, 11, 15]`)
- `target`: Integer value (e.g., `9`)

---

### 📤 Output

- A list of **two indices** from `nums` such that:

  ```python
  nums[index1] + nums[index2] == target
  ```

---

### ✅ Example

```py
Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]

Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

<details>
<summary><strong>Click here to see solution</strong></summary>

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i, num in enumerate(nums):
            if target - num in has:
                return has[target - num],i
            has[num] = i
```

</details>

<details>
<summary><strong>Expand to understand complexity of the given solution<br></summary>

## ✅ Time Complexity: **O(n)**

- The code iterates through the list **once** using `enumerate(nums)` → **O(n)** time.
- Each dictionary operation (`in`, `get`, and assignment) is **O(1)** on average.
- So for **n elements**, the total time is **O(n)**.

---

## ✅ Space Complexity: **O(n)**

- The `has` dictionary stores at most one entry per element in `nums`.
- In the worst case (when no match is found until the end), it stores **n** elements → **O(n)** space.

---
    </details>
        </details>

### 2. **Remove Duplicates from Sorted Array** – [#26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

3. **Best Time to Buy and Sell Stock** – [#121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
4. **Merge Sorted Array** – [#88](https://leetcode.com/problems/merge-sorted-array/)
5. **Move Zeroes** – [#283](https://leetcode.com/problems/move-zeroes/)
6. **Valid Mountain Array** – [#941](https://leetcode.com/problems/valid-mountain-array/)
7. **Third Maximum Number** – [#414](https://leetcode.com/problems/third-maximum-number/)

---

### 🟡 Medium

1. **3Sum** – [#15](https://leetcode.com/problems/3sum/)
2. **Container With Most Water** – [#11](https://leetcode.com/problems/container-with-most-water/)
3. **Product of Array Except Self** – [#238](https://leetcode.com/problems/product-of-array-except-self/)
4. **Set Matrix Zeroes** – [#73](https://leetcode.com/problems/set-matrix-zeroes/)
5. **Subarray Sum Equals K** – [#560](https://leetcode.com/problems/subarray-sum-equals-k/)
6. **Spiral Matrix** – [#54](https://leetcode.com/problems/spiral-matrix/)
7. **Sort Colors (Dutch National Flag)** – [#75](https://leetcode.com/problems/sort-colors/)
8. **Insert Interval** – [#57](https://leetcode.com/problems/insert-interval/)
9. **Find All Duplicates in an Array** – [#442](https://leetcode.com/problems/find-all-duplicates-in-an-array/)
10. **Maximum Product Subarray** – [#152](https://leetcode.com/problems/maximum-product-subarray/)

---

### 🔴 Hard

1. **First Missing Positive** – [#41](https://leetcode.com/problems/first-missing-positive/)
2. **Trapping Rain Water** – [#42](https://leetcode.com/problems/trapping-rain-water/)
3. **Sliding Window Maximum** – [#239](https://leetcode.com/problems/sliding-window-maximum/)
4. **Merge k Sorted Arrays** (variation of #23) – \[custom implement with min heap]
5. **Minimum Number of Swaps to Sort** – \[Not on LeetCode, but often asked in interviews]
6. **Maximum Gap** – [#164](https://leetcode.com/problems/maximum-gap/) (uses bucket sort)

---

### 🧠 Bonus: Classic Patterns in Array Problems

| Pattern               | Example Problems                                |
| --------------------- | ----------------------------------------------- |
| Two pointers          | Two Sum, Move Zeroes, Container With Most Water |
| Sliding window        | Maximum Subarray, Sliding Window Maximum        |
| Sorting + logic       | 3Sum, Merge Intervals                           |
| Prefix sums           | Subarray Sum Equals K                           |
| Greedy                | Best Time to Buy and Sell Stock                 |
| In-place manipulation | Set Matrix Zeroes, Sort Colors                  |
| Heap                  | Merge k Sorted Arrays, Sliding Window Maximum   |

---

Would you like this list broken down into a **15-day practice plan** or get **PDF/CSV format**?
