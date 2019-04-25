from queue import Queue
class QItem:
    def __init__(self, x, y, dist):
        self.row = x
        self.col = y
        self.dist = dist

def get_distance():
    blockades = [(1,1)]
    source = (0,0)
    destination = (2, 2)
    # print blockades
    grid = get_grid(3, 3, blockades)
    print min_distance(grid, source, destination, N, M)

def min_distance(grid, src, dst, N, M):
    QItem source(srs[0], src[1], 0)
    visited = [[0] * N for i in range(M)]

    # initialize by marking some cells as visited
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '0': visited[i][j] = True 
            else: visited[i][j] = False

    
    # apply BFS 
    q = Queue()





def get_grid(N, M, blockades):
    grid = [['*'] * N for i in range(M)]
    for i in range(len(grid)):
        for j in range(len(grid[0])): 
            if (i,j) in blockades: 
                grid[i][j] = '0'
    return grid

get_distance()