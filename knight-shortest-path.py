'''
Given a knight in a chessboard(a binary matrix with 0 as empty and 1 as barrier)
with a source position, find the shortest path to a destination position, return
the length of the route. Return -1 if knight cannot be reached.
'''


class Solution:
    # @return {int} the shortest path
    def shortestPath(self, grid, source, destination):
        # Write your code here
        n = len(grid)
        m = len(grid[0])

        import sys
        record = [[sys.maxint for _ in xrange(m)] for i in xrange(n)]
        record[source.x][source.y] = 0

        import Queue
        q = Queue.Queue(maxsize = n * m)
        q.put(source)

        d = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        while not q.empty():
            head = q.get()
            for dx, dy in d:
                x, y = head.x + dx, head.y + dy
                if x >=0 and x < n and y >= 0 and y < m and not grid[x][y] and \
                    record[head.x][head.y] + 1 < record[x][y]:
                    record[x][y] = record[head.x][head.y] + 1
                    q.put(Point(x, y))

        if record[destination.x][destination.y] == sys.maxint:
            return -1

        return record[destination.x][destination.y]
