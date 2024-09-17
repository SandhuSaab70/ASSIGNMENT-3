#Collects staff information and generates a unique RequistionID.
#gives information of date, staff ID, staff name, and RequistionID.
#prints all staff info

RequistionID = 10000  # Initialize RequistionID outside the function

def staff_info():
    print("Printing Staff Information:")
    Date = input("Date: ")
    staffID = input("StaffID: ")
    staffname = input("Staff name: ")
    global RequistionID  # Use global variable
    RequistionID += 1
    print(Date, staffID, staffname,"RequistionId is", RequistionID)
    
    return Date, staffID, staffname, RequistionID


#taking input of items
# making total of all items
# printing total of all items

def requisitions_total():
    Date, staffID, staffname, RequistionID = staff_info()
    requisitionitems = []  # Store multiple items
    for i in range(3):
        requisitionitem = input(f"Enter requisition item {i+1}: ")
        requisitionitems.append(requisitionitem)  # Add item to list
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter cost$: "))
    totalvalue = quantity * price
    print("total cost is",totalvalue)
    return Date, staffID, staffname, RequistionID, requisitionitems, quantity, totalvalue


# function for making decisions 
# this is get approval of total requisitions

def requistion_approval():
    Date, staffID, staffname, RequistionID, requisitionitems, quantity, totalvalue = requisitions_total()
    if totalvalue <= 500:
        print("Approve")
    else:
        print("Pending")
    return Date, staffID, staffname, RequistionID, requisitionitems, quantity, totalvalue


# this function is for getting staff's basic information and total requiaition

def display_requistons():
    Date, staffID, staffname, RequistionID, requisitionitems, quantity, totalvalue = requistion_approval()
    print("Staff ID:", staffID)
    print("Staff Name:", staffname)
    print("Date:", Date)
    print("Requistion ID:", RequistionID)
    print("Requistion Items:", ', '.join(requisitionitems))  # Print all items
    print("Quantity:", quantity)
    print("Total Value:", totalvalue)

display_requistons()