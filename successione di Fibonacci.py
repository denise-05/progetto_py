def print_fibonacci(length):
    a = 1
    b = 1
    for i in range (length):
        print(a, end=" ")
        a, b = b, a + b
n = int(input('Quanti numeri?: ' ))
while(n < 0):
    n = int(input('Quanti numeri? Inserisci un numero positivo: ' ))
print_fibonacci(8)