class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = dict()
        for char in s:
            hashset[char]=hashset.get(char,0)+1
        for char in t:
            if char not in hashset:
                return False
            hashset[char]=hashset[char]-1
        print(hashset.values())
        return list(hashset.values())==[0]*len(hashset)

        