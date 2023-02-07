#Creator CS 1/20/2023

# Initialize sum variable
sum = 0

# Use while loop to contune asking user for input 
while True:
    # Ask user for input
    num = int(input("Enter a number: "))
    
    # Check for value (-1)
    if num == -1:
    # display sum
        print("Sum of numbers: ", sum)
        break
    else:
        # Add input to sum
        sum += num
