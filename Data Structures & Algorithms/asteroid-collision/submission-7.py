class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []
        state = []
        for rock in asteroids:
            while state and rock < 0 < state[-1]:
                lsurv = state[-1]
                if abs(rock) > lsurv:
                    state.pop()  # rock destroys top, continue checking
                elif abs(rock) == lsurv:
                    state.pop()  # both destroy each other
                    rock = 0     # stop further checks
                else:
                    rock = 0     # rock destroyed
            if rock != 0:
                state.append(rock)
        return state