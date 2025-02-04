class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter

        counter = Counter(arr1)
        res = []

        for num in arr2:
            res.extend([num] * counter.pop(num,0))
        
        res.extend(sorted(counter.elements()))
        
        return res