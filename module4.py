print("""🔍 Number Search Tool 🔍

This program will take list of numbers provided by you, and prompt you to enter a number to search for in the list. 

If the number is present in the list, the program will return the order in which it was first provided. 
If not, it will return -1. 
""")
n = int(input("* Enter a positive integer (this will be size of the list of numbers): "))
numbers = []
for i in range(n):
    number = int(input(f"\n* Enter number {i+1}: "))
    numbers.append(number)
x = int(input("\n* Enter the number to search for: "))

if x in numbers:
    index = numbers.index(x) + 1
else:
    index = -1

print(f"\n The result is... found at position {index}!") if index != -1 else print("\n The result is... -1 not found!")