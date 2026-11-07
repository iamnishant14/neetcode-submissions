from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    dicts = defaultdict(int)
    for char in s:
        dicts[char]+=1
    return dicts


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    dicts = defaultdict(list)
    for num in nums:
        dicts[num[0]].extend(num[1:])
    return dicts


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
