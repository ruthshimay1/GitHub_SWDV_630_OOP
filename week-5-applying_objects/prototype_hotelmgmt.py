import copy

class Prototype(object):

  def clone(self):
    return copy.deepcopy(self)

class Hoterl_Rooms(Prototype):
  def __init__(self, hotel_name,hotel_address, room_type, number_of_beds, smoking):
    self.hotel_name = hotel_name
    self.hoterl_address = hotel_address
    self.room_type = room_type
    self.number_of_beds = number_of_beds
    self.smoking = smoking

  def __str__(self):
    return '\n\tHotel: {hotel_name}     piAddress: {hotel_address} \n\tRoom type: {room_type}    Number of beds: {number_of_beds}    Smoking: {smoking}\n'.format(hotel_name = self.hotel_name, hotel_address = self.hoterl_address, room_type = self.room_type, number_of_beds= self.number_of_beds, smoking = self.smoking)


def main():
  room_1 = Hoterl_Rooms("Marriot", "Fenton street, MD", "FAMILY_SUITE", 4, 'No')
  
  room_2 = room_1.clone()
  room_2.number_of_beds = 1
  room_2.room_type = "standard"
  
  room_3 = room_2.clone()
  room_3.smoking = "YES"
  
  print (room_1)
  print(room_2)
  print(room_3)

main()