class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        stack = []
        i = 0
        while i<len(formula):
            atom=formula[i]
            i += 1
            if atom == ("("):
                stack+="("
            elif atom == (")"):
                num = ""
                while i<len(formula) and formula[i].isdigit():
                    num+=formula[i]
                    i+=1
                
                num = int(num) if num else 1
                temp=[]
                while stack and stack[-1] != "(":
                    (a,b) = stack.pop()
                    temp.insert(0,(a,b*num))
                
                stack.pop()
                stack.extend(temp)
            else:
                while i<len(formula) and formula[i].islower():
                    atom+=formula[i]
                    i+=1
                
                count = ""
                while i<len(formula) and formula[i].isdigit():
                    count+=formula[i]
                    i+=1
                
                stack.append((atom, int(count) if count else 1))
        
        saved=dict()
        for (atom, count) in stack:
            if atom not in saved:
                saved[atom] = 0
            saved[atom] += count
        
        print(saved)
        ans=str()
        for (atom,count) in sorted(saved.items()):
            ans+=atom if count==1 else atom+str(count)
        
        return ans
                
