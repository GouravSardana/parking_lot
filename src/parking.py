import vehicle_details
import sys
import argparse
import input_fields

# input all the given string
input_fields


class Parking:
    def __init__(self):
        self.parking_capacity = 0
        self.slot_id = 0
        self.occupied_slots = 0
    

    def createParkingCapacity(self, parking_capacity):
        self.slots_list = [0] * parking_capacity
        self.parking_capacity = parking_capacity
        return self.parking_capacity
    

    def nearestEmptySlot(self):
        for i in range(len(self.slots_list)):
            if self.slots_list[i] == 0:
                return i
    

    def park(self, registration_number, driver_age):
        if self.occupied_slots < self.parking_capacity:
            slot_id = self.nearestEmptySlot()
            self.slots_list[slot_id] = vehicle_details.Car(registration_number, driver_age)
            self.slot_id = self.slot_id + 1
            self.occupied_slots = self.occupied_slots + 1
            return slot_id + 1
        else:
            return 0
    

    def vacantSlot(self, availableSlot):
        if self.occupied_slots > 0 and self.slots_list[availableSlot - 1] != 0:
            self.slots_list[availableSlot - 1] = 0
            self.occupied_slots = self.occupied_slots - 1
            return True
        else:
            return False
    

    def getCarDetailsFromDriverAge(self, driver_age):

        registration_number_list = []
        for parking_car in self.slots_list:
            if parking_car == 0:
                continue
            if parking_car.driver_age == driver_age:
                registration_number_list.append(parking_car.registration_number)
        return registration_number_list


    def getDetailsFromRegisNumber(self, registration_number):
        for i in range(len(self.slots_list)):
            if self.slots_list[i].registration_number == registration_number:
                return i+1
        return 0


    def getSlotNoFromDriverAge(self, driver_age):
        resultant_slots = []

        for i in range(len(self.slots_list)):
            if self.slots_list[i] == 0:
                continue
            if self.slots_list[i].driver_age == driver_age:
                resultant_slots.append(str(i+1))
        return resultant_slots
    
    def getCarDetailsWithSlotNumber(self, slot_number):
        result = []
        for i in range(len(self.slots_list)):
            if i == slot_number:
                result.append(self.slots_list[i].registration_number)
                result.append(self.slots_list[i].driver_age)
        return result


    def command(self, line):
        if line.startswith('Create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.createParkingCapacity(n)
            print('Created a parking lot with '+ str(res) +' slots')


        elif line.startswith('Park'):
            registration_number = line.split(' ')[1]
            age = line.split(' ')[3]
            res = self.park(registration_number, age)
            if res == 0:
                print("Sorry, parking lot is full")
            else:
                resultant_string = 'Car with vehicle registration number ' + '"{}"' + ' has been parked at slot number {}'
                print(resultant_string.format(str(registration_number), str(res)))


        elif line.startswith('Leave'):
            leave_slotid = int(line.split(' ')[1])
            status = self.vacantSlot(leave_slotid)
            car_details = self.getCarDetailsWithSlotNumber(leave_slotid)
            if status:
                if car_details == []:
                    print("Slot Number is already Free")
                else:
                    result = 'Slot number '+str(leave_slotid)+' vacated, the car with vehicle registration number ' + '"{}"' + ' left the space, the driver of the car was of age ' + str(car_details[1])
                    print(result.format(str(car_details[0])))


        elif line.startswith('Slot_numbers_for_driver_of_age'):
            driver_age = line.split(' ')[1]
            reg_numbers = self.getSlotNoFromDriverAge(driver_age)
            print(','.join(reg_numbers))


        elif line.startswith('Vehicle_registration_number_for_driver_of_age'):
            driver_age = line.split(' ')[1]
            slot_number = self.getCarDetailsFromDriverAge(driver_age)
            print(','.join(slot_number))


        elif line.startswith('Slot_number_for_car_with_number'):
            registration_number = line.split(' ')[1]
            slot_number = self.getDetailsFromRegisNumber(registration_number)
            if slot_number == 0:
                print("Not found")
            else:
                print(slot_number)
        elif line.startswith('exit'):
            exit(0)

            