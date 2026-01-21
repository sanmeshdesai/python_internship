# dict / object

# store data in key-value pair
# have methods and propertie
# readable and structuries
# mutable
# data access name indexing
# ordered
# no duplicate keys, unique, mutable


# dict = {
#     key: value
# }

# keys in single or double qoute

# emp = {
#     'id': 1,
#     'name': 'Nishant',
#     'skill': ['Python','AI','Devops'],
#     'CTC': '10LPA',
#     'role': 'Python Developer',
#     'company': 'Accenture',
#     'onRole': True,
#     'age': 23.5,
#     'age': 20,
#     'promotion': None   
# }

# print(emp)


# print(emp['role'])

# print(emp['skill'][1])

# print(emp['company'])

# # no duplicate key if keys duplicate consider last key
# print(emp['age'])

# emp['role'] = 'AI Eng'
# print(emp['role'])

# emp['email'] = 'nishant.works@gmail.com'
# print(emp)


# it will return keys
# for x in emp:
#     print(x)

# return keys
# for keys in emp.keys():
#     print(keys)

# return values
# for value in emp.values():
#     print(value)

# return key, value
# for items in emp.items():
#     print(items)

# print('role' in emp)

# print('role' not in emp)


# for key, value in emp.items():
#     print(f'{key}, {value}')


# print(len(emp))

# print(type(emp))

# get method --------------------------

# dict1 = {
#     "user" : "Omkar",
#     "emial" : "omkar@gmail.com",
# }

# dict2 = {
#     "address" : "Pune",
#     "skill" : "Python",
# }

# # dict3 = dict2
# dict3 = dict2.copy()

# dict2['skill'] = 'AI Engineer'
# dict2['role'] = 'Software Developer'



# print(dict1)
# print(dict2)
# print(dict3)


# update

# products = {
#     'productName' : 'Mac',
#     'productPrice' : '1Lac',
#     'productDetails' : {
#         'ram' : '16GB',
#         'rom' : '256GB',
#         'processor': 'm4'
#     }
# }

# print(products)

# products.update({'productOfferPrice': '80000', 'productBrand': 'Apple'})

# print(products)


# l3 = [1,2,3]
# a = tuple(l3)
# print(type(a))




# setDefault: key is present then default value 
# student = {
#     'name' : 'om',
#     'address' : 'Nagar',
#     'role': 'Mern Stack'
# }

# student.setdefault('role', 'Software Trainee' )

# print(student)

