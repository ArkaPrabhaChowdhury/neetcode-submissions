class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrings = {}
        shell = {}

        for i in range(len(strs)):
            sortedWord = (" ").join(sorted(strs[i]))
            sortedStrings[i] = sortedWord
            shell[sortedWord] = []

        for i in range(len(sortedStrings)):
            ogWord = strs[i]
            shell[sortedStrings[i]].append(ogWord)

        return list(shell.values())