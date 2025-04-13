# def extract_all_palindromes(s):
#     def expand_around_center(left, right, palindromes):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             palindromes.add(s[left:right+1])  # Add palindrome substring
#             left -= 1
#             right += 1

#     palindromes = set()  # Use a set to store unique palindromes
    
#     for i in range(len(s)):
#         expand_around_center(i, i, palindromes)      # Odd-length palindromes
#         expand_around_center(i, i + 1, palindromes)  # Even-length palindromes
    
#     return sorted(palindromes, key=len, reverse=True)  # Sort by length (longest first)

# # Example Usage
# s = "madaxm"
# print(extract_all_palindromes(s))
# def extract_all_substrings(s):
#     substrings = []
    
#     for i in range(len(s)):  # Start index
#         for j in range(i + 1, len(s) + 1):  # End index (exclusive)
#             substrings.append(s[i:j])  # Extract substring
    
#     return substrings

# # Example Usage
# s = "madaxsm"
# sub = extract_all_substrings(s)
# new =''
# long = ''
# for j in sub:
#     new = s.replace(j,"",1)
#     # print(new)
#     if new == new[::-1] and len(new) > len(long):
#         long = new
# print(long)
    
# def longest_palindrome_after_removal(s):
#     n = len(s)
#     longest = ""

#     for i in range(n):  
#         new_s = s[:i] + s[i+1:]  # Remove the i-th character (O(n))
#         print(new_s)
#         if new_s == new_s[::-1] and len(new_s) > len(longest):  # O(n) palindrome check
#             longest = new_s  # Store the longest palindrome found

#     return longest

# # Example Usage
# s = "madaxsm"
# print(longest_palindrome_after_removal(s))  # Output: "madam"


def longest_palindrome_after_removing_chars(s):
    n = len(s)
    
    # Reverse the string
    rev_s = s[::-1]
    
    # Find the longest common subsequence (LCS) between s and rev_s
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    print(dp)
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rev_s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    # The longest palindromic subsequence length
    lps_length = dp[n][n]

    # We remove characters that are not part of the LPS
    chars_to_remove = n - lps_length  # Min characters to remove

    return dp[n][n], lps_length, chars_to_remove

# Example Usage
s = "xmadaxsm"
text, lps_length, chars_to_remove = longest_palindrome_after_removing_chars(s)
print(f"Longest Palindromic Subsequence Length: {text}")
print(f"Minimum Characters to Remove: {chars_to_remove}")

def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    pal = ""
    
    for i in range(len(s)):
        # Odd length palindrome (single character center)
        found = findpal(s, i, i)
        if len(pal) < len(found):
            pal = found
        
        # Even length palindrome (two character center)
        found = findpal(s, i, i + 1)
        if len(pal) < len(found):
            pal = found
            
    return pal

def findpal(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]  # Return the expanded palindrome substring

# Test Case
print(longestPalindrome("madamx"))  # Output: "madam"

def lengthOfLongestSubstring(s: str) -> int:
    chars = set()
    l, res = 0, 0
        
    for r in range(len(s)):
      while s[r] in chars:
        chars.remove(s[l])
        l += 1
      chars.add(s[r])
      res = max(res, r - l + 1)
      
    return res

print(lengthOfLongestSubstring("madamxx"))

# s = input()
 
def longest_palindromic_substring(s):
    if not s:
        return 0, ""
    
    n = len(s)
    start = 0
    end = 0
    
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    for i in range(n):
        l1, r1 = expand_around_center(i, i)   # Odd length palindromes
        l2, r2 = expand_around_center(i, i + 1) # Even length palindromes
        
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    
    longest_palindrome = s[start:end + 1]
    return len(longest_palindrome), longest_palindrome
 
length, palindrome = longest_palindromic_substring('cracecarx')
print(length)
print(palindrome)
