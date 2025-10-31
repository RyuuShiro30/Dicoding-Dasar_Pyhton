x = 'Dicoding'
print(type(x))

"""
Output: 
<class 'str'>
"""

x = [1, 2.2, 'Dicoding']
print(type(x))

"""
Output: 
<class ‘list’>
"""

x = [1, 'Dicoding', True, 1.0]

print(x[2])

""" 
Output:
True
"""

x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

"""
Output:
['Indonesia', 2.2, 'Dicoding']
"""

x = (1, "Dicoding", 1+3j)
print(type(x))

"""
Output:
<class 'tuple'>
"""

x = {1,2,7,2,3,13,3}
print(x[0])

"""
Output:
'set' object is not subscriptable
"""

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(type(x))

"""
Output:
<class 'dict'>
"""

print(float(5))

"""
Output:
5.0
"""

print(int(5.6))
print(int(-5.6)) 

""" 
Output:
5
-5
"""

print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

"""
Output:
25
25
25.0
"""