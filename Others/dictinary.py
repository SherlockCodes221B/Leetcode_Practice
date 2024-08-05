'''
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 

'''


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr = [i for i in arr if arr.count(i) == 1]
        return "" if k > len(arr) else arr[k - 1]