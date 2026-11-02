class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start,end =0,0
        count = {}
        max_f,result = 0,0
        while end<len(s):
            count[s[end]] = count.get(s[end],0)+1
            max_f = max(max_f,count[s[end]])
            
            while (end-start+1) - max_f > k:
                count[s[start]] -= 1
                start += 1
            
            result = max(result,end-start+1)
            end+=1
        return result