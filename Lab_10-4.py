# Creator CS 1/23/2023

def indexed_names(names_list):
    return [f"{i}: {name}" for i, name in enumerate(names_list)]

#Test cases
print(indexed_names(["John", "Jane", "Bob"])) 
print(indexed_names(["Alice", "Bob", "Charlie"]))