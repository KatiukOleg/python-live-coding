from collections import Counter

def reverse_string(string: str) -> str:
    """
    Reverse the entire string.
    
    :param string: Description
    :type string: str

    Complexity:
        - Time: 0(n)
        - Space: 0(n) for new string
    """
    return string[::-1]

def reverse_words(sentence: str) -> str:
    """
    Reverse order of words in a sentence.
    
    Clarify:
        - Words are separeted by whitespace.

    Approach:
        - Split into words, reverse list, join with single spaces.    

    Complexity:
        - Time: 0(n)
        - Space: 0(n) for new string
    """
    words = sentence.split()
    return " ".join(reversed(words))    

def is_palindrome(string: str) -> bool:
    """
    Check if string is a palindrome ignoring spaces and case.
    
    Clarify:
        - Ignore spaces and case.

    Approach:
        - Normalize -> compare with reversed.    

    Complexity:
        - Time: 0(n)
        - Space: 0(n)
    """
    normalized = string.lower().replace(" ", "")
    return normalized == normalized[::-1]

def first_unique_char(string: str) -> int:
    """
    Return the index of the first non-repeating character in string.
    If none exists, return -1.
    
    Clarify:
        - Return index from original string.
        - Empty string -> -1

    Approach:
        - Count chars, then scan for first count == 1.    

    Complexity:
        - Time: 0(n)
        - Space: 0(k)
    """
    if not string:
        return -1

    counts = Counter(string)
    print(counts)
    
    for i, ch in enumerate(string):
        print(i, ch)
        if counts[ch] == 1:
            return i
    return -1 


if __name__ == "__main__":
    print(first_unique_char("loveleetcode"))