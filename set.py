# collection of unique, unordered elements
# mutable
# store in { }
# no duplication allowed
# mathematical operation union, intercetion, difference
# doesnt maintain order


# sets = { 'omkar', 'aditya', 'nishant', 'om', 'snehit' }
# print(sets)

# empty set
# s = set()
# print(type(s))

# empty tuple
# a = ()
# print(type(a))

# empty dict
# d = {}


# movie_1 = { "Dhurandhar", "Saiyarra", "Dhadak 2", "Sairat", "Marco", "Pushpa 2", "KGF"}
# movie_2 = { "Salar", "Zindagi Na Milegi Dobara", "Mission Imposible", "Saiyarra" , "Tere Ishq Me" }

# print(movie_1)
# print(movie_2)

# union - combine both set
# print(movie_1.union(movie_2))
# print(movie_1 | movie_2)

# intersection - common
# print(movie_1 & movie_2)
# print(movie_1.intersection(movie_2))

# differemce - present in set1 but not in set2
# print(movie_1.difference(movie_2))
# print(movie_2 - movie_1)



# emp = {"Payal", "Alisha", "Shrushti", "Rutuja", "Samruddhi"}
# print(emp)

# add
# emp.add("PRatiksha")
# print(emp)

# update
# emp.update(["Kaya","Isha"])
# print(emp)

# pop - random element
# emp.pop()
# print(emp)

# remove - specific element, if element is not present show error
# emp.remove('Isha')
# print(emp)

# discard - specific element, if element is not present avoid error
# emp.discard('Isha')
# emp.clear()
# print(emp)

# num = {10,20,30,40,200,50}
# print(len(num))
# print(min(num))
# print(max(num))
# print(sorted(num))


# immutable set cannot perform operaation
users = frozenset(['john','doe','mark','sundar'])
# user.add('Andrew')
print(users)