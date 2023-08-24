class Anagram:
    def __init__(self, word):
        self._word = word
    
    def match(self, word_list):
        anagrams = []
        for candidate in word_list:
            if sorted(candidate.lower()) == sorted(self._word.lower()) and candidate.lower() != self._word:
             anagrams.append(candidate)

        return anagrams
       

anagram_example = Anagram("listen")
words = ["enlist", "inlets", "silent", "hello", "tinsel", "neat", "slit", "nets", "shine", "tile", "site"]
matched_anagrams = anagram_example.match(words)
print(matched_anagrams)