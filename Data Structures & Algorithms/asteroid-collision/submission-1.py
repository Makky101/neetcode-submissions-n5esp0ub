class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []
        state = []
        for rock in asteroids:
            while state and rock < 0 < state[-1]:
                if state[-1] < abs(rock):
                    state.pop()
                    continue
                elif state[-1] == abs(rock):
                    state.pop()
                break
            else:
                state.append(rock)
        return state