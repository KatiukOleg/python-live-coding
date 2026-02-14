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



if __name__ == "__main__":
    print(reverse_words("Hello World!"))