

class Circle():
  def __init__(self):
    self.marbles = [0]
    self.current_marble_index = 0
    
    
  def add_marble(self, marble_index):
    self.marbles.append(marble_index)
    print (self.marbles)

class CircleGame():
  def __init__(self):
    self.scores = {}
    self.circle = Circle()
    
  def add_marble(self, player, marble_index):
    self.circle.add_marble(marble_index)  



def Day9_1(players, lastMarbleScore):
  game = CircleGame()
  player_turns = 0
  marble_index = 1
  while (player_turns < players):
    game.add_marble(player_turns, marble_index)
    player_turns+=1
    marble_index+=1
  
  
assert(Day9_1(10,1618)==8317)
assert(Day9_1(13,7999)==146373)
assert(Day9_1(17,1104)==2764)
assert(Day9_1(21,6111)==54718)
assert(Day9_1(30,5807)==37305)
print(Day9_1(427,70723))