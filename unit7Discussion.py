# Tuples are faster than list
words = ('Buttonhole', 'pinpoint', 'axehead', 'goalpost', 'Luke Skywalker')
# Construct a dictionary from pairs
d = dict(enumerate(words))
print(d)
for key, value in d.items():
    print(f'{key} --> {value}')

# Using d.items() in the above code is faster because no lookup (d[key]) is involved

# for key in d:
#     print(f'{key} --> {d[key]}')  # Not efficient


tuple1 = ('Button', 'pin', 'axe', 'goal', 'Luke')
tuple2 = ('hole', 'point', 'head', 'post', ' Skywalker')

# Construct a dictionary from pairs
d1 = dict(zip(tuple1, tuple2))
print(d1)
