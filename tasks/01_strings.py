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


if __name__ == "__main__":
    print(reverse_string("Hello World!"))