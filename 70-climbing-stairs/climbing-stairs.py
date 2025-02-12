class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2 = 1, 1

        for i in range(n-1):
            tmp = step1
            step1 = step1+step2
            step2 = tmp

        return step1