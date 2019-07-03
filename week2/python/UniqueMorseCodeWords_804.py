class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        encrypted_set = set()
        for word in words:
            encrypted_word="".join(morse_codes[ord(char) - ord('a')] for char in word)
            encrypted_set.add(encrypted_word)
            
        return len(encrypted_set)
