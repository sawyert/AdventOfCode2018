INPUT = "#...#####.#..##...##...#.##.#.##.###..##.##.#.#..#...###..####.#.....#..##..#.##......#####..####..."

RULES = """
#.#.# => #
..### => .
#..#. => #
.#... => #
..##. => #
##.#. => #
##..# => #
####. => #
...#. => #
..#.# => #
.#### => #
#.### => .
...## => .
..#.. => .
#...# => .
.###. => #
.#.## => .
.##.. => #
....# => .
#..## => .
##.## => #
#.##. => .
#.... => .
##... => #
.#.#. => .
###.# => #
##### => #
#.#.. => .
..... => .
.##.# => .
###.. => .
.#..# => .
"""

TEST_INPUT = "#..#.#..##......###...###"
TEST_RULES = """
...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
"""

def process_rule(teststring, rules):
  try:
    result = rules[teststring]
  except KeyError:
    result = "."
  return result 

def process(state, rules):
  index=0
  newState = list(state)
  while(True):
    if index < 2:
      index+=1
      continue
    try:  
      teststring = state[index-2]+state[index-1]+state[index]+state[index+1]+state[index+2]
      result = process_rule(teststring, rules)
      # print ("%d: %s => %s" % (index, teststring, result))
      newState[index] = result    
    except IndexError:
      try:
        newState[index] = "."
      except IndexError:
        pass
      
    index+=1
    if (index > len(state)):
      break
  return newState
    
def parseRules(rules):
  parsedRules = {}
  for rule in rules.split("\n"):
    if len(rule.strip()) == 0:
      continue
    key = rule[0:5]
    value = rule[-1]
    parsedRules[key] = value
    print ("%s => %s" % (key, parsedRules[key]))
  return parsedRules

def Day12_1(start, rules, iterations):
  parsed_rules = parseRules(rules)
  state = list("...................." + start + ('.' * 100))
  numbers = [-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120]
  print ("0:" + ''.join(state))
  while (iterations > 0):
    state = process(state, parsed_rules)
    print (str(iterations)+":" + ''.join(state))  
    iterations-=1

  index = 0    
  result = 0
  for char in state:
    print (index)
    if state[index] == '#':
      result += numbers[index]
    index += 1
  
  return result
    
print (Day12_1(INPUT, RULES, 20))


