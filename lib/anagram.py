class Anagram:
    def __init__(self, word):
        self._word = word
    
    def match(self, word_list):
        anagrams = []
        for candidate in word_list:
            if sorted(candidate.lower()) == sorted(self._word.lower()) and candidate.lower() != self._word:
             anagrams.append(candidate)

        return anagrams
        pass