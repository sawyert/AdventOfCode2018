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

def Day12_2(start, rules, iterations):
  parsed_rules = parseRules(rules)
  state = list("...................." + start + ('.' * 2000))
  numbers = [-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]
  numbers = numbers + (list(range(1, 3000)))
  # print ("0:" + ''.join(state))
  while (iterations > 0):
    state = process(state, parsed_rules)
    print (str(iterations)+":" + ''.join(state))  
    iterations-=1
    
    if iterations < 4:
      index = 0    
      result = 0
      for char in state:
        if state[index] == '#':
          result += numbers[index]
        index += 1
      print (result)
  
  return result
    
print (Day12_2(INPUT, RULES, 50000000000))


