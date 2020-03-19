import time
from datetime import timedelta

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


#   using zip function to pair words from 2 tuples
#   to form a dictionary

awords = {}
i = 0
for w in zip(tuple1, tuple2):
    awords[w[0] + w[1]] = i
    i += 1
# --------------------------------------------------
# Showing how to check the running time of a program.
# print method 1
start_time = time.time()
for w in awords:
    print(w, awords[w])
elapsed_time_secs = time.time() - start_time

print(
    f"Execution took: {timedelta(seconds=round(elapsed_time_secs))} secs(Wall clock time)")
# --------------------------------------------------
# print method 2
start_time = time.time()
for k, v in awords.items():
    print(v, k)
elapsed_time_secs = time.time() - start_time

print(
    f"Execution took: {timedelta(seconds=round(elapsed_time_secs))} secs(Wall clock time)")
# --------------------------------------------------
