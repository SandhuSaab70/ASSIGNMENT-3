# Staff Requisition System

This Python program gathers staff information, generates a unique Requisition ID, and calculates the total cost of requested items. It also determines the approval status based on the total requisition value.

## Characteristics

- Records and shows personnel data, such as the date, the employee's ID, their name, and a special Requisition ID.
- Requests the entry of the cost, quantity, and products on the requisition.
- Gives overall cost of all things that are requisitioned.
- If the total cost of items is $500 or less it is approved or it is marked as pending.
- Shows all personnel and requisition information.

## Operation

1. **Collect Staff Information**:  
   The program starts by asking the user to input staff details such as the date, Staff ID, and Staff Name.

2. **Input Requisition Items**:  
   The user is prompted to enter three requisition items, along with their quantities and prices. The total cost is then calculated.

3. **Requisition Approval**:  
   If the total cost of the request is $500 or less it is granted. The request status is pending if the cost is above $500.

4. **Display Information**:  
   The program outputs the staff details, requisition items, quantities, and the total value of the requisition.


## Code Structure

1. staff_info(): Collects staff details and generates a unique Requisition ID.
2. requisitions_total(): Collects requisition items, their quantity, and price, then calculates the total cost.
3. requistion_approval(): Depending on the total cost, decides if the requisition is accepted or pending.
4. display_requistons(): Displays all staff and requisition information.



