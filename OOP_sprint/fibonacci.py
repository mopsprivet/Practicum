def fibonacci(n):
    # Допишите функцию.
    num_0 = 0 
    num_1 = 1 

    for _ in range(n): 
        yield num_0 
        num_0, num_1 = num_1, num_0 + num_1 


sequence = fibonacci(10)
for number in sequence:
    print(number) 