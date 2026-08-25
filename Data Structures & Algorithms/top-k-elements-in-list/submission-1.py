class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for n in nums:
            countMap[n] = 1 + countMap.get(n,0)
        sortedMap = sorted(countMap,key=countMap.get,reverse=True)
        return sortedMap[:k]