"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s: str) -> int:
    left, right = 0, 0
    max_length = 0
    seen = {}
    while right<=len(s)-1:
        elm = s[right]
        if elm in seen and seen[elm]>=left:
            left = seen[elm] + 1
        else:
            length = (right - left) + 1
            max_length = max(max_length, length)
        seen[elm] = right
        right+=1
    return max_length


if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcdefgh") == 8
    assert lengthOfLongestSubstring("abcabshh") == 5