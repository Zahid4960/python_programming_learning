# Tuples are not immutable that means we can't update values of tuples.


friends = ("Mahin", "Shuhi", "Masum", "Leon", "Aunik")

print(friends) # ("Mahin", "Shuhi", "Masum", "Leon", "Aunik")

print(friends[0]) # Mahin
print(friends[1]) # Shuhi

print(friends[-1]) # Aunik
print(friends[-2]) # Leon

print(friends[1:3]) # ('Shuhi', 'Masum')

# friends[0] = "moinul"
# print(friends)  # Will throw error