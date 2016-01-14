import buildings, modules


subscibers = []

def notify(time):
	for subsciber in subscibers:
		subsciber.update(time)

class Game(object):
	"""docstring for Game
		Gametime is in seconds
		runGame() runs the game in Intervals of one second until 20 Minutes have passed
	"""
	def __init__(self, gametime):
		super(Game, self).__init__()
		self.gametime = gametime
		self.spieler = []
	def __repr__(self):
		return 'In this Game, there are %s, the current gametime is %s' % (self.spieler, self.gametime)
	def updatetimeSeconds(self, count):
		notify(count)
		self.gametime += count
		return self.gametime
	def updatetimeMinutes(self, count):
		notify(count*60)
		self.gametime += count*60
		return self.gametime
	def runGame(self):
		while self.gametime < 1200:
			notify(1)
			print(self)
			self.gametime += 1



		
class Spieler(object):
	"""docstring for Spieler"""
	def __init__(self, name, startgeld, bandbreite, game, basis):
		super(Spieler, self).__init__()
		self.name = name
		self.bitcoin = startgeld
		self.bandbreite = bandbreite
		self.basis = basis
		game.spieler.append(self)
	def __repr__(self):
		return 'Spieler %s has Bitcoin: %s, Bandbreite: %s' % (self.name, self.bitcoin, self.bandbreite)


def setupGame(game):

	spieler1basis = buildings.Basis()
	hans = Spieler('Hans', 30000, 6000, game, spieler1basis)
	spieler1basis.setOwner(hans)

	spieler2basis = buildings.Basis()
	peter = Spieler('Peter', 30000, 6000, game, spieler2basis)
	spieler2basis.setOwner(peter)

"""Game is supposed to last for 20 Minutes"""

def main():
	game = Game(0)


	#SETUP Spieler 1
	spieler1basis = buildings.Basis()
	subscibers.append(spieler1basis)
	hans = Spieler('Hans', 30000, 6000, game, spieler1basis)
	spieler1basis.setOwner(hans)

	#SETUP Spieler 2
	spieler2basis = buildings.Basis()
	subscibers.append(spieler2basis)
	peter = Spieler('Peter', 30000, 6000, game, spieler2basis)
	spieler2basis.setOwner(peter)
	

	game.runGame()

if __name__ == '__main__':
	main()