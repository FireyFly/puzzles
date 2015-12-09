import re
import sys

grid = [[0]*1000 for _ in range(1000)]

#def do(op, sx, sy, tx, ty):
#  for x in range(sy, ty + 1):
#    for y in range(sx, tx + 1):
#      if op == 'turn on': grid[y][x] = 1
#      elif op == 'turn off': grid[y][x] = 0
#      elif op == 'toggle': grid[y][x] = 1 - grid[y][x]
#      else: raise("error: bad op '" + op + "'")

def do(op, sx, sy, tx, ty):
  for x in range(sy, ty + 1):
    for y in range(sx, tx + 1):
      if op == 'turn on': grid[y][x] += 1
      elif op == 'turn off': grid[y][x] = max(grid[y][x] - 1, 0)
      elif op == 'toggle': grid[y][x] += 2
      else: raise("error: bad op '" + op + "'")

for line in sys.stdin:
  op, sx, sy, tx, ty = re.findall(r'(.*) (\d+),(\d+) through (\d+),(\d+)', line)[0]
  do(op, int(sx), int(sy), int(tx), int(ty))

print(sum(sum(xs) for xs in grid))
