class Solution:
    def isPalindrome(self, s: str) -> bool:
        start,end = 0,len(s)-1
        while start<end:
            if (ord(s[start])<65 and (ord(s[start])<48 or ord(s[start])>57)) or ord(s[start])>122:
                start+=1
                continue
            if (ord(s[end])<65 and (ord(s[end])<48 or ord(s[end])>57)) or ord(s[end])>122:
                end-=1
                continue
            if s[start].lower()!=s[end].lower():
                return False
            start+=1
            end-=1
        return True