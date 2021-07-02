def my_fact(n):
    total = 1
    for i in range(n):
        total *= i+1
    return total
print(my_fact(5))
