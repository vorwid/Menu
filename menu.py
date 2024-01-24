menu = {
    "Pizza Margherita": 25.99,
    "Spaghetti Bolognese": 19.99,
    "Caesar Salatka": 15.99,
    "Kurczak Alfredo": 22.99,
    "Cheeseburger": 17.99
}

order = []

def add_to_order(item):
    if item in menu:
        order.append(item)
        print(f"{item} dodano do zamowienia.")
    else:
        print(f"{item} nie jest dostepny w menu.")

def calculate_total():
    total = sum(menu[item] for item in order)
    return total

while True:
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")
    
    print("\n1. Dodaj do zamowienia")
    print("2. Podlicz zamowienie")
    print("3. Wyjscie")
    
    choice = input("Podaj swoj wybor: ")
    
    if choice == "1":
        item = input("Podaj nazwe pozycji: ")
        add_to_order(item)
    elif choice == "2":
        total = calculate_total()
        print(f"Calosc: ${total}")
    elif choice == "3":
        break
    else:
        print("Zly wybor. Sproboj jeszcze raz.")