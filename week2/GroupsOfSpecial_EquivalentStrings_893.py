class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        words_set = set()
        for word in A:
            even_position=""
            odd_position=""
            for index,char in enumerate(word):
                if index%2==0:
                    even_position+=char
                else:
                    odd_position+=char
            
            sorted_word = ''.join(sorted(odd_position)+sorted(even_position))
            words_set.add(sorted_word)
        return len(words_set)
