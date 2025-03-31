total_seats = int(input("Total Tickets: "))
booked_seats = []
Available_seats= [i for i in range(1,total_seats+1) if i not in booked_seats]

def book(book_seat):
    if book_seat in Available_seats :
        booked_seats.append(book_seat)
        Available_seats.remove(book_seat)
        while True:
            x=input("You want to book another ticket:(yes/no) ").lower()
            if x=='yes' or x=='y':
                n=int(input("Enter Seat Number:"))
                booked_seats.append(n)
                Available_seats.remove(n)
            else:
                break
    else:
        print(f'Seat {book_seat} is already booked or Invalid')
def cancel(cancel_seat):
    if cancel_seat in booked_seats:
        booked_seats.remove(cancel_seat)
        while True:
            x=input("You want to cancel another ticket:(y/n) ").lower()
            if x=='yes' or x=='y':
                n=int(input("Enter Seat Number:"))
                if n in booked_seats:
                    booked_seats.remove(n)
                else:
                    print(f"You didn't booked seat {n}")
            else:
                return
    else:
        print(f"You didn't booked seat {cancel_seat}")
def available():
    Available_seats=[i for i in range(1,total_seats+1) if i not in booked_seats]
    return f'Available_seats:{Available_seats}'
book(int(input("Enter Seat number to be booked: ")))
cancel(int(input("Enter Seat number to be cancelled: ")))
print(available())
