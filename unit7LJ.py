# Learning Journal Unit 7
# Create a Python dictionary that returns a list of values for each key. The key can be whatever type you want.

# Design the dictionary so that it could be useful for something meaningful to you. Create at least three different items in it. Invent the dictionary yourself. Do not copy the design or items from some other source.

# Next consider the invert_dict function from Section 11.5 of your textbook.

# From Section 11.5 of:
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press.


def invert_dict_given(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

# Modify this function so that it can invert your dictionary. In particular, the function will need to turn each of the list items into separate keys in the inverted dictionary.


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for item in val:
            inverse[item] = key
    return inverse


# Run your modified invert_dict function on your dictionary. Print the original dictionary and the inverted one.
d = {"Primary Contact": ["Jamie Malloy", "Hendrik Kurk", "Betty Wilson"], "Company": [
    "Accenture", "Salesforce", "BCG"], "Account Owner": ["Alex Shevelenko", "Tom Griffin", "Nikita Koroteav"]}

print("***Original Dictionary***")
print("-------------------------")
for key in d:
    print(key, d[key], sep=" ==> ")
inverse = invert_dict(d)
print("\n***Inverted Dictionary***")
print("-------------------------")
for key in inverse:
    print(key, inverse[key], sep=" ==> ")
# Include your Python program and the output in your Learning Journal submission.
print(inverse)
