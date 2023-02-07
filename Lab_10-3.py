#Creator CS 1/23/2023

def double_stuff(a_list):
    return [i*2 for i in a_list]

#Test cases
print(double_stuff([1, 2, 3])) 
print(double_stuff([1, 2.5, 3])) 
print(double_stuff([1, 'hello', 3.5]))
