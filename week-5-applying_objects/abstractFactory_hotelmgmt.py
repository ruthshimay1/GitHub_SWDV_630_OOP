"""I think I would make use of the Abstract Factory (and/or Factory), Prototype and Facade methods in my project. In this week's assignment, I will try to show roughly on how to use these methods in my project."""

from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
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
   
class Customer(Person):
    def get_role(self):
      return "client"

class Receptionist(Person):
   def get_role(self):
      return "Reception"

class Server(Person):
   def get_role(self):
      return "Room Service"

class Manager(Person):
   def get_role(self):
      return "Management"
  
class House_keeper(Person):
    def get_role(self):
        return "House Keeping" 

class PersonFactory(object):
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
      elif name == 'customer':
         return Customer(*args)

#testing Abstract Factory class
def main(): 
    print (PersonFactory.create('manager', 'Samri', 'Berhe', '13th street, DC', 'F')) 
    print (PersonFactory.create('reception', 'Sarah', 'Mehari', '28th street, MD', 'F')) 
    print (PersonFactory.create('server', 'Henok','Goitom', 'Mcmost Av, CA', 'M')) 
    print (PersonFactory.create('Customer', 'Halal','Ephrem', 'McGrath Blv, MD', 'M')) 
     
main()
