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



def obfuscator(func):
    def wrapper():
        data = func()
        name = data['name']
        password = data['password']
        
        if len(name) <= 2:
            name_obfuscated = name
        else:
            name_obfuscated = name[0] + '*' * (len(name) - 2) + name[-1]
        
        password_obfuscated = '*' * len(password)
        
        return {
            'name': name_obfuscated,
            'password': password_obfuscated
        }
    return wrapper