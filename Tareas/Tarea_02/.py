# Usamos un bucle for para imprimir los números del 1 al 100
for numero in range(1, 101):
    print(numero)




# Usamos un bucle for para imprimir los números del 1 al 100 que son divisibles por 3
for numero in range(1, 101):
    if numero % 3 == 0:
        print(numero)




# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Calcular la suma de los dos números
resultado = numero1 + numero2

# Comprobar las condiciones y mostrar los mensajes apropiados
if resultado < 100:
    print("El resultado es menor a 100")
elif resultado <= 150:
    print("El resultado es mayor a 100, pero menor o igual a 150")
else:
    print("El resultado es mayor a 150")





    def evaluar_compras(presupuesto_mensual, ha_comprado_prendas_falsificadas, ha_comprado_accesorios_falsificados, gastos_prendas, gastos_accesorios):
    total_gastos = gastos_prendas + gastos_accesorios
    
    if ha_comprado_prendas_falsificadas or ha_comprado_accesorios_falsificados:
        mensaje = f"Has gastado un total de ${total_gastos:.2f} en tus compras, incluyendo productos falsificados."
    else:
        mensaje = "No has comprado prendas de vestir ni accesorios en los últimos 2 años."

    if total_gastos > presupuesto_mensual:
        exceso_gastos = total_gastos - presupuesto_mensual
        mensaje += f"\nHas gastado ${exceso_gastos:.2f} más de tu presupuesto mensual. ¡Necesitas administrar mejor tus gastos!"
    
    return mensaje

# Solicitar al usuario su presupuesto mensual
presupuesto_mensual = float(input("Ingresa tu presupuesto mensual: $"))

# Preguntar si ha comprado prendas de vestir y accesorios falsificados en los últimos 2 años
ha_comprado_prendas_falsificadas = input("¿Has comprado prendas de vestir falsificadas en los últimos 2 años? (Sí/No)").lower() == "sí"
ha_comprado_accesorios_falsificados = input("¿Has comprado accesorios falsificados en los últimos 2 años? (Sí/No)").lower() == "sí"

# Si ha comprado prendas de vestir, solicitar el monto gastado en prendas
if ha_comprado_prendas_falsificadas:
    gastos_prendas_falsificadas = float(input("¿Cuánto has gastado en prendas de vestir falsificadas? $"))
else:
    gastos_prendas_falsificadas = 0.0

# Si ha comprado accesorios, solicitar el monto gastado en accesorios
if ha_comprado_accesorios_falsificados:
    gastos_accesorios_falsificados = float(input("¿Cuánto has gastado en accesorios falsificados? $"))
else:
    gastos_accesorios_falsificados = 0.0

# Llamar a la función y mostrar el mensaje correspondiente
mensaje = evaluar_compras(
    presupuesto_mensual,
    ha_comprado_prendas_falsificadas,
    ha_comprado_accesorios_falsificados,
    gastos_prendas_falsificadas,
    gastos_accesorios_falsificados
)

print(mensaje)