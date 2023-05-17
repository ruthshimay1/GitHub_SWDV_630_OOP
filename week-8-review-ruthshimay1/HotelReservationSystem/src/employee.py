#Employee Class
    
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self, first_name,last_name, address, gender):
      self.first_name = first_name
      self.last_name = last_name
      self.adress = address
      self.gender = gender

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
       return "\n{}: \n\tFrist Name: {}    Last Name: {} \n\tAddress: {} \n\tGender: {}".format(self.__class__. __name__, self.first_name, self.last_name, self.adress, self.gender)
   
class Receptionist(Employee):
   def get_role(self):
      return "Reception"

class Server(Employee):
   def get_role(self):
      return "Room Service"

class Manager(Employee):
   def get_role(self):
      return "Management"
  
class House_keeper(Employee):
    def get_role(self):
        return "House Keeping" 

class EmployeeFactory(object):
   """Abstract Factory"""
   @classmethod
   def create(cls, name, *args):
      name = name.lower().strip()

      if name == 'reception':
         return Receptionist(*args)
      elif name == 'server':
         return Server(*args)
      elif name == 'manager':
         return Manager(*args)
      elif name == 'house_keeper':
         return House_keeper(*args)
      
      
def main(): 
    print (EmployeeFactory.create('manager', 'Samri', 'Berhe', '13th street, DC', 'F')) 
    print (EmployeeFactory.create('reception', 'Sarah', 'Mehari', '28th street, MD', 'F')) 
    print (EmployeeFactory.create('server', 'Henok','Goitom', 'Mcmost Av, CA', 'M')) 
    print (EmployeeFactory.create('Customer', 'Halal','Ephrem', 'McGrath Blv, MD', 'M')) 
     
main()