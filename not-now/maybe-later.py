import pickle

# Define some variables to be saved
my_variable_1 = 'Hello, world!'
my_variable_2 = [1, 2, 3, 4, 5]

# Save the variables to a file
with open('my_variables.pickle', 'wb') as f:
    pickle.dump((my_variable_1, my_variable_2), f)

# Load the variables back into memory
with open('my_variables.pickle', 'rb') as f:
    my_variable_1, my_variable_2 = pickle.load(f)

# Print the values of the loaded variables
print(my_variable_1) # Output: 'Hello, world!'
print(my_variable_2) # Output: [1, 2, 3, 4, 5]