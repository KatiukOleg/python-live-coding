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