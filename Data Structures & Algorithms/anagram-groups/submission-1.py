class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = dict()
        for words in strs:
            freq = [0]*25
            for char in words:
                freq[ord(char)-97]+=1
            print(freq)
            freq_str = ",".join(str(x) for x in freq)
            if freq_str not in hashes:
                hashes[freq_str]=list()
            hashes[freq_str].append(words)
            print(hashes)
        return hashes.values()
        