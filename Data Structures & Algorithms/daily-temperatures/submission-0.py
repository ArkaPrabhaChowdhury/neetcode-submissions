class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while(stk and temperatures[i]>temperatures[stk[-1]]):
                index = stk.pop()
                res[index] = i-index
            stk.append(i)
        
        return res