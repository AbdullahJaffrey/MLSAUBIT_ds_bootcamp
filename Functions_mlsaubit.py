def maximun(arr):
    maximum_value = max(arr)
    print("f Maximum Value: {maximum_value}")


def square():
    lis1 = []
    for i in range(1,30):
        list1.append(i)
        list1.append(i**2)
    print(list1) 



def factorial(number):
    fac = 1
    if number > 0:
        for i in range(1, number+1):
            fac = fac * (i)
        print(fac)
    else:
        print('Can factorized Negative values')


def mult(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i, length):
            print(arr[i]*arr[j])

def upper_or_lower(text):
    upper, lower = 0, 0	
    for i in text:
        for j in i:
            if j == j.isupper():
                upper += 1
            else:
                lower += 1
    print(upper, lower)


def count_upper_lower(text):
    upper, lower = 0, 0
    for char in text:
        if char.isupper():
            upper += 1
        else:
            lower += 1
    print("Uppercase:", upper, "Lowercase:", lower)
    

lst1 = ['Jane','Lee', 'Will','Brie']

def hello(n):
    return f"Hello, {n}"

list(map(hello(), lst1)  