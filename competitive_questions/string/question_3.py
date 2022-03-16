"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
"""

def reverseWords(s: str) -> str:

    ## Method 1
    # words = s.split(" ")
    # result = ""
    # for word in words:
    #     word = word[::-1]
    #     if not result:
    #         result = word
    #         continue
    #     result = result +" "+ word
    # return result

    return " ".join([word[::-1] for word in s.split(" ")])

if __name__=='__main__':
    print(reverseWords("Let's take LeetCode contest"))
    assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"