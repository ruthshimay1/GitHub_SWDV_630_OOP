from datetime import datetime 
# importing datetime module


class Person:  
    #Paret class  

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def __str__(self):
      return 'Full Name: {} {}'.format(self.first_name, self.last_name)
      
  

class Employee(Person):
    #child class 1 - Employee
    
  def __init__(self, employee_id, title,*args, **kwargs):
      
      self.employee_id = employee_id
      self.title = title
      super(Employee, self).__init__(*args, **kwargs)
   
  
  def get_employee_id(self):
      return self.employee_id
  
  def __str__(self):
        return 'Employee Full Name: {} {} \nEmployee_id:{} Title:{}'.format(self.first_name, self.last_name,self.employee_id, self.title)   
        
class Book(Person):
    #child class 2 - booking

    def __init__(self, checkin_date, checkout_date,room_type ,*args, **kwargs):
      
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.room_type = room_type    

        super(Book, self).__init__(*args, **kwargs)
    
    def get_Book_date(self):
        return  self.checkin_date, self.checkout_date        
      
    def get_reserved_room(self):
        return self.room_type 
    
    def __str__(self):
        return 'Customer Full Name: {} {} Room Type:{}\nCheckin Date:{} Checkout Date:{}'.format(self.first_name, self.last_name, self.get_reserved_room(),self.checkin_date, self.checkout_date)     


class Checkout(Person):
    #child class 3 -  Customer checkout 
    
  def __init__(self, checkin_date, checkout_date ,price, *args, **kwargs):
      
    self.checkin_date = checkin_date
    self.checkout_date = checkout_date
    self.price = price    

    super(Checkout, self).__init__(*args, **kwargs)
    

  def num_days_stayted(self):
        
    days_stayed = abs((datetime.strptime(self.checkin_date, "%Y-%m-%d") - datetime.strptime(self.checkout_date, "%Y-%m-%d")).days) 
    
    return days_stayed
 
  def payment(self):
      
        total_amount_due = self.num_days_stayted()*self.price
        
        return total_amount_due

  def __str__(self):
        return 'Customer Full Name: {} {} \nNumber Of Days Stayed:{} Amount Due: ${:.2f}'.format(self.first_name, self.last_name,self.num_days_stayted(), self.payment())     

#Testing code
person = Person("John", "Doe")    
print(person)  

employee_1 = Employee("0052", "Front Desk", "Andrew", "Frank")
print(employee_1)

customer_1 =Book("2022-8-10", "2022-8-15", 'standard - two bedroom', 'Saron', 'Tekle')
print(customer_1)         

customer_1_checkout = Checkout("2022-8-10", "2022-8-15", 150.99, 'Saron', 'Tekle')

print(customer_1_checkout)
          
          
    
  