# Follow along lecture exercises
x = 2

print(x)

print(x*2)

y = "hello"

print(y)

z = x**2 + 5*x

print(z)

my_first_list = ['apple',1,'banana',2]
my_fruit_list = ['apple', 'banana']
my_int_list = [1,2,3]

cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

for f in my_fruit_list:
    print(f)

for f in my_fruit_list:
    pass
    print(f)

def sq_int(x):
    y = x**2
    return y

# Python Basic Exercises
# write a while loop
i = 6
while i < 12:
    print(i)
    i += 1

# write a loop using dictionary key-value pairs
for value in cal_lookup.values():
    print(value)

# write a function for is_odd and is_even
def is_odd(x):
    if x % 2 > 0:
        return True
    else:
        return False

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# loop over my_first_list and square number but print calories if fruit
integers = [1,2]
strings = ['apple','banana']

for item in my_first_list:
    if type(item)==int:
        print("This is a number")
    elif type(item)==str:
        print("This is a fruit")

# final answer
for x in my_first_list:
    if type(x)==int:
        x**2
    elif type(x)==str:
        for key, value in cal_lookup.items():
            if key == x:
                print(value)
    else:
         print('Error')

# write a loop using dictionary and return square value of each value in dictionary
for value in cal_lookup.values():
    value**2

# end of practice exercises


y = 5
x = 4

def describe_evenness(x):
    if is_even(x):
        print("It's even!")
    elif is_odd(x):
        print("It's odd!")
    else:
        print("It's neither even nor odd!")

# end of lecture exercise