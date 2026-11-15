class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        start1,start2=0,0
        out = list()
        while start1<len(word1) and start2<len(word2):
            out.append(word1[start1])
            out.append(word2[start2])
            start1+=1
            start2+=1
        while start1<len(word1):
            out.append(word1[start1])
            start1+=1
        while start2<len(word2):
            out.append(word2[start2])
            start2+=1
        return "".join(out)