from module5_mod import NumberProcessor

print("""🔍 Number Search Tool 🔍

This program will take list of numbers provided by you, and prompt you to enter a number to search for in the list. 

If the number is present in the list, the program will return the order in which it was first provided. 
If not, it will return -1. 
""")

processor = NumberProcessor()

while True:
    try:
        n_input = input("\n* Enter a positive integer (this will be size of the list of numbers): ")
        n = int(n_input)
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

for i in range(n):
    while True:
        try:
            num_input = input(f"\n* Enter number {i + 1}: ")
            num = int(num_input)  # Assuming numbers are integers
            processor.add_number(num)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

while True:
    try:
        x_input = input("\n* Enter an integer X to search: ")
        x = int(x_input)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

result = processor.find_number(x)
print(f"\n The result is... found at position {result}!") if result != -1 else print("\n The result is... -1 not found!")
