import GameSim

class Knotenpunkt(object):
	"""docstring for Knotenpunkt"""
	def __init__(self):
		super(Knotenpunkt, self).__init__()
		self.health = 100
		self.leistung = 0
		self.modulplaetze = 0
		self.netzwerkkarten = 0
		GameSim.subscibers.append(self)
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
		GameSim.subscibers.append(self)
	def setOwner(self, player):
		self.owner = player
	def update(self, time):
		self.owner.bitcoin += (time * self.grundproduktion)