# HotelReservation

## A simple hotel reservation system


To get the code running, please download the repo and run **main.py**, then you can select a usecases.


The system is OOP based. A hotel can be defined with any number of rooms of 3 different room types: Standard, Deluxe, Executive (varying prices). The features are:


1. Any number of customers can be added. Each customer has a unique ID which is used to create/modify/cancel a booking.

2. Each room has a calendar that keeps track of bookings. The calendar length is customizable - i.e. the booking date range can be up to the user (90-120 days ahead is a reasonalbe). 


3. Reservations can be cancelled or modified. Refunds are also provided.

4. Each customer has an Invoice which prints the bill at the end and is updated if the reservation is cancelled or modified.

5. The program shows the user which rooms are available on the selected dates, along with the range of booking dates possible. If a room is booked for the dates requested, it will not show up on the list.


Constraints 

1. There is only one Hotel

2. If the user inputs incorrect values or data types, there is an error message provided, however the function has to be re-initialized again. 

3. There is no housekeeping or receptionist assigned to each room. 

4. The price of each room type is uniform and holidays are not considered.

5. If 2 customers have the same first name and last name letter, along with the same last 4 digits of phone number, this will conflict the ID, however what are the chances of that in real life!



## The time complexity for some of the methods is as follows: Let the variables represent:

1. **nRooms** = number of total Rooms
2. **nDays** = number of Calendar days (per room)
3. **nBookedDays** = number of days booked by the customer (<nDays) - (checkOutDate - checkInDate)

The 3 methods are

1. **checkIfHotelBooked()**: nRooms - since it has to search each room to see if it's booked or not.

2. **checkReservationDates()**: 2*nDays + 2*nBookedDays - since this method first extracts all the dates from the Calendar list, then checks if the checkinDate and checkOutDate falls within this list, along with getting their indices within the list. Obtaining these indices are important since then the second operation (+ nBookedDays) goes directly to the section of the calendar between the check-in/out dates. The second iteration of nBookedDays checks if the ID is 'none' or assigned to a customer ID. Each of these days has to be checked. 

3. **bookCustomer()**: nBookedDays - this method assigns the customer ID to the section of the calendar within the check-in/out dates, to each booked day. Since it is called after checkReservationDates(), there is no need to check again if the ID assigned to the room date is 'none' prior to booking. If this check was added here, the complexity would be 2*nBookedDays. The reservation flag inside checkReservationDates() value tells the makeReservation() method if the dates fall within the range and if there is no active booking present simultaneously.

## Class Diagram -

https://github.com/Maryville-SWDV-630-FA2022-1W/week-8-review-ruthshimay1/blob/main/class_diagram_htlmgt.pdf


## Sequence/Activity Diagrams - 

https://github.com/Maryville-SWDV-630-FA2022-1W/week-8-review-ruthshimay1/blob/main/sequence_diagram_htlmgmt.pdf


## UI -

https://github.com/Maryville-SWDV-630-FA2022-1W/week-8-review-ruthshimay1/blob/main/UI.pdf

## Architecture Diagram -

https://github.com/Maryville-SWDV-630-FA2022-1W/week-8-review-ruthshimay1/blob/main/architecture_diagram.pdf

## Use Case Elaboration

https://github.com/Maryville-SWDV-630-FA2022-1W/week-8-review-ruthshimay1/blob/main/usecase_elaboration.pdf


