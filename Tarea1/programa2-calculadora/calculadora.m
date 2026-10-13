operador = input('Elige la operacion (+, -, *, /): ', 's');
num1 = input('Ingresa el primer numero: ');
num2 = input('Ingresa el segundo numero: ');

% Evaluar la operación usando switch
switch operador
    case '+'
        resultado = num1 + num2;
        fprintf('\nResultado: %.2f + %.2f = %.2f\n', num1, num2, resultado);
        
    case '-'
        resultado = num1 - num2;
        fprintf('\nResultado: %.2f - %.2f = %.2f\n', num1, num2, resultado);
        
    case '*'
        resultado = num1 * num2;
        fprintf('\nResultado: %.2f * %.2f = %.2f\n', num1, num2, resultado);
        
    case '/'
        if num2 ~= 0
            resultado = num1 / num2;
            fprintf('\nResultado: %.2f / %.2f = %.2f\n', num1, num2, resultado);
        else
            disp('\nError: No se puede dividir entre cero.');
        end
        
    otherwise
        disp('\nError: Operador no valido.');
end