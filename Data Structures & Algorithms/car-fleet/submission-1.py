class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])

        cars.sort(key=lambda x: x[0], reverse=True)
        
        for i in range(len(position)):
            pos = cars[i][0]
            spd = cars[i][1]
            time = (target - pos)/spd
            if not stk or time > stk[-1]:
                stk.append(time)
        return len(stk)