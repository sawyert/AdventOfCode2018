input = """
59, 110
127, 249
42, 290
90, 326
108, 60
98, 168
358, 207
114, 146
242, 170
281, 43
233, 295
213, 113
260, 334
287, 260
283, 227
328, 235
96, 259
232, 177
198, 216
52, 115
95, 258
173, 191
156, 167
179, 135
235, 235
164, 199
248, 180
165, 273
160, 297
102, 96
346, 249
176, 263
140, 101
324, 254
72, 211
126, 337
356, 272
342, 65
171, 295
93, 192
47, 200
329, 239
60, 282
246, 185
225, 324
114, 329
134, 167
212, 104
338, 332
293, 94
"""

testdata = """
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
"""

from collections import Counter 

def createGrid(size):
  grid = []
  x = 0
  while x < size:
    grid.append([])
        
    y = 0
    while y < size:
      grid[x].append("99999")
      y+=1
      
    x+=1
  return grid
  
def dist(a, b):
  return abs(a[0]-b[0])+abs(a[1]-b[1])
  
def print_grid(grid):
  print("*****************")
  for row in grid:
    print (row)   
  
def Day6_1(input, gridSize):
  grid_distances = createGrid(gridSize)
  grid_whichpoint = createGrid(gridSize)
  rows = input.split("\n")
  rownum = 1
  for row in rows:
    if len(row.strip()) == 0: continue
    coords = row.split(',')
    x = int(coords[1])
    y = int(coords[0])
    grid_distances[x][y] = "R" + str(rownum)
    grid_whichpoint[x][y] = "R" + str(rownum)
    print ("R" + str(rownum))
    for i in range(0, gridSize):
      for j in range(0, gridSize):
        if str(grid_distances[i][j])[0] == "R": continue
        distance = dist((i,j),(x,y))
        existing_distance = int(grid_distances[i][j])
        if distance < existing_distance:
            grid_distances[i][j]=distance
            grid_whichpoint[i][j]="r"+str(rownum)
        if distance == existing_distance:
            grid_distances[i][j]=distance
            grid_whichpoint[i][j]+="r"+str(rownum)
    rownum += 1
  #print_grid(grid_distances)
  #print_grid(grid_whichpoint)
  
  cnt = Counter()
  for i in range(0, gridSize):
      for j in range(0, gridSize):
        cnt[grid_whichpoint[i][j]] += 1
        
  for i in range(0, gridSize):
    cnt[grid_whichpoint[i][0]] = 0
    cnt[grid_whichpoint[i][gridSize-1]] = 0
    
  for j in range(0, gridSize):
    cnt[grid_whichpoint[0][j]] = 0
    cnt[grid_whichpoint[gridSize-1][j]] = 0
  print(cnt.most_common())
  return int(cnt.most_common()[0][1])+1

assert(Day6_1(testdata, 20)==17)
print(Day6_1(input, 1200))