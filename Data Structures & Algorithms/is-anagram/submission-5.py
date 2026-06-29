class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter -> Python's collections module that counts how many times each element appears in an iterable
        return Counter(s) == Counter(t)