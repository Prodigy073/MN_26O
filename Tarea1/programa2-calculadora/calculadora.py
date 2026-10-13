operador = input("Elige la operacion (+, -, *, /): ")
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

if operador == '+':
    resultado = num1 + num2
    print(f"\nResultado: {num1:.2f} + {num2:.2f} = {resultado:.2f}")
elif operador == '-':
    resultado = num1 - num2
    print(f"\nResultado: {num1:.2f} - {num2:.2f} = {resultado:.2f}")
elif operador == '*':
    resultado = num1 * num2
    print(f"\nResultado: {num1:.2f} * {num2:.2f} = {resultado:.2f}")
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nResultado: {num1:.2f} / {num2:.2f} = {resultado:.2f}")
    else:
        print("\nError: No se puede dividir entre cero.")
else:
    print("\nError: Operador no valido.")

