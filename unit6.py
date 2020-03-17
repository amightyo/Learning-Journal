# Write a Python program that does the following.

# Create a string that is a long series of words separated by spaces. The string is your own creative choice.
# It can be names, favorite foods, animals, anything. Just make it up yourself. Do not copy the string from another source.

skating_jumps = 'waltz salchow half-loop toe-loop flip loop lutz split axel'

# Turn the string into a list of words using split.
skating_jumps_list = skating_jumps.split()
print(skating_jumps_list)

# Delete three words from the list, but delete each one using a different kind of Python operation.
skating_jumps_list.pop(2)
del skating_jumps_list[5]
skating_jumps_list.remove('axel')
print(skating_jumps_list)

# Sort the list.
skating_jumps_list.sort()
print(skating_jumps_list)
# Add new words to the list (three or more) using three different kinds of Python operation.

# Turn the list of words back into a single string using join.

# Print the string.
