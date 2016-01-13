class Game(object):
	"""docstring for Game"""
	def __init__(self, gametime):
		super(Game, self).__init__()
		self.gametime = gametime
		self.spieler = []

	def __repr__(self):
		return 'In this Game, there are %s, the current gametime is %s' % (self.spieler, self.gametime)
		

class Basis(object):
	"""docstring for Basis"""
	def __init__(self, health):
		super(Basis, self).__init__()
		self.health = health
	def reduceHealth(self, count):
		self.health -= count
		
class Spieler(object):
	"""docstring for Spieler"""
	def __init__(self, name, startgeld, bandbreite):
		super(Spieler, self).__init__()
		self.name = name
		self.bitcoin = startgeld
		self.bandbreite = bandbreite

	def __repr__(self):
		return 'Spieler %s has Bitcoin: %s, Bandbreite: %s' % (self.name, self.bitcoin, self.bandbreite)
		

"""Game is supposed to last for 20 Minutes"""

def update(newgametime):
	Game.gametime = newgametime

def main():
	game = Game(0)
	hans = Spieler('Hans', 3000, 6000)
	peter = Spieler('Peter', 3000, 6000)
	game.spieler.append(hans)
	game.spieler.append(peter)

	print(game)

	basiseins = Basis(100)
	basiszwei = Basis(100)
	print(basiseins.health)
	print(basiszwei.health)
	basiseins.reduceHealth(50)
	print(basiseins.health)

if __name__ == '__main__':
	main()
