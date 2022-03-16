"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List

def reverseString(s: List[str]) -> None:
    low = 0
    high = len(s) - 1
        
    while low <= high:
        l_elm = s[low]
        h_elm = s[high]
            
        s[low] = h_elm
        s[high] = l_elm
            
        low += 1
        high -=1
    
    return s

if __name__ == "__main__":
    str_to_reverse = list('grag tnahsarp')
    print(reverseString(str_to_reverse))