class Player:
  def play(self):
      print("The player is playing cricket.")

class Batsman(Player):
  def play(self):
      print("The batsman is batting.")

class Bowler(Player):
  def play(self):
      print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman1 = Batsman()
bowler1 = Bowler()

# Call the play() method for each object
batsman1.play()
bowler1.play()
