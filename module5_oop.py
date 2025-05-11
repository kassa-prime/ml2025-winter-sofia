class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def find_number(self, x):
        try:
            index = self.numbers.index(x)
            return index + 1
        except ValueError:
            return -1

if __name__ == "__main__":
    print("""🔍 Number Search Tool 🔍

This program will take list of numbers provided by you, and prompt you to enter a number to search for in the list. 

If the number is present in the list, the program will return the order in which it was first provided. 
If not, it will return -1. 
""")
    processor = NumberProcessor()

    while True:
        try:
            n = int(input("\n* Enter a positive integer (this will be size of the list of numbers): "))
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
                num = int(num_input) # Assuming numbers are integers, can be float(num_input) if decimals are allowed
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
    print(f"\nThe result is... found at position {result}!") if result != -1 else print("\n The result is... -1 not found!")
