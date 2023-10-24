# Shoe Inventory Management System

## Description

The **Shoe Inventory Management System** is a Python program that allows you to manage a list of shoes in an inventory. It provides various functionalities, including adding new shoes, viewing all shoes, restocking, searching for shoes by their unique codes, calculating the value of each item, and finding products with the highest quantity for sale. This project helps users keep track of their shoe inventory and make informed decisions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions and Classes](#functions-and-classes)
- [Menu Options](#menu-options)

## Installation

To run the **Shoe Inventory Management System**, follow these steps:

1. Clone the repository or download the Python script.

2. Ensure you have Python installed on your computer. If not, you can download and install it from the official [Python website](https://www.python.org/downloads/).

3. Open your preferred code editor or integrated development environment (IDE) to run the Python script.

4. Make sure you have a data file named `inventory.txt` in the same directory as the Python script. You can create this file to store shoe data.

## Usage

1. Run the Python script `shoe_inventory.py`.

2. The program will display a menu with several options. You can select an option by entering a number from 1 to 7.

3. Follow the on-screen instructions to perform various actions, such as viewing all shoes, adding new shoes, restocking, searching for shoes by their codes, calculating the value of each item, and finding products with the highest quantity for sale.

4. The program will provide feedback and results based on your selections.

5. You can exit the program by choosing option 7.

## Functions and Classes

- `Shoe` class: Represents a shoe product with attributes like country, code, product name, cost, and quantity.

- `read_shoes_data(file_name)`: Reads shoe data from a file and appends it to the shoe list.

- `capture_shoes()`: Captures and adds new shoe data to the inventory.

- `view_all()`: Displays a table of all shoes in the inventory.

- `re_stock()`: Restocks shoes and updates the quantity in the text file.

- `search_shoe(code)`: Searches for a shoe by its unique code and returns the shoe object.

- `value_per_item()`: Calculates and displays the value of each item in the inventory.

- `highest_qty()`: Finds the product with the highest quantity for sale.

## Menu Options

- **View all shoes**: Displays all shoes in the inventory.

- **Add new shoe**: Captures and adds new shoes to the inventory.

- **Re-stock shoes**: Restocks shoes with the lowest quantity.

- **Search for a shoe by code**: Searches for a shoe by its unique code.

- **Calculate value per item**: Calculates and displays the value of each item.

- **Find product with the highest quantity**: Finds and displays the product with the highest quantity for sale.

- **Exit**: Exits the program.

---

*The Shoe Inventory Management System is a tool to efficiently manage your shoe inventory and make informed decisions about restocking and product value. It is designed for educational purposes and practical inventory management.*
