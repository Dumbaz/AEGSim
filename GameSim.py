subscibers = []

def notify(time):
	for subsciber in subscibers:
		subsciber.update(time)

class Game(object):
	"""docstring for Game
		Gametime is in seconds
		runGame() runs the game until 20 Minutes have passed
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
			self.gametime += 1

class Knotenpunkt(object):
	"""docstring for Knotenpunkt"""
	def __init__(self):
		super(Knotenpunkt, self).__init__()
		self.health = 100
		self.leistung = 0
		self.modulplaetze = 0
		self.netzwerkkarten = 0
		subscibers.append(self)
	def __repr__(self):
		return 'Dieser Knotenpunkt hat %s Lebenspunkte und %s Leistungspunkte.' % (self.health, self.leistung)
	def changeHealth(self, count):
		self.health += count
		if self.health < 0:
			self.health = 0
	def changeLeistung(self, count):
		self.leistung += count
		if self.leistung < 0:
			self.leistung = 0
	def update(self, time):
		if self.leistung == 0:
			self.changeHealth(-(time*100))
		elif self.leistung > 0:
			self.changeHealth(time*50)

class KleinerKnotenpunkt(Knotenpunkt):
	"""docstring for KleinerKnotenpunkt"""
	def __init__(self):
		super(KleinerKnotenpunkt, self).__init__()
		self.health = 3000
		self.leistung = 5000
		self.modulplaetze = 3
		self.netzwerkkarten = 2

class MittlererKnotenpunkt(Knotenpunkt):
	"""docstring for MittlererKnotenpunkt"""
	def __init__(self):
		super(MittlererKnotenpunkt, self).__init__()
		self.health = 4500
		self.leistung = 7500
		self.modulplaetze = 5
		self.netzwerkkarten = 3

class GrosserKnotenpunkt(Knotenpunkt):
	"""docstring for GrosserKnotenpunkt"""
	def __init__(self):
		super(GrosserKnotenpunkt, self).__init__()
		self.health = 6000
		self.leistung = 10000
		self.modulplaetze = 7
		self.netzwerkkarten = 4

class Basis(Knotenpunkt):
	"""docstring for Basis"""
	def __init__(self):
		super(Basis, self).__init__()
		self.health = 100000
		self.Leistungspunkte = 50000
		self.modulplaetze = 3
		self.netzwerkkarten = 3
		self.grundproduktion = 100
		self.owner = None
	def setOwner(self, player):
		self.owner = player
	def update(self, time):
		self.owner.bitcoin += time * self.grundproduktion


class Controlserver(object):
	"""docstring for Controlserver"""
	def __init__(self):
		super(Controlserver, self).__init__()
		self.kosten = 20000
		self.leistungskosten = 1000
		self.ownedclients = 0
		self.clientrate = 2
		self.owner = None
		subscibers.append(self)
	def setOwner(self, player):
		self.owner = player
	def update(self, time):
		self.ownedclients += 2 * time

class Bitcoinmine(object):
	"""docstring for Bitcoinmine"""
	def __init__(self):
		super(Bitcoinmine, self).__init__()
		self.kosten = 10000
		self.produktion = 350
		self.leistungskosten = 500
		self.owner = None
		subscibers.append(self)
	def setOwner(self, player):
		self.owner = player
	def update(self, time):
		self.owner.bitcoin += time * self.produktion

		
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
	spieler1basis = Basis()
	hans = Spieler('Hans', 30000, 6000, game, spieler1basis)
	spieler1basis.setOwner(hans)

	spieler2basis = Basis()
	peter = Spieler('Peter', 30000, 6000, game, spieler2basis)
	spieler2basis.setOwner(peter)


	print(game)

"""Game is supposed to last for 20 Minutes"""

def main():
	game = Game(0)
	setupGame(game)

	testbase = Knotenpunkt()
	testbase.changeLeistung(-120)
	testbase.changeLeistung(10)


	game.updatetimeSeconds(50)

	game.updatetimeMinutes(15)

	game.runGame()
	print(game)

if __name__ == '__main__':
	main()
