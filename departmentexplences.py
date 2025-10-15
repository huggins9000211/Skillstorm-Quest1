import csv



try:
    with open('city-of-seattle-2012-expenditures-dollars.csv', 'r') as file:
        reader = csv.reader(file)

        # Initialize variables
        depatmentcosts = {}

        # Skip the first row
        try:
            next(reader) 
        except StopIteration:
            print("The CSV file is empty or only contains one row.")

        for row in reader:

            department = row[0] if row[0].strip() else "Unspecified Department"
            cost = int(row[3]) if row[3].strip() else 0

            if depar in depatmentcosts:
                # If the department is in the dictionary, add the cost to the total.
                depatmentcosts[depar] += cost
            else:
                # If the department is not in the dictionary, add the department and cost to the dictionary.
                depatmentcosts[depar] = cost

        
        for department, cost in depatmentcosts.items():
            # Print the total cost for each department.
            print(f"{department:<10}: ${cost:,.2f}")


except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to access this file.")
except Exception as e:
    print(f"An error occurred: {e}")



"""
Solution 2: Does not use a dictionary. And has less loops making it faster if a larger dataset is used
Less flexable for more analysis and requires the data to be sorted alphabetically by department as it is in example file.


try:
    with open('city-of-seattle-2012-expenditures-dollars.csv', 'r') as file:
        reader = csv.reader(file)

        # Initialize variables
        department = ""
        cost = 0

        # Skip the first row
        try:
            next(reader) 
        except StopIteration:
            print("The CSV file is empty or only contains one row.")

        # Read the second row and set as starting values for department and cost
        try:
            second_row = next(reader)
            department = second_row[0]
            cost = int(second_row[3]) if second_row[3].strip() else 0
        except StopIteration:
            print("The CSV file does not contain a second row.")

        # Read the remaining rows and calculate the total cost for each department.
        for row in reader:
            # If the department is the same as the previous row, add the cost to the total.
            if row[0] == department:
                cost += int(row[3]) if row[3].strip() else 0
            else:
                # If the department is different, print the total cost for the previous department and start a new department.
                print(f"{department:<10}: ${cost:,.2f}")
                department = row[0]
                cost = int(row[3]) if row[3].strip() else 0
        # Print the total cost for the last department.
        print(f"\nUnspesified department: ${cost:,.2f}")

except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to access this file.")
except Exception as e:
    print(f"An error occurred: {e}")
"""
