# Define the screens of the shopping list app prototype
screens = [
    "Home Screen (List Overview)",
    "Add Item Screen",
    "Edit Item (Cart) Screen",
    "Checkout Page",
    "Order Confirmation Page"
]

# Print the total number of screens
print(f"Total prototype pages: {len(screens)}\n")

# Print the sequence of screens in the app
print("Screen Flow:")
for index, screen in enumerate(screens, start=1):
    print(f"{index}. {screen}")
