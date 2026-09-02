class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))  # store timestamp first, makes bisect easier

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        arr = self.timeMap[key]
        lo, hi = 0, len(arr) - 1
        res = ""
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]   # candidate answer, keep searching right for a better one
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res