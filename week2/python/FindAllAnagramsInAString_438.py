class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return list()
        
        dictionary = dict()
        for char in p:
            dictionary[char] = 1 if char not in dictionary else 1+dictionary[char]
            
        count=len(p)
        start= 0
        ans=list()
        for index,char in enumerate(s):
            if start>len(s)-len(p):
                break
            if char in dictionary:
                while dictionary[char]==0:
                    dictionary[s[start]]+=1
                    start+=1
                    count+=1
                        
                dictionary[char]-=1
                count-=1
                if count==0:
                    ans.append(start)
                    
            else:
                while start<index:
                    dictionary[s[start]]+=1
                    start+=1
                    count+=1
                start+=1
                
        return ans
