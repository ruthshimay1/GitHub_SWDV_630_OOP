"""Code to use SQLAlchemy to store and retrieve objects from the internal SQLite database"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# connect with data base
engine = create_engine('sqlite:///SQLalchemy_db_wk_6.sqlite', echo = True)

# manage tables 
Base = declarative_base()  #base mapper

#__________________________________

class Employee(Base):
    __tablename__ = 'emplyees'
    
    emplyee_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(String(1))
    address = Column(String(100))
    title = Column(String(50))

    def __repr__(self):
         return "\n\tFrist Name: {}    Last Name: {} \n\tAddress: {} \n\tGender: {} Position: {} ID: {}".format(self.first_name, self.last_name, self.address, self.gender, self.title, self.emplyee_id)
     
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    employeeID = Column(Integer, ForeignKey('emplyees.emplyee_id'))

    employee = relationship("Employee", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
        
#______________________________________________________________
Employee.addresses = relationship("Address", order_by=Address.id, back_populates="employee")

Base.metadata.create_all(engine)   

#_________________________________________________________________      

Session = sessionmaker(bind=engine, autoflush=False)
session = Session()

#Adding data to the employees table   
session.add_all([
            Employee(emplyee_id = 101, first_name='Samri', last_name='Berhe', address='13th street, DD', gender ='F', title = 'Manager'),
            Employee(emplyee_id = 102,first_name='Saba', last_name='Kudus', address='Mcgrath Blv, MD', gender ='F', title = 'Accountant'),
            Employee(emplyee_id = 103, first_name='Brook', last_name='Stevens',  address='U street, DC', gender ='M', title = 'Data Engineer'),
            Employee(emplyee_id = 104, first_name='Fidel', last_name='Malik',  address='Connecticut Ave, VA', gender ='M', title = 'Head Chef'),
            Employee(emplyee_id = 105, first_name='Fidel', last_name='Amir',  address='Wisconson Ave, MD', gender ='M', title = 'Head Chef')
                ])

#Adding data to the addresses table
session.add_all([
        Address(id = 11, email_address='samri@hotel.com', employeeID=101),
        Address(id = 12, email_address='samri_b@gmail.com', employeeID=101),
        Address(id = 13, email_address='saba@hotel.com', employeeID=102),
        Address(id = 14, email_address='saba_01@prog.net', employeeID=102),
        Address(id = 15, email_address='brook@hotel.com', employeeID=103),
        Address(id = 16, email_address='brook_stev@gmail.com',employeeID=103),        
        Address(id = 17, email_address='fidel_m@hotel.com', employeeID=104),
        Address(id = 18, email_address='fidel_99@fidel.com', employeeID=104),
        Address(id = 19, email_address='fidel_a@hotel.com', employeeID=105),
        Address(id = 20, email_address='fidel_amir@prog.net', employeeID=105)
        ])

# session.commit()
"""I have commented the session.commit() out once I have inserted data to test the db and prevent double entry which will throw primary key error"""

#___________________________________
#Testing the database

#test-1
for instance in session.query(Employee).order_by(Employee.first_name):
    print(instance.first_name, instance.last_name,instance.title )

#test-2
session.query(Employee).filter(Employee.first_name.in_(['fidel', 'saba'])).all()

#test-3
for u, a in session.query(Employee, Address).\
                    filter(Employee.emplyee_id == Address.employeeID).\
                    filter(Address.employeeID == 101).\
                    all():
         print(u)
         print(a)
         
 #test-4-using join        
session.query(Employee).join(Address).\
             filter(Address.email_address == 'fidel_99@fidel.com').\
                all()                

#______________________________________
#Using Subqueries
#test-5
stmt = session.query(Address.employeeID, func.count('*').\
        label('address_count')).\
        group_by(Address.employeeID).subquery()

for u, count in session.query(Employee, stmt.c.address_count).\
    outerjoin(stmt, Employee.emplyee_id==stmt.c.employeeID).order_by(Employee.emplyee_id):
    print(u, count)
















