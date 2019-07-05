class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ans=None
        saved = dict()
        for word in re.split('\W+', paragraph.lower()):
            if word.isalpha() and word not in banned:
                if word not in saved:
                    saved[word]=0
                saved[word]+=1
                if not ans or saved[ans]<saved[word]:
                    ans=word
        return ans
