import GameSim

class Modul(object):
	"""
		Können in Knotenpunkte eingesetzt werden. Ein Knotenpunkt hat nur eine begrenzte Anzahl Plätze.
	"""
	def __init__(self):
		super(Modul, self).__init__()
		self.kosten = 0		


class Controlserver(Modul):
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

class Bitcoinmine(Modul):
	"""
		A Bitcoinmine produces Bitcoins, thats it.
	"""
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
		self.owner.bitcoin += (time * self.produktion)