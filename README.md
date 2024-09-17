# Staff Requisition System

This Python program collects staff information, generates a unique Requisition ID, and calculates the total cost of requisitioned items. The system also determines approval status based on the total requisition value. 

## Features

- Collects and prints staff information including Date, Staff ID, Staff Name, and a unique Requisition ID.
- Takes input for requisition items, their quantity, and cost.
- Calculates the total cost of the requisition.
- Approves requisitions if the total cost is less than or equal to $500, otherwise marks it as pending.
- Displays all staff and requisition information.

## Program Flow

1. **Collect Staff Information**:  
   The program starts by prompting the user to input the staff details like Date, Staff ID, and Staff Name.
   
2. **Input Requisition Items**:  
   The user is asked to input three requisition items, their quantity, and the price per item. The total cost of the requisition is calculated.

3. **Requisition Approval**:  
   Based on the total cost, the system either approves or keeps the requisition pending. If the total value is less than or equal to $500, the requisition is approved; otherwise, it remains pending.

4. **Display Staff and Requisition Information**:  
   The system finally prints the staff details, requisition items, quantity, and total cost.

## How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/repositoryname.git
