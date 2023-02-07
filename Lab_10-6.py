#Creator CS 1/25/2023

def add_nums(num_list):
    while True:
        try:
            user_input = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    for i in range(len(num_list)):
        num_list[i] += user_input

    print("Passed list:", num_list, "; User input:", user_input)
