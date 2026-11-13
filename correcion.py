ORDEN = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]


def promedio(valores: list[float]) -> float:
    suma = 0
    for v in valores:
        suma += v
    return suma / len(valores)


def maximo(valores: list[float]) -> float:
    mayor = valores[0]
    for v in valores:
        if v > mayor:
            mayor = v
    return mayor


def dias_sobre(valores: list[float], dias: list[str], umbral: float) -> list[str]:
    resultado = []
    for i in range(len(valores)):
        if valores[i] > umbral:
            resultado.append(dias[i])
    return resultado


def pedir_dia(mensaje: str) -> str:
    return input(mensaje).strip().capitalize()


def pedir_temperatura(mensaje: str):
    try:
        return float(input(mensaje).replace(",", "."))
    except ValueError:
        print("Temperatura no válida.")
        return None


def ordenar(datos: dict) -> dict:
    return {d: datos[d] for d in ORDEN if d in datos}


def mostrar_datos(datos: dict) -> None:
    dias = [d for d, t in datos.items() if t is not None]
    temps = [datos[d] for d in dias]

    if not temps:
        print("No hay temperaturas para calcular.")
        return

    prom = promedio(temps)
    calurosos = dias_sobre(temps, dias, prom)
    print(f"Promedio semanal: {prom:.1f}°C")
    print(f"Máxima semanal: {maximo(temps):.1f}°C")
    print(f"Días calurosos: {calurosos}")
    print(f"Total de días calurosos: {len(calurosos)}")


datos = {
    "Lun": 31.5,
    "Mar": 24.0,
    "Mie": 19.5,
    "Jue": 21.0,
    "Vie": 25.5,
    "Sab": 27.0,
    "Dom": 23.5,
}

mostrar_datos(datos)

opcion = 0

while opcion != 7:
    print("\n================")
    print("Opciones:")
    print("1. Eliminar día")
    print("2. Eliminar temperatura")
    print("3. Asignar día")
    print("4. Asignar temperatura")
    print("5. Mostrar datos")
    print("6. Revisar datos")
    print("7. Salir")

    try:
        opcion = int(input("Elige una opción (1-7): "))
    except ValueError:
        print("Escribe un número del 1 al 7.")
        continue

    if opcion == 1:
        dia = pedir_dia("Día a eliminar: ")
        if dia in datos:
            del datos[dia] 
            print(f"Día {dia} eliminado.")
        else:
            print("Ese día no está en la lista.")

    elif opcion == 2:
        dia = pedir_dia("Día cuya temperatura quieres eliminar: ")
        if dia in datos and datos[dia] is not None:
            datos[dia] = None 
            print(f"Temperatura del {dia} eliminada.")
        else:
            print("Ese día no existe o no tiene temperatura.")

    elif opcion == 3:
        dia = pedir_dia("Día a asignar: ")
        if dia not in ORDEN:
            print("Día no válido.")
        elif dia in datos:
            print("Ese día ya existe.")
        else:
            datos[dia] = None 
            datos = ordenar(datos)
            print(f"Día {dia} asignado.")

    elif opcion == 4:
        dia = pedir_dia("Asignar a qué día? (Lun, Mar, Mie, Jue, Vie, Sab, Dom): ")
        if dia in datos:
            temp = pedir_temperatura("Temperatura a asignar: ")
            if temp is not None:
                datos[dia] = temp
                print(f"Temperatura {temp} asignada a {dia}.")
        else:
            print("Día no válido. Primero asígnalo con la opción 3.")

    elif opcion == 5:
        mostrar_datos(datos)

    elif opcion == 6:
        faltan_temp = [d for d, t in datos.items() if t is None]
        faltan_dias = [d for d in ORDEN if d not in datos]
        print(f"Datos actuales: {datos}")
        print(f"Días sin temperatura: {faltan_temp}")
        print(f"Días de la semana que faltan: {faltan_dias}")

    elif opcion == 7:
        print("Byeeee :3.")

    else:
        print("Opción no válida. Elige del 1 al 7.")