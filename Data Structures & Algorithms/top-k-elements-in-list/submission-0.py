class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            if n in count:
                count[n] = 1 + count.get(n,0)
            else:
                count[n] = 1
        
        sorted_descending = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        print(sorted_descending)
        result = []

        for i in sorted_descending:
            result.append(i)
            k=k-1
            if k == 0:
                return result