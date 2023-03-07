from django.shortcuts import render
import math

def calculator(request):
    try:
        if request.method == 'POST':
            num1 = float(request.POST['num1'])
            num2 = float(request.POST['num2'])
            operation = request.POST['operation']
            result = float()
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                if num1 == num2:
                    result = "0"
                else:
                    result = num1 - num2
            elif operation == 'multiply':
                if num1 != 0 and num2 != 0:
                    result = num1 * num2
                elif num1 == 0 or num2 == 0:
                    result = "0"
            elif operation == 'divide':
                if num2 != 0 and num1 != 0:
                    result = num1 / num2
                elif num1 == 0:
                    result = "0"
                else:
                    return render(request, 'calculator.htm', {'result': "Invalido, no se puede divir por 0"})
            return render(request, 'calculator.htm', {'result': result})
        return render(request, 'calculator.htm')
    except:
        return render(request, 'calculator.htm')

def calculadora_cuadratica(request):
    try:
        if request.method == 'POST':
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            c = float(request.POST.get('c'))

            discriminant = b ** 2 - 4 * a * c

            if discriminant < 0:
                numeros = f"A = {a}, B = {b}, C = {c}"
                resultado = "La ecuación no tiene solución real"
            elif discriminant == 0:
                x = -b / (2 * a)
                numeros = f"A = {a}, B = {b}, C = {c}"
                resultado = f"La solución es x = {x}"
            else:
                x1 = (-b + math.sqrt(discriminant)) / (2 * a)
                x2 = (-b - math.sqrt(discriminant)) / (2 * a)
                numeros = f"A = {a}, B = {b}, C = {c}"
                resultado = f"Las soluciones son: x1 = {x1} y x2 = {x2}"

            return render(request, 'calculadora_cuadratica.html', {'resultado': resultado, "numeros": numeros})
        else:
            return render(request, 'calculadora_cuadratica.html', {})
    except:
        return render(request, 'calculadora_cuadratica.html', {})