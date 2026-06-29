class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.replace(" ","").lower()
        s2=""
        for i in s1:
            if i.isalnum():
                s2+=i
        if s2[::] == s2[::-1]:
            return True
        return False