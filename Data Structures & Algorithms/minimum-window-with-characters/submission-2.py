import copy
class Solution:
    def isValid(self,s,freq, start , end):
        if start == -1: return False, -1
        current_freq = copy.deepcopy(freq)
        for index in range(start,end+1):
            if s[index] in current_freq:
                current_freq[s[index]]-=1
                if current_freq[s[index]] <=0:
                    del current_freq[s[index]]
        if len(current_freq)==0:
            return True,end-start+1
        return False,-1
    

    def shrinkWindow(self,s,freq,start,end, min_sub_len, min_sub):
        while start<=end:
            valid, valid_len = self.isValid(s,freq,start,end)
            if valid:
                if valid_len < min_sub_len:
                    min_sub_len = valid_len
                    min_sub = s[start:end+1]
                start+=1
            else:
                break
        return min_sub,min_sub_len,start

    def minWindow(self, s: str, t: str) -> str:
        start,end = -1,0
        freq = dict()
        for char in t:
            freq[char]= freq.get(char,0)+1
        current_freq = copy.deepcopy(freq)
        size = len(s)
        min_sub_len = sys.maxsize
        min_sub = ""
        while end<size:
            if s[end] in freq and start==-1:
                start = end
            
            valid_window, valid_window_size = self.isValid(s,current_freq,start,end)
            if valid_window:
                min_sub, min_sub_len, start = self.shrinkWindow(s, current_freq, start, end, min_sub_len, min_sub)
            end+=1
        return min_sub