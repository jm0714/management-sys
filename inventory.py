# import tabulate used to create a table later on in the code
from tabulate import tabulate

# the shoe class represents a shoe product with its attributes
# these attributes include country of production, unique code of the shoe, name of the shoe, the cost and quantity of the product
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
# this function returns the cost of one unit of the shoe
    def get_cost(self):
        return self.cost

# this function returns the quantity of the shoe available in inventory
    def get_quantity(self):
        return self.quantity

# this returns a string representation of a shoe object
# it is called to display shoe details when print("shoe") is used
    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

# the list will be used to store a list of objects of shoes.
shoes_list = []

#==========Functions outside the class==============
# this function opens inventory.txt, reads the file data and appends to the shoe list.
def read_shoes_data(file_name):
    try:
        with open(file_name, 'r') as file:
            next(file)  # skip the header line
            for line in file:
                country, code, product, cost, quantity = line.strip().split(',')
                cost = int(cost)
                quantity = int(quantity)
                shoe = Shoe(country, code, product, cost, quantity)
                shoes_list.append(shoe)
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

# this function allows user to capture shoe data, create shoe object and append in shoe list
def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = int(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)
    with open("inventory.txt", "a") as file:
        file.write(f"{country},{code},{product},{cost},{quantity}\n")

# iterates over shoe list and prints all shoes listed in the text file
# tabulate is used to store data in a table
def view_all():
    if not shoes_list:
        print("No shoes in the inventory.")
    else:
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        data = [(shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity) for shoe in shoes_list]
        print(tabulate(data, headers=headers, tablefmt="grid"))

# finds shoe object with lowest quantity and asks user to specify quantity for restock
# quantity is updated in text file
def re_stock():
    if not shoes_list:
        print("No shoes in the inventory.")
        return

    lowest_quantity_shoe = min(shoes_list, key=lambda shoe: shoe.quantity)
    print("Shoe with the lowest quantity:")
    print(lowest_quantity_shoe)

    add_quantity = int(input("Enter the quantity to be added: "))
    lowest_quantity_shoe.quantity += add_quantity

    with open("inventory.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            data = line.strip().split(',')
            if data[1] == lowest_quantity_shoe.code:
                data[-1] = str(lowest_quantity_shoe.quantity)
                line = ','.join(data) + '\n'
            file.write(line)
        file.truncate()

    print("Quantity updated.")

# this function searches for a shoe from the list using the unique code assigned to the shoe
# it returns the shoe object and prints it
def search_shoe(code):
    for shoe in shoes_list:
        if shoe.code == code:
            return shoe
    return None

# this function calculates the total value for each item using the formula cost * quantity
def value_per_item():
    if not shoes_list:
        print("No shoes in the inventory.")
    else:
        for shoe in shoes_list:
            value = shoe.cost * shoe.quantity
            print(f"Product: {shoe.product}, Value: {value}")

# this function finds the product with the highest quantity and prints that it is for sale
def highest_qty():
    if not shoes_list:
        print("No shoes in the inventory.")
    else:
        highest_quantity_shoe = max(shoes_list, key=lambda shoe: shoe.quantity)
        print("Product with the highest quantity for sale:")
        print(highest_quantity_shoe)

# this function displays the menu options to the user
def display_menu():
    print('''\nMenu:
    1. View all shoes
    2. Add new shoe
    3. Re-stock shoes
    4. Search for a shoe by code
    5. Calculate value per item
    6. Find product with the highest quantity
    7. Exit''')

# this serves as the entry point of the program
# the previous functions are called based on the users choice from the above menu
# the necessary messages are displayed if user input is incorrect
def main():
    read_shoes_data("inventory.txt")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            view_all()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            code = input("Enter the code of the shoe to search: ")
            shoe = search_shoe(code)
            if shoe:
                print(shoe)
            else:
                print("Shoe not found.")
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()