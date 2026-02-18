def spam():  # Function to modify the global variable 'eggs'
    global eggs  # Declare 'eggs' as a global variable
    eggs = 'spam'  # Assign a new value to the global variable 'eggs'

eggs = 'global'  # Initialize the global variable 'eggs' with a string 'global'
spam()  # Call the function 'spam' to modify the global variable 'eggs'
print(eggs)  # Print the value of the global variable 'eggs' after modification