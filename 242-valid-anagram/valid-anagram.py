class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        one, two = {}, {}

        for letter in s:
            if letter in one:
                one[letter] += 1
            else:
                one[letter] = 1

        for letter in t:
            if letter in two:
                two[letter] += 1
            else:
                two[letter] = 1

        return one == two