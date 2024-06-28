'''
Unique Number of Occurrences

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.



'''


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        setarr = {}
        res = True
        for x in arr:
            setarr[x] = arr.count(x)
        y = list(setarr.values())
        for i in y:
            if y.count(i) > 1:
                res = False
                break

        return res
