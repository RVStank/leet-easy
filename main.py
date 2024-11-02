from typing import List, Optional

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        moves = 0
        x1, y1 = points.pop()
        while points:
            x2, y2 = points.pop()
            moves += max(abs(y2 - y1), abs(x2 - x1))
            x1, y1 = x2, y2

        return moves


if __name__ == "__main__":
    solution = Solution()
    solution.minTimeToVisitAllPoints([[1,1], [3,4], [-1,0]])