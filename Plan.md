# **Concert Ticket Platform API Project**

This project consists of the following:

### Database

:star: Table one: Events - Event ID (PK), Event Name, Date, Location, Capacity, Number of tickets available
:star: Table two: Ticket_Sales - Transaction ID (PK), Event ID (FK), Date purchased, Amount

### Stored Procedure

We plan to have a stored procedure that adds a new ticket transaction. There will probably be a stored procedure that adds a new ticket transaction. Potentially tickets could also be returned, so a different store procedure would delete the corresponding transaction.

### Main File | Client Side

The client should be able to:

* Check upcoming events - All events and specific dates
* Buy a ticket
* Potentially return a ticket

### App.py | Server side

Will contain endpoints

### db_utils.py | Server side

Connect to DB
Get available tickets
Book ticket (put method -> update)


