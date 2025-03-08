print("*****Welcome to Book Ticket Services*****")
seating = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

print("To Get The Arragement: 1")
print("To Book Seat: 2")
print("To Cancel Seat: 3")

c = input("enter the operation you want to perform: ")

def arrangement(seating):
    print("Seating Arrangement")
    for row in seating:
        print(row)

def book_seat(row,colm):
    if seating[row][colm] == 0 :
        seating[row][colm] = 1
        print(f"seat number {row}{colm} has been booked")
        print("###THANKS FOR CHOOSING US###")
    else:
        print(f"seat {row}{colm} has already booked")
        print("***Please Choose Another Seat*****")
def cancel_seat(row,colm):
    if seating[row][colm] == 1 :
        seating[row][colm] = 0
        print("**********************")
        print(f"Seat {row}{colm} is Canceled")
        print("******Visit Again*****")
    else:
        print(f"seat {row}{colm} is available")

if c == "1":
    arrangement(seating)
elif c== "2":
    print("enter the row and column you want to book")
    row = int(input("enter the row: "))
    colm = int(input("enter the colm: "))
    book_seat(row , colm)
    arrangement(seating)
elif c == "3":
    print("enter the row and column you want to cancel")
    row = int(input())
    colm = int(input())
    cancel_seat(row , colm)
    arrangement(seating)