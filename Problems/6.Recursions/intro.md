Great — let’s dive into the **time and space complexity of recursion** in DSA. Understanding complexity helps you know how efficient (or inefficient 😅) your recursive solution is.

---

## ⏱️ **Time Complexity of Recursion**

To find time complexity of a recursive function:

1. **Write the recurrence relation.**
2. **Solve it using**:
   - Recursion Tree
   - Master Theorem
   - Iterative method (sometimes)

---

### 🔁 Example 1: Factorial
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

- **Recurrence relation**: T(n) = T(n-1) + O(1)
- **Time complexity**: **O(n)**

---

### 🔁 Example 2: Fibonacci (Naive Recursion)
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

- **Recurrence relation**: T(n) = T(n-1) + T(n-2) + O(1)
- **Time complexity**: **O(2^n)** (Exponential 😬)

> Can be optimized to O(n) using **memoization** or **bottom-up DP**.

---

### 🔁 Example 3: Merge Sort
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

- **Recurrence relation**: T(n) = 2T(n/2) + O(n)
- Use **Master Theorem**:
  - a = 2, b = 2, f(n) = O(n) → Case 2
- **Time complexity**: **O(n log n)**

---

## 🧠 Master Theorem (Quick Ref)

For T(n) = aT(n/b) + f(n)

| Case | If f(n) is... | Then T(n) is... |
|------|---------------|-----------------|
| Case 1 | f(n) = O(n^log_b(a) - ε) | O(n^log_b(a)) |
| Case 2 | f(n) = Θ(n^log_b(a))     | O(n^log_b(a) * log n) |
| Case 3 | f(n) = Ω(n^log_b(a) + ε) | O(f(n)) (if regularity condition holds) |

---

## 🧮 Space Complexity of Recursion

Space is consumed on the **call stack**.

### General Rule:
- If your function goes **n levels deep**, it takes **O(n)** space on the stack.

### Examples:
| Function      | Recursive Depth | Space Complexity |
|---------------|-----------------|------------------|
| Factorial     | O(n)            | O(n)             |
| Fibonacci     | O(n)            | O(n)             |
| Merge Sort    | O(log n)        | O(log n)         |
| Tree Traversal| O(h)            | O(h) (`h` = height of tree) |

---

## 📌 TL;DR

| Example         | Time Complexity | Space Complexity |
|----------------|------------------|------------------|
| Factorial       | O(n)             | O(n)             |
| Fibonacci (naive)| O(2^n)          | O(n)             |
| Fibonacci (DP)  | O(n)             | O(n)             |
| Merge Sort      | O(n log n)       | O(log n)         |
| DFS (Tree/Graph)| O(n)             | O(h) or O(n)     |

---

Want help calculating time complexity for a custom recursive function? Drop the code!