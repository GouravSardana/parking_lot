import unittest
import os
from parking import Parking


class TestParkingLot(unittest.TestCase):

	def test_create_parking_lot(self):
		parkingLot = Parking()
		res = parkingLot.createParkingCapacity(6)
		self.assertEqual(6,res)

	def test_park(self):
		parkingLot = Parking()
		res = parkingLot.createParkingCapacity(6)
		res = parkingLot.park("KA-01-HH-1234",15)
		self.assertNotEqual(0,res)

	def test_leave(self):
		parkingLot = Parking()
		res = parkingLot.createParkingCapacity(6)
		res = parkingLot.park("KA-01-HH-1254",5)
		res = parkingLot.vacantSlot(1)
		self.assertEqual(True,res)

	def test_getCarDetailsFromAge(self):
		parkingLot = Parking()
		res = parkingLot.createParkingCapacity(6)
		res = parkingLot.park("KA-01-HH-1234",15)
		res = parkingLot.park("KA-01-HH-9999",15)
		regnos = parkingLot.getCarDetailsFromDriverAge(15)
		self.assertIn("KA-01-HH-1234",regnos)
		self.assertIn("KA-01-HH-9999",regnos)

	def test_getSlotNoFromDriverAge(self):
		parkingLot = Parking()
		res = parkingLot.createParkingCapacity(6)
		res = parkingLot.park("KA-01-HH-1234",14)
		res = parkingLot.park("KA-01-HH-9999",15)
		slotno = parkingLot.getSlotNoFromDriverAge(15)
		self.assertEqual(2, int(slotno[0]))

	def test_getregistrationNumber(self):
		parkingLot = Parking()
		res = parkingLot.createParkingCapacity(6)
		res = parkingLot.park("KA-01-HH-9999",15)
		res = parkingLot.park("KA-01-HH-9449",15)
		registration_number = parkingLot.getDetailsFromRegisNumber("KA-01-HH-9999")
		self.assertEqual(1,registration_number)

if __name__ == '__main__':
	unittest.main()
