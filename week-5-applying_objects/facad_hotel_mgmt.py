"""Facade pattern to get access to hotel services through the Hoter_services"""

class Rooms:
    def get_Rooms(self):
        print("\nAccess to Rooms...")

    def get_avilable_rooms(self):
        print("\nAccess to  Rooms available at the moment...")

class Reservation:
	def get_reservation(self):
		print("\nAccess to Reservation...")
  
class Restaurant:	
	def get_restaurant(self):
		print("\nAccess To Restaurant Reservation...\n")

class Hotel_services_Facade:
    '''Facade'''

    def __init__(self):
        self.reservation = Reservation()
        self.Rooms = Rooms()
        self.restaurant = Restaurant()

    def get_hotel_services(self):
        self.reservation.get_reservation()
        self.Rooms.get_Rooms()
        self.Rooms.get_avilable_rooms()
        self.restaurant.get_restaurant()
	
""" main method to test code"""

def main():
	hotel_service = Hotel_services_Facade()
	hotel_service.get_hotel_services()
 
main()