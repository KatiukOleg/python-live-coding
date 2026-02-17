from collections import Counter
from typing import Any  

def remove_duplicates_preserve_order(nums: list[int]) -> list[int]:
    """
    Remove duplicates while preserving first-seen order
    """
    raw: set[int] = set()
    filtered: list[int] = []
    for n in nums:
        if n not in raw:
            raw.add(n)
            filtered.append(n)
    return filtered

def find_min_max(nums: list[int]) -> tuple[int, int]:
    """
    Return (min, max) without using min()/max().

    Clarify:
        - if list is empty, raise ValueError
    """
    if not nums:
        raise ValueError("nums must not be empty")

    mn = mx = nums[0]
    for n in nums[1:]:
        if n < mn:
            mn = n
        if n > mx:
            mx = n
    return mn, mx