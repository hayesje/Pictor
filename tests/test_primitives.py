import unittest

from primitives import PictorPlayer
from primitives import PictorInventory
from primitives import PictorRoom
from primitives import PictorExit
from primitives import PictorObject
from primitives import PictorGhost

pPlayer = PictorPlayer()
pRoom = PictorRoom()
pInventory = PictorInventory()
pExit = PictorExit()
pObject = PictorObject()
pGhost = PictorGhost()

		
class TruthTest(unittest.TestCase):
	#1
	def test_player_visible_true(self):
		pPlayer.setVisible(True)
		self.assertTrue(pPlayer.getVisible(), "#1:  Failed Player -> setVisible(True)")
	#2	
	def test_player_visible_false(self):
		pPlayer.setVisible(False)
		self.assertFalse(pPlayer.getVisible(), "#2  Failed Player -> setVisible(False)")	
	#3	
	def test_room_discovered_true(self):
		pRoom.setDiscovered(True)
		self.assertTrue(pRoom.getDiscovered(), "#3  Failed Room -> setDiscovered(True)")
    #4
	def test_room_discovered_false(self):
		pRoom.setDiscovered(False)
		self.assertFalse(pRoom.getDiscovered(), "#4  Failed Room -> setDiscovered(False)")
    #5
	def test_room_lighted_true(self):
		pRoom.setLighted(True)
		self.assertTrue(pRoom.getLighted(), "#5  Failed Room -> setLighted(True)")
    #6
	def test_room_lighted_false(self):
		pRoom.setLighted(False)
		self.assertFalse(pRoom.getLighted(), "#6  Failed Room -> setLighted(False)")
	#7	
	def test_exit_visible_true(self):
		pExit.setVisible(True)
		self.assertTrue(pExit.getVisible(), "#7  Failed Exit -> setVisible(True)")
    #8
	def test_exit_visible_false(self):
		pExit.setVisible(False)
		self.assertFalse(pExit.getVisible(), "#8  Failed Exit -> setVisible(False)")
	#9	
	def test_exit_unlocked_true(self):
		pExit.setUnLocked(True)
		self.assertTrue(pExit.getUnLocked(), "#9  Failed Exit -> setUnlocked(True)")
    #10 
	def test_exit_unlocked_false(self):
		pExit.setUnLocked(False)
		self.assertFalse(pExit.getUnLocked(), "#10  Failed Exit -> setUnlocked(False)")
	#11	
	def test_object_acquirable_true(self):
		pObject.setAquirable(True)
		self.assertTrue(pObject.getAquirable(), "#11  Failed Object -> setAquirable(True)")
    #12
	def test_object_acquirable_false(self):
		pObject.setAquirable(False)
		self.assertFalse(pObject.getAquirable(), "#12  Failed Object -> setAquirable(False)")
	#13		
	def test_object_visible_true(self):
		pObject.setVisible(True)
		self.assertTrue(pObject.getVisible(), "#13  Failed Object -> setVisible(True)")
    #14
	def test_object_visible_false(self):
		pObject.setVisible(False)
		self.assertFalse(pObject.getVisible(), "#14  Failed Object -> setVisible(False)")		
	#15					
	def test_object_lighted_true(self):
		pObject.setLighted(True)
		self.assertTrue(pObject.getLighted(), "#15  Failed Object -> setLighted(True)")
    #16
	def test_object_lighted_false(self):
		pObject.setLighted(False)
		self.assertFalse(pObject.getLighted(), "#16  Failed Object -> setLighted(False)")
    #17
	def test_object_equipped_true(self):
		pObject.setEquipped(True)
		self.assertTrue(pObject.getEquipped(), "#17  Failed Object -> setEquipped(True)")
    #18
	def test_object_equipped_false(self):
		pObject.setEquipped(False)
		self.assertFalse(pObject.getEquipped(), "#18  Failed Object -> setEquipped(False)")
    #19
	def test_object_read_true(self):
		pObject.setRead(True)
		self.assertTrue(pObject.getRead(), "#19  Failed Object -> setRead(True)")
    #20
	def test_object_read_false(self):
		pObject.setRead(False)
		self.assertFalse(pObject.getRead(), "#20  Failed Object -> setRead(False)")
	#21			
	def test_object_unlocked_true(self):
		pObject.setUnLocked(True)
		self.assertTrue(pObject.getUnLocked(), "#21  Failed Object -> setUnLocked(True)")
    #22
	def test_object_unlocked_false(self):
		pObject.setUnLocked(False)
		self.assertFalse(pObject.getUnLocked(), "#22  Failed Object -> setUnLocked(False)")
    #23 				
	def test_ghost_visible_true(self):
		pGhost.setVisible(True)
		self.assertTrue(pGhost.getVisible(), "#23  Failed Ghost -> setVisible(True)")
    #24
	def test_ghost_visible_false(self):
		pGhost.setVisible(False)
		self.assertFalse(pGhost.getVisible(), "#24  Failed Ghost -> setVisile(False)")		

	
class InequalityTest(unittest.TestCase):
	
	#25
	def test_player_health(self):
		pPlayer.setHealth(100)
		self.assertEqual(pPlayer.getHealth(), 100, "#25  Failed Player -> setHealth()")  
	#26
	def test_player_location(self):
		pPlayer.setLocation("Kitchen")
		self.assertEqual(pPlayer.getLocation(), "Kitchen", "#26  Failed Player -> setLocation()")	
	#27
	def test_inventory_capacity(self):
		pInventory.setCapacity(180)
		self.assertEqual(pInventory.getCapacity(), 180, "#27  Failed Inventory -> setCapacity()")
	#28
	def test_inventory_object_add(self):
		olist = ['Object1', 'Object2', 'Object3']
		pInventory.addObject("Object1")
		pInventory.addObject("Object2")
		pInventory.addObject("Object3")
		self.assertItemsEqual(pInventory.getObjects(), olist, "#28  Failed Inventory -> addObject()")
	#29	
	def test_inventory_object_remove(self):
		olist = ['Object2']
		pInventory.removeObject("Object1")
		pInventory.removeObject("Object3")
		self.assertItemsEqual(pInventory.getObjects(), olist, "#29  Failed Inventory -> removeObject()")
	#30
	def test_room_name(self):
		pRoom.setName("Treasure Room")
		self.assertEqual(pRoom.getName(), "Treasure Room", "#30  Failed Room -> setRoom()")
	#31
	def test_room_long_description(self):
		pRoom.setLongDescription("Long Description")
	#32
	def test_room_short_description(self):
		pRoom.setShortDescription("Short Description")
		self.assertEqual(pRoom.getShortDescription(), "Short Description", "#32  Failed Room -> setShortDescription()")
	#33
	def test_room_object_add(self):
		olist = ['Object1', 'Object2', 'Object3']
		pRoom.addObject("Object1")
		pRoom.addObject("Object2")
		pRoom.addObject("Object3")
		self.assertItemsEqual(pRoom.getObjects(), olist, "#33  Failed Room -> addObject()")
	#34
	def test_room_object_remove(self):
		olist = ['Object2']
		pRoom.removeObject("Object1")
		pRoom.removeObject("Object3")
		self.assertItemsEqual(pRoom.getObjects(), olist, "#34  Failed Room -> removeObject()")
	#35
	def test_room_exit_add(self):
		olist = ['Exit1', 'Exit2', 'Exit3']
		pRoom.addExit("Exit1")
		pRoom.addExit("Exit2")
		pRoom.addExit("Exit3")
		self.assertItemsEqual(pRoom.getExits(), olist, "#35  Failed Room -> addExit()")
	#36
	def test_room_exit_remove(self):
		olist = ['Exit2']
		pRoom.removeExit("Exit1")
		pRoom.removeExit("Exit3")
		self.assertItemsEqual(pRoom.getExits(), olist, "#36  Failed Room  -> removeExit()")
	#37
	def test_exit_name(self):
		pExit.setName("CD1")
		self.assertEqual(pExit.getName(), "CD1", "#37  Failed Exit -> setName()")
	#38
	def test_exit_long_description(self):
		pExit.setLongDescription("Long Description")
		self.assertEqual(pExit.getLongDescription(), "Long Description", "#38  Failed Exit -> setLongDescription()")	
	#39
	def test_exit_short_description(self):
		pExit.setShortDescription("Short Description")
		self.assertEqual(pExit.getShortDescription(), "Short Description", "#39  Failed Exit -> setShortDescription()")
	#40
	def test_exit_key_object(self):
		pExit.setKeyObject("Key1")
		self.assertEqual(pExit.getKeyObject(), "Key1", "#40  Failed Exit -> setKeyObject()")
	#41
	def test_exit_to_room(self):
		pExit.setToRoom("Storeroom")
		self.assertEqual(pExit.getToRoom(), "Storeroom", "#41  Failed Exit -> setToRoom()")
	#42
	def test_object_name(self):
		pObject.setName("Cloak1")
		self.assertEqual(pObject.getName(), "Cloak1", "#42  Failed Object -> setName()")
	#43
	def test_object_long_description(self):
		pObject.setLongDescription("Long Description")
		self.assertEqual(pObject.getLongDescription(), "Long Description", "#43  Failed Object -> setLongDescription()")
	#44
	def test_object_short_description(self):
		pObject.setShortDescription("Short Description")
		self.assertEqual(pObject.getShortDescription(), "Short Description", "#44  Failed Object -> setShortDescription()")
	#45
	def test_object_weight(self):
		pObject.setWeight(5)
		self.assertEqual(pObject.getWeight(), 5, "#45  Failed Object -> setWeight()")
	#46
	def test_object_health_points(self):
		pObject.setHealthPoints(25)
		self.assertEqual(pObject.getHealthPoints(), 25, "#46  Failed Object -> setHealthPoints()")
	#47 
	def test_object_damage_points(self):
		pObject.setDamagePoints(10)
		self.assertEqual(pObject.getDamagePoints(), 10, "#47  Failed Object -> setDamagePoints()")
	#48
	def test_object_protection_points(self):
		pObject.setProtectionPoints(47)
		self.assertEqual(pObject.getProtectionPoints(), 47, "#48  Failed Object -> setProtectionPoints()")
	#49
	def test_ghost_name(self):
		pGhost.setName("Blinky")
		self.assertEqual(pGhost.getName(), "Blinky", "#49  Failed Ghost -> setName()")
	#50
	def test_ghost_long_description(self):
		pGhost.setLongDescription("Long Description")
		self.assertEqual(pGhost.getLongDescription(), "Long Description", "#50  Failed Ghost -> setLongDescription()")
	#51
	def test_ghost_short_description(self):
		pGhost.setShortDescription("Short Description")
		self.assertEqual(pGhost.getShortDescription(), "Short Description", "#51  Failed Ghost -> getShortDescription()")
	#52
	def test_ghost_location(self):
		pGhost.setLocation("Bedroom")
		self.assertEqual(pGhost.getLocation(), "Bedroom", "#52  Failed Ghost -> setLocation()")
	#53
	def test_ghost_health(self):
		pGhost.setHealth(18)
		self.assertEqual(pGhost.getHealth(), 18, "#53  Failed Ghost -> setHealth()")
	#54
	def test_ghost_damage_points(self):
		pGhost.setDamagePoints(34)
		self.assertEqual(pGhost.getDamagePoints(), 34, "#54  Failed Ghost -> setDamagePoints()")
	
	
if __name__ == '__main__':
	unittest.main()
