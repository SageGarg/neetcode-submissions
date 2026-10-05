class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0] * len(position)
        for i in range(len(position)):
            time[i] = (target - position[i]) / speed[i]

        myList = list(zip(position, time))
        myList.sort(reverse=True)          # closest to target first

        stack = []                         # each entry = one fleet's arrival time
        for pos, t in myList:
            if not stack or t > stack[-1]: # can't catch the fleet ahead
                stack.append(t)            # it becomes a new fleet
            # else: t <= stack[-1], so it joins the fleet ahead. Nothing to do.

        return len(stack)