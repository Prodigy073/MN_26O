#include <stdio.h>

int main() {
    char operador;
    float num1, num2, resultado;

    printf("Elige la operacion (+, -, *, /): ");
    scanf(" %c", &operador);

    printf("Ingresa el primer numero: ");
    scanf("%f", &num1);
    printf("Ingresa el segundo numero: ");
    scanf("%f", &num2);

    switch (operador) {
        case '+':
            resultado = num1 + num2;
            printf("\nResultado: %.2f + %.2f = %.2f\n", num1, num2, resultado);
            break;
            
        case '-':
            resultado = num1 - num2;
            printf("\nResultado: %.2f - %.2f = %.2f\n", num1, num2, resultado);
            break;
            
        case '*':
            resultado = num1 * num2;
            printf("\nResultado: %.2f * %.2f = %.2f\n", num1, num2, resultado);
            break;
            
        case '/':
            if (num2 != 0) {
                resultado = num1 / num2;
                printf("\nResultado: %.2f / %.2f = %.2f\n", num1, num2, resultado);
            } else {
                printf("\nError: No se puede dividir entre cero.\n");
            }
            break;
            
        default:
            printf("\nError: Operador no valido.\n");
            break;
    }

    return 0;
}