Ah got it — you're asking for **time and space complexities of search algorithms in Data Structures and Algorithms (DSA)** (like Linear Search, Binary Search, etc.), not AI search strategies. Here's a clean and concise summary:

---

### 🔍 **Search Algorithms in DSA**

| **Algorithm**      | **Time Complexity (Best)** | **Time (Average)** | **Time (Worst)** | **Space Complexity** | **Notes** |
|--------------------|----------------------------|--------------------|------------------|-----------------------|-----------|
| **Linear Search**  | `O(1)`                     | `O(n)`             | `O(n)`           | `O(1)`                | Works on unsorted arrays |
| **Binary Search**  | `O(1)`                     | `O(log n)`         | `O(log n)`       | `O(1)` (Iterative)<br>`O(log n)` (Recursive) | Requires sorted array |
| **Jump Search**    | `O(1)`                     | `O(√n)`            | `O(√n)`          | `O(1)`                | Sorted array |
| **Exponential Search** | `O(1)`                 | `O(log i)`         | `O(log i)`       | `O(1)`                | `i` is position of target. For unbounded/infinite arrays |
| **Interpolation Search** | `O(1)`               | `O(log log n)`     | `O(n)`           | `O(1)`                | Works best with uniformly distributed data |
| **Ternary Search** | `O(1)`                     | `O(log₃ n)`        | `O(log₃ n)`      | `O(1)`                | Like binary, but splits into 3 parts. Needs sorted array |

---

### 🧠 Notes

- `n` = number of elements in the array  
- Binary, Jump, Interpolation, and Ternary searches **require sorted arrays**.
- Linear Search works on **unsorted** or **unordered** data.

---

Let me know if you'd like a visual or want this info applied to linked lists, trees, or graphs too!