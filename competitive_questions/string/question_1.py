"""
Given a string, find the most common character in the string
"""

from collections import defaultdict

def find_most_common_character(input_word: str) -> str:
    
    counter = defaultdict(int)
    max_count = 0
    most_occuring_char = None
    for i in range(len(input_word)):
        char_ord = ord(input_word[i])
        if (char_ord >= 65 and char_ord <=90) or (char_ord >= 97 and char_ord <=122):
            counter[input_word[i]]+=1
    for k, v in counter.items():
        if v > max_count:
            most_occuring_char = k
            max_count = v
    return most_occuring_char

    # another method discussed at: https://www.geeksforgeeks.org/return-maximum-occurring-character-in-the-input-string/


if __name__=='__main__':
    name = "Prashant Garg"
    most_occuring_char = find_most_common_character(name)
    print(f"Most occuring element in '{name}' is '{most_occuring_char}'")