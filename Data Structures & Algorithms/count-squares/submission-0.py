class CountSquares:
    def __init__(self):
        self.hashset = defaultdict(int)
        self.helo = []

    def add(self, point: List[int]) -> None:
        self.hashset[tuple(point)] += 1
        self.helo.append(point)
    def count(self, point: List[int]) -> int:
        res = 0
        Px,Py = point
        for x, y in self.helo:
            if (abs(Px - x) != abs(Py - y)) or Px == x or Py == y:
                continue
            res += self.hashset[(x,Py)] * self.hashset[(Px,y)]
        return res
        