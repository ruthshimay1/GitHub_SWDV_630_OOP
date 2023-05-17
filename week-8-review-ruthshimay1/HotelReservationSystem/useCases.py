#All the Test Cases
from src.reservation import Reservation
from operator import attrgetter
from datetime import date
from dateutil.relativedelta import relativedelta

'''

How the Reservation class works:

The Reservation class takes 4 parameters: number of standard rooms, number of 
deluxe rooms, and number of executive rooms, along with the number of days the
calendar looks ahead.

Example: R = Reservation(10,10,10,30) means that there are 10 of each room in
the hotel, and the user can book up to 30 days ahead.

Methods:

The addCustomer() method takes in first/last name, number of guests, and phone #

The makeReservation() and modifyReservation() methods require an ID, and check 
in/out dates of a customer. An ID is generated automatically when the customer is added, it's the
firstname and lastname initial along with last 4 digits of the phone number.

'''





'''Since you will run this program at a different date, everything is relative to the 
date you run the program, i.e. 'today's date'''


#get today's date and convert to a tuple

dateToday = date.today()

def testCase1():
    
    
    ''' This is a normal usecase, with 10 rooms in each suite, 45 days lookahead, and 2 random bookings
    The purpose here is to ensure that these 2 bookings can be made and modified, provided 
    you choose the correct rooms (as per prompt)'''
    
    date1 = attrgetter(*Reservation.attrs)(dateToday)
    #3 days from today
    date2 = dateToday + relativedelta(days = 3)
    date2 = attrgetter(*Reservation.attrs)(date2) 
    #6 days from today
    date3 = dateToday + relativedelta(days = 6)
    date3 = attrgetter(*Reservation.attrs)(date3) 
    #9 days from today
    date4 = dateToday + relativedelta(days = 9)
    date4 = attrgetter(*Reservation.attrs)(date4)      
    
    reservation = Reservation(10, 10, 10, 45)
    reservation.addCustomer('Sam', 'Allen', 0, 2401239876)
    reservation.addCustomer('Raphael', 'Arthur', 0, 2223435678)
    #Choose different dates to completely avoid any conflicts
    reservation.makeReservation('SA9876', date1, date2)
    reservation.makeReservation('RA5678', date3, date4)
    
    #This is your choice, you can choose any random dates here, and modify anyone
    reservation.modifyReservation('SA9876', date1, date4)


def testCase2():
    

    '''In this usecase, 2 customers will be added, book the first customer which sells out the hotel, then customer 1 
    canceled his/her reservation and refund is issued, and then customer 2 was able to make a reservation.'''

    dateIn = attrgetter(*Reservation.attrs)(dateToday)
    dateOut = dateToday + relativedelta(days = 1)
    dateOut = attrgetter(*Reservation.attrs)(dateOut)
    
    reservation = Reservation(0, 1, 0, 1)
    reservation.addCustomer('Sam', 'Allen', 0, 2401239876)
    reservation.addCustomer('John', 'Doe', 0, 3012349076)
    reservation.makeReservation('SA9876', dateIn, dateOut)
    reservation.cancelReservation('SA9876')
    #John should be able to make a reservation 
    reservation.makeReservation('JD9076', dateIn, dateOut)
    
    #Expected output, both reservation invoices
    
def testCase3():
    
    '''This is another usecase in which customers can not have overlapping rooms.'''


    dateVin = dateToday + relativedelta(days = 1)
    dateVin = attrgetter(*Reservation.attrs)(dateVin)
    #next week
    dateVout = dateToday + relativedelta(days = 7)
    dateVout = attrgetter(*Reservation.attrs)(dateVout)
    #11 days from today
    dateVout2 = dateToday + relativedelta(days = 11)
    dateVout2 = attrgetter(*Reservation.attrs)(dateVout2)    
    #5 days from today
    dateJin = dateToday + relativedelta(days = 5)
    dateJin = attrgetter(*Reservation.attrs)(dateJin)   
    #13 days from today
    dateJout = dateToday + relativedelta(days = 13)
    dateJout = attrgetter(*Reservation.attrs)(dateJout)  
    
    reservation = Reservation(1, 1, 1, 30)
    reservation.addCustomer('Sam', 'Allen', 0, 2401239876)
    reservation.addCustomer('John', 'Doe', 0, 3012349076)
    reservation.makeReservation('SA9876', dateVin, dateVout)
    #This reservation should not be booked
    reservation.makeReservation('SA9876', dateVin, dateVout2)
    #This reservation should not show Sam's room selection due to overlapping dates
    #since dateJin is before dateVout
    reservation.makeReservation('JD9076', dateJin, dateJout)
    
def testCase4():

    ''' This usecase is to show customers can not make booking with overlapping dates.
    
    1 room is available, the calendar is available 6 days ahead from today, customer 1 books first 3 days, customer 2 books next 3.
    Customer 1 attempts to modify their reservation whilst choosing dates that overlap with customer 2's booking The purpose of this 
    test is to ensure that Customer 1 should not be able to modify his.
    
    '''
    #reservation since customer 2 has a conflicting booking
    
    dateVIn = attrgetter(*Reservation.attrs)(dateToday)
    #3 days from today
    dateOut = dateToday + relativedelta(days = 3)
    dateOut = attrgetter(*Reservation.attrs)(dateOut) 
    #6 days from today
    dateOut2 = dateToday + relativedelta(days = 6)
    dateOut2 = attrgetter(*Reservation.attrs)(dateOut2) 
    #4 days from today
    dateOut3 = dateToday + relativedelta(days = 4)
    dateOut3 = attrgetter(*Reservation.attrs)(dateOut3) 
    
    reservation = Reservation(0, 1, 0, 6)
    reservation.addCustomer('Sam', 'Allen', 0, 2401239876)
    reservation.addCustomer('John', 'Doe', 0, 3012349076)
    reservation.makeReservation('SA9876', dateVIn, dateOut)
    reservation.makeReservation('JD9076', dateOut, dateOut2)
    #Sam's reservation should not be able to modify due to conflict
    #Attempt to modify dates with checkout date conflicting with John
    reservation.modifyReservation('SA9876', dateVIn, dateOut3)
    #The expected output should be the dates resetting and Vin being able to rebook the same room




def testCase5():
    
  
    
    ''' In this use case, a user accidentally has entered 0 rooms and 0 days, in which case the hotel defaults
    to having 1 standard room only. The calender will make the booking to 1 day by default.This means that the user can only 
    book today's date in 1 room!'''
    

    #get the date tuple from the object via 'attrgetter()'
    dateIn = attrgetter(*Reservation.attrs)(dateToday)
    dateOut = dateToday + relativedelta(days = 1)
    dateOut = attrgetter(*Reservation.attrs)(dateOut)
    reservation = Reservation(0, 0, 0, 0)
    reservation.addCustomer('Sam', 'Allen', 0, 2401239876)
    reservation.makeReservation('SA9876', dateIn, dateOut)
   
    
    #Expected output: 'SA9876 reservation summary will be printed'

    
    
    
    