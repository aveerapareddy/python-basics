# LISTS

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
print(friends[:3])
friends[1] = "Mike"
print(friends)

# LIST FUNCTIONS
lucky_numbers = [4, 1, 8, 5, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop()
print(friends)
friends.pop()
print(friends)
print(friends)
print(friends.index("Kevin"))
print(friends.count("Kevin"))
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
friends.extend(lucky_numbers)
friends.clear()
