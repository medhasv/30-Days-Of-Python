# Introduction
# Day 1 - 30DaysOfPython Challenge

print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool

print('***********medha\'s additions****************')
print(type(15))                  # Int
print(type(2.87))                # Float
print(type(9 + 7j))              # Complex
print(type('soreness'))          # String
print(type(['monday', 'wednesday','thursday']))           # List
print(type({'name' : 'medha', 'dad':'chary'})) # Dictionary
print(type({'she', 'him', 'theirs'}))    # Set
print(type(('a', 'b', 'c')))    # Tuple
print(type(7 == 8))              # Bool
print(type(10 >= 6))              # Bool

print('***********Chary\'s additions for collection operations****************')
# List operations
my_list = [1, 2, 3]
my_list.append(4)
my_list.extend([5, 6])
my_list.insert(0, 0)
my_list.remove(3)
popped = my_list.pop()
print('List:', my_list)
print('Popped:', popped)

# Dictionary operations
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
value = my_dict.get('a')
removed = my_dict.pop('b')
print('Dict:', my_dict)
print('Value:', value)
print('Removed:', removed)

# Set operations
my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6])
my_set.discard(2)
my_set.remove(3)
print('Set:', my_set)

# Tuple operations
my_tuple = (1, 2, 3, 2)
count_2 = my_tuple.count(2)
index_3 = my_tuple.index(3)
print('Tuple:', my_tuple)
print('Count of 2:', count_2)
print('Index of 3:', index_3)
