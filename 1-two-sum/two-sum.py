class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {} # {num: index}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in visited:
                return [i, visited[diff]]
            visited[nums[i]] = i