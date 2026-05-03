class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        visited = {} # {num: index}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visited:
                return [i, visited[diff]]
            else:
                visited[nums[i]] = i
        return []