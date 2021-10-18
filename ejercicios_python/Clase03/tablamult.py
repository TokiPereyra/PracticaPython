def tabla_mult(number):
    number = number
    header = ('0','1','2','3','4','5','6','7','8','9')
    print(f'{"":>4s} {"%4s %4s %4s %4s %4s %4s %4s %4s %4s %4s" % header}')
    print(f'{"":->55}')
    row = 0
    col = 0
    while row <= number:
        numbers = []
        num = 0
        for col in range (10):
            numbers.append(str(num))
            num += row
        numbers = tuple(numbers)
        print(f'{str(row)+":":>4s} {"%4s %4s %4s %4s %4s %4s %4s %4s %4s %4s" % numbers}')
        row += 1
    
tabla = tabla_mult(10)