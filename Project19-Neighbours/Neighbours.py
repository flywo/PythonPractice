#!/usr/bin/env python
# coding:utf-8


def check(grid, row, col):
    neighbours = []
    for x in range(row-1,row+2):
        neighbours.extend(([x, col - 1], [x, col + 1])) if x==row else \
            neighbours.extend(([x, col-1], [x, col], [x, col+1]))
    neighbours = [(x, y) for x,y in neighbours if
                  len(grid)>x>=0 and len(grid[0])>y>=0]
    return len([1 for x,y in neighbours if grid[x][y]==1])


#大神
def check1(grid, row, col):
    rows = range(max(0, row-1), min(row+2, len(grid)))
    cols = range(max(0, col-1), min(col+2, len(grid[0])))
    return sum(grid[r][c] for r in rows for c in cols)-grid[row][col]


def check2(grid, row, col):
    rs, cs = [slice(max(0,x-1), x+2) for x in (row, col)]
    return sum(e for r in grid[rs] for e in r[cs]) - grid[row][col]


def check3(grid, row, col):
    n, m = len(grid), len(grid[0])
    neighbours = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    return sum(0<=row+i<n and 0<=col+j<m and grid[row+i][col+j] for i,j in neighbours)


if __name__ == '__main__':
    tup = ([[[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0]],5,4])
    print(check(*tup))
    print(check1(*tup))
    print(check2(*tup))
    print(check3(*tup))

    fun = lambda grid, I, J: sum(cell
                                 for i, row in enumerate(grid)
                                 for j, cell in enumerate(row)
                                 if max(abs(i-I), abs(j-J)) == 1)
    print(fun(*tup))