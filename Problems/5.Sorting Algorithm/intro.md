Here's a handy breakdown of the most popular **sorting algorithms in DSA** along with their **time and space complexities**:

---

## 📊 Sorting Algorithms – Time & Space Complexities

| Algorithm            | Best Time     | Average Time  | Worst Time    | Space       | Stable?   | Notes                             |
|----------------------|---------------|----------------|----------------|-------------|-----------|------------------------------------|
| **Bubble Sort**      | O(n)          | O(n²)          | O(n²)          | O(1)        | ✅ Yes     | Good for small data / educational |
| **Selection Sort**   | O(n²)         | O(n²)          | O(n²)          | O(1)        | ❌ No      | Always does n² comparisons        |
| **Insertion Sort**   | O(n)          | O(n²)          | O(n²)          | O(1)        | ✅ Yes     | Efficient for nearly sorted lists |
| **Merge Sort**       | O(n log n)    | O(n log n)     | O(n log n)     | O(n)        | ✅ Yes     | Divide & conquer, uses recursion  |
| **Quick Sort**       | O(n log n)    | O(n log n)     | O(n²)          | O(log n)*   | ❌ No      | In-place, fastest on avg          |
| **Heap Sort**        | O(n log n)    | O(n log n)     | O(n log n)     | O(1)        | ❌ No      | Uses binary heap                  |
| **Counting Sort**    | O(n + k)      | O(n + k)       | O(n + k)       | O(k)        | ✅ Yes     | Only works for integers in range  |
| **Radix Sort**       | O(nk)         | O(nk)          | O(nk)          | O(n + k)    | ✅ Yes     | Non-comparative, for integers     |
| **Bucket Sort**      | O(n + k)      | O(n + k)       | O(n²)          | O(n + k)    | ✅ Yes     | Good for uniformly distributed    |
| **Tim Sort**         | O(n)          | O(n log n)     | O(n log n)     | O(n)        | ✅ Yes     | Python's built-in sort algorithm  |

> 🧠 **Notes:**
- `k` in Counting/Radix/Bucket Sort = Range or number of digits/buckets.
- Quick Sort’s worst case is **O(n²)** when pivot selection is poor (e.g., already sorted array).
- Tim Sort is a hybrid of **merge + insertion sort**, used in Python and Java.

---

## ✅ Stability in Sorting:
A **stable sort** maintains the relative order of equal elements.

| Stable Sorts          | Unstable Sorts         |
|-----------------------|------------------------|
| Merge Sort            | Quick Sort             |
| Bubble Sort           | Selection Sort         |
| Insertion Sort        | Heap Sort              |
| Counting, Radix, Bucket |                      |

---

### 🔧 Which to use when?

- **Small / nearly sorted arrays**: Insertion Sort
- **General purpose**: Merge Sort or Quick Sort
- **Real-world language sorting (Python, Java)**: Tim Sort
- **Non-comparative (integer-only)**: Counting, Radix, Bucket

---

Want me to show visual comparisons or give you Python implementations for each of these?