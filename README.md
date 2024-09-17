# Staff Requisition System

This Python program gathers staff information, generates a unique Requisition ID, and calculates the total cost of requested items. It also determines the approval status based on the total requisition value.

## Features

- Captures and displays staff information, including Date, Staff ID, Staff Name, and a unique Requisition ID.
- Prompts for input of requisition items, their quantities, and cost.
- Calculates the total cost of all requisitioned items.
- Approves requisitions if the total cost is $500 or less; otherwise, marks them as pending.
- Displays all staff and requisition details.

## Workflow

1. **Collect Staff Information**:  
   The program starts by asking the user to input staff details such as the date, Staff ID, and Staff Name.

2. **Input Requisition Items**:  
   The user is prompted to enter three requisition items, along with their quantities and prices. The total cost is then calculated.

3. **Requisition Approval**:  
   Requisitions are approved if the total cost is $500 or less. If the cost exceeds $500, the requisition status is set to pending.

4. **Display Information**:  
   The program outputs the staff details, requisition items, quantities, and the total value of the requisition.

## Code Structure

1. staff_info(): Collects staff details and generates a unique Requisition ID.
2. requisitions_total(): Collects requisition items, their quantity, and price, then calculates the total cost.
3. requistion_approval(): Determines whether the requisition is approved or pending based on the total cost.
4. display_requistons(): Displays all staff and requisition information.


## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repositoryname.git
