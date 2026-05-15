class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse = True)
        fleets = 1
        # time taken by the closest car to destination
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currTime = (target - pair[i][0]) / pair[i][1]
            # if the next car is taking more time than previous
            # it means, it will never meet
            # in that case, change the previous time to current and increase fleet
            if currTime > prevTime:
                prevTime = currTime
                fleets += 1
        return fleets

