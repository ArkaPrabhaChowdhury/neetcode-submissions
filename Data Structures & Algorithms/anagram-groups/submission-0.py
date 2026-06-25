class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortedStrings = {}
        shell = {}
        for i in range(len(strs)):
            sortedWord = (" ").join(sorted(strs[i]))
            sortedStrings[i] = sortedWord
            shell[sortedWord] = [] 

        for i in range(len(sortedStrings)):
            sortedWord = sortedStrings[i]
            ogWord = strs[i]
            shell[sortedWord].append(ogWord)

        return list(shell.values())

            