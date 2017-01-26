class PictorPlayer():
	
	def __init__(self):
		self.__health = 0
		self.__visible = False
		self.__location = ""
		
	def getHealth(self):
		return self.__health
		
	def setHealth(self, health):
		self.__health = health
		
	def getLocation(self):
		return self.__location
		
	def setLocation(self, location):
		self.__location = location
	
	def getVisible(self):
		return self.__visible
		
	def setVisible(self, visible):	
		self.__visible = visible

#-------------------------------------------------------------------
class PictorInventory():
	
	def __init__(self):
		self.__capacity = 0
		self.__objects = []
	
	def getCapacity(self):
		return self.__capacity
	
	def setCapacity(self, capacity):
		self.__capacity = capacity
		
	def getObjects(self):
		return self.__objects
		
	def addObject(self, name):
		self.__objects.append(name)
		
	def removeObject(self, name):
		self.__objects.remove(name)

#-------------------------------------------------------------------
class PictorRoom():
	
	def __init__(self):
		self.__name = ""
		self.__longDescription = ""
		self.__shortDescription = ""
		self.__discovered = False
		self.__lighted = False
		self.__objects = []
		self.__exits = []
		
	def getName(self):
		return self.__name
	
	def setName(self, name):
		self.__name = name
		
	def getLongDescription(self):
		return self.__longDescription
		
	def setLongDescription(self, description):
		self.__longDescription = description
	
	def getShortDescription(self):
		return self.__shortDescription
		
	def setShortDescription(self, description):
		self.__shortDescription = description
		
	def getDiscovered(self):
		return self.__discovered
		
	def setDiscovered(self, discovered):
		self.__discovered = discovered
		
	def getLighted(self):
		return self.__lighted
		
	def setLighted(self, lighted):
		self.__lighted = lighted
		
	def getObjects(self):
		return self.__objects
		
	def addObject(self, name):
		self.__objects.append(name)
		
	def removeObject(self, name):
		self.__objects.remove(name)
		
	def getExits(self):
		return self.__exits
		
	def addExit(self, name):
		self.__exits.append(name)
		
	def removeExit(self, name):
		self.__exits.remove(name)
		
#-------------------------------------------------------------------
class PictorExit():
	
	def __init__(self):
		self.__name = ""
		self.__longDescription = ""
		self.__shortDescription = ""
		self.__visible = False
		self.__unlocked = False
		self.__keyObjects = ""
		self.__toRoom = ""	
			
	def getName(self):
		return self.__name
	
	def setName(self, name):
		self.__name = name
	
	def getLongDescription(self):
		return self.__longDescription
	
	def setLongDescription(self, description):
		self.__longDescription = description
	
	def getShortDescription(self):
		return self.__shortDescription
		
	def setShortDescription(self, description):
		self.__shortDescription = description
			
	def getVisible(self):
		return self.__visible
		
	def setVisible(self, visible):	
		self.__visible = visible
		
	def getUnLocked(self):
		return self.__unlocked
		
	def setUnLocked(self, unlocked):
		self.__unlocked = unlocked
	
	def getKeyObject(self):
		return self.__keyObject
	
	def setKeyObject(self, keyObject):
		self.__keyObject = keyObject
	
	def getToRoom(self):
		return self.__toRoom
	
	def setToRoom(self, room):
		self.__toRoom = room
	
#-------------------------------------------------------------------		
class PictorObject():
	
	def __init__(self):
		self.__name = ""
		self.__longDescription = ""
		self.__shortDescription = ""
		self.__weight = 0
		self.__visible = False
		self.__acquirable = False
		self.__healthPoints = 0
		self.__damagePoints = 0
		self.__protectionPoints = 0
		self.__lighted = False
		self.__equipped = False
		self.__read = False
		self.__unlocked = True

	def getName(self):
		return self.__name
	
	def setName(self, name):
		self.__name = name    
		
	def getLongDescription(self):
		return self.__longDescription
	
	def setLongDescription(self, description):
		self.__longDescription = description
	
	def getShortDescription(self):
		return self.__shortDescription
		
	def setShortDescription(self, description):
		self.__shortDescription = description
	
	def getWeight(self):
		return self.__weight
		
	def setWeight(self, weight):
		self.__weight = weight
	
	def getVisible(self):
		return self.__visible
		
	def setVisible(self, visible):
		self.__visible = visible
		
	def getAquirable(self):
		return self.__aquirable
		
	def setAquirable(self, aquirable):
		self.__aquirable = aquirable
		
	def getHealthPoints(self):
		return self.__healthPoints
		
	def setHealthPoints(self, points):
		self.__healthPoints = points
		
	def getLighted(self):
		return self.__lighted
		
	def setLighted(self, lighted):
		self.__lighted = lighted

	def getUnLocked(self):
		return self.__unlocked
	
	def setUnLocked(self, unlocked):
		self.__unlocked = unlocked
	
	def getProtectionPoints(self):
		return self.__protectionPoints
	
	def setProtectionPoints(self, points):
		self.__protectionPoints = points
		
	def getEquipped(self):
		return self.__equipped
	
	def setEquipped(self, equipped):
		self.__equipped = equipped
		
	def getRead(self):
		return self.__read
	
	def setRead(self, read):
		self.__read = read
	
	def getDamagePoints(self):
		return self.__damagePoints
		
	def setDamagePoints(self, points):
		self.__damagePoints = points
	
#-------------------------------------------------------------------
class PictorGhost():
	
	def __init__(self):
		self.__name = ""
		self.__longDescription = ""
		self.__shortDescription = ""
		self.__visible = False
		self.__location = ""
		self.__health = 0	
		self.__damagePoints = 0	

	def getName(self):
		return self.__name
	
	def setName(self, name):
		self.__name = name    
		
	def getLongDescription(self):
		return self.__longDescription
	
	def setLongDescription(self, description):
		self.__longDescription = description
	
	def getShortDescription(self):
		return self.__shortDescription
		
	def setShortDescription(self, description):
		self.__shortDescription = description
		
	def getVisible(self):
		return self.__visible
		
	def setVisible(self, visible):
		self.__visible = visible	
			
	def getLocation(self):
		return self.__location
		
	def setLocation(self, location):
		self.__location = location
					
	def getHealth(self):
		return self.__health
		
	def setHealth(self, health):
		self.__health = health
		
	def getDamagePoints(self):
		return self.__damagePoints
		
	def setDamagePoints(self, points):
		self.__damagePoints = points
