friends = ["Mahin", "Masum", "Leon", "Anik"]
lucky_numbers = [33, 7, 75, 18]

friends_copy = friends.copy()
lucky_numbers_copy = lucky_numbers.copy()


friends.append("Badhan") # ['Mahin', 'Masum', 'Leon', 'Anik', 'Badhan']
friends.insert(0, "Shuhi") # ['Shuhi', 'Mahin', 'Masum', 'Leon', 'Anik', 'Badhan']
friends.remove("Badhan") # ['Shuhi', 'Mahin', 'Masum', 'Leon', 'Anik']
friends.pop() # ['Shuhi', 'Mahin', 'Masum', 'Leon']

print(friends_copy) # ["Mahin", "Masum", "Leon", "Anik"]
print(lucky_numbers_copy) # [33, 7, 75, 18]

print(friends) 
print(friends.index("Shuhi")) # 0
print(friends.count("Shuhi")) # 1

friends.sort()
lucky_numbers.sort()
print(friends) # ['Leon', 'Mahin', 'Masum', 'Shuhi']
print(lucky_numbers) # [7, 18, 33, 75]

friends.reverse()
lucky_numbers.reverse()
print(friends) # ['Shuhi', 'Masum', 'Mahin', 'Leon']
print(lucky_numbers) # [75, 33, 18, 7]

friends.extend(lucky_numbers) # ['Shuhi', 'Masum', 'Mahin', 'Leon', 75, 33, 18, 7]
print(friends)

friends.clear()
print(friends)  # []