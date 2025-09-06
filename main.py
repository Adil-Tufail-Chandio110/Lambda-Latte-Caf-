greet = "Welcome To Lambda Latte Cafe!"
print(greet.center(120))
print("\nPizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 80\nPizza Roll: Rs 150\n")

Menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80,
    'pizza roll': 150,
}

order_total = 0

while True:
    item = input("Enter the name of the item: ").lower()
    if item in Menu:
        order_total += Menu[item]
        print(f"'{item.title()}' has been added to your order.")
    else:
        print(f"Sorry, '{item}' is not available on the menu.")

    print("\nPizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 80\nPizza Roll: Rs 150\n")
    another = input("Do you want to add more items? (Yes/No): ").lower()

    if another != 'yes':
        break

print("\nThanks For Visiting Our Cafe.")
print(f"Your Total Bill is Rs {order_total}")