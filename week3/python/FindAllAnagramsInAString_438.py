class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return list()
        
        # 1st approach with multiset
#         dictionary = dict()
#         for char in p:
#             dictionary[char] = 1 if char not in dictionary else 1+dictionary[char]
            
#         count=len(p)
#         start= 0
#         ans=list()
#         for index,char in enumerate(s):
#             if start>len(s)-len(p):
#                 break
#             if char in dictionary:
#                 while dictionary[char]==0:
#                     dictionary[s[start]]+=1
#                     start+=1
#                     count+=1
                        
#                 dictionary[char]-=1
#                 count-=1
#                 if count==0:
#                     ans.append(start)
                    
#             else:
#                 while start<index:
#                     dictionary[s[start]]+=1
#                     start+=1
#                     count+=1
#                 start+=1
                
#         return ans
        
        # 2nd approach with sorting
        def findIndex(s: str, char: chr) -> int:
            l,r = 0, len(s) - 1
            while l<r:
                mid = (l + r)//2

                if s[mid]<char:
                    l=mid + 1
                elif s[mid]==char:
                    l=mid
                    break
                else:
                    r=mid
            
            return l
        
        def insert(s: str, char: chr):
            if not s:
                s.append(char)
                return 
            
            index=findIndex(s,char)
            if s[index]>char:
                s.insert(index,char)
            else:
                s.insert(index+1,char)
            
        result = list()
        p = sorted(p)
        len_s = len(s)
        len_p = len(p)
        
        window = sorted(s[0:len_p])
        if window==p:
            result.append(0)
            
        for i in range(1,len_s-len_p+1,1):
            window.remove(s[i-1])
            insert(window,s[i+len_p-1])
            
            if window==p:
                result.append(i)
                
        return result
