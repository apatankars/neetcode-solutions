class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortedWords = {}
        for word in strs:

            sortedWord = ''.join(sorted(word))
            if sortedWord not in sortedWords:
                sortedWords[sortedWord] = [word]
            else:
                sortedWords[sortedWord].append(word)
        
        result = []
        for sortedWord, wordList in sortedWords.items():
            result.append(wordList)
        
        return result



        