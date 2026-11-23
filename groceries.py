"""
Grocery list
4/22
Denzel Asamoah
25
Denzela1@umbc.edu

reads a given file that contains lines:
     item, amount and adds it to a dictionary, if an item 
     appears twice add their respective amounts together
     
     odd lines will be the item and odd lines +1 will be their respective amount,
     when 
     
     PEDAC problem, example, data structures, algorithm, code.
     P:reads a given file with each line having an item and amount seperated by a space anf comma
     input: filename
     output: printed verson of inventory {item, ammount}
     constraint: If item appears twice add together their respective amounts

     E: filename: market.txt
     market.txt lines: apple, 4
                        orange, 5
                        orange, 4
     
"""

def read_groceries(filename):
    f = open(filename)
    inventory = {}
    for line in f: #line in file
        item, amount = line.split(", ")
        amount = int(amount.strip())
        if item in inventory:#constraint case, as the for loop continues it checks for repeat items if item exists in inventory += its amount to the original amount
            inventory[item] += amount
        else:
            inventory[item] = amount
    return inventory


def display(dct):
    if dct == {}:
        print("This is empty :/")
    else:
        for item, amount in dct.items():
            print(f"{item}: {amount}")


def buy(wares, cart):
    line = input()
    parts = line.split()
    item = parts[0]
    amount = int(parts[1])

    if item not in wares:
        print("This item is not in the inventory.")
        return

    if amount > wares[item]:
        print("Requested amount of " + item + " exceeds stock")
        return

    wares[item] = wares[item] - amount

    if item in cart:
        cart[item] = cart[item] + amount
    else:
        cart[item] = amount

    print("Added to cart!")


def remove(wares, cart):
    line = input()
    parts = line.split()
    item = parts[0]
    amount = int(parts[1])

    if item not in cart:
        print("This item is not in the cart.")
        return

    if amount > cart[item]:
        print("Requested amount of " + item + " exceeds what's in cart")
        return

    cart[item] = cart[item] - amount
    wares[item] = wares[item] + amount

    if cart[item] == 0:
        del cart[item]
    print()
    print("Removed from cart!")

def make_menu(): #My code was being hella stubborn when I didnt do this please check my past attempts I swear they were identical
    print("What would you like to do?")
    print("1: Buy")
    print("2: Display Stock")
    print("3: Display Cart")
    print("4: Remove from Cart")
    print("5: Exit")

def shop(wares):
    cart = {}

    while True:
        make_menu()

        choice = input()

        if choice == "1":
            buy(wares, cart)
        elif choice == "2":
            print()
            print("Stock:")
            display(wares)
            print()
        elif choice == "3":
            print()
            print("Cart:")
            display(cart)
            print()
        elif choice == "4":
            remove(wares, cart)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    filename = input().strip()
    wares = read_groceries(filename)
    shop(wares)