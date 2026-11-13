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


def posicion_para_insertar(dias: list[str], dia: str) -> int:
    posicion = 0
    for d in dias:
        if ORDEN.index(d) < ORDEN.index(dia):
            posicion += 1
    return posicion


def mostrar_datos(dias: list[str], temperaturas: list) -> None:
    dias_con_temp = []
    temps = []
    for i in range(len(dias)):
        if temperaturas[i] is not None:
            dias_con_temp.append(dias[i])
            temps.append(temperaturas[i])

    if not temps:
        print("No hay temperaturas para calcular.")
        return

    prom = promedio(temps)
    calurosos = dias_sobre(temps, dias_con_temp, prom)
    print(f"\nPromedio semanal: {prom:.1f}°C")
    print(f"Máxima semanal: {maximo(temps):.1f}°C")
    print(f"Días calurosos: {calurosos}")
    print(f"Total de días calurosos: {len(calurosos)}")

dias = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
temperaturas = [31.5, 24.0, 19.5, 21.0, 25.5, 27.0, 23.5]

mostrar_datos(dias, temperaturas)

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
        opcion = int(input("Opción: "))
    except ValueError:
        print("Elige una opción del 1 al 7.")
        continue

    if opcion == 1:
        dia = pedir_dia("Día a eliminar: ")
        if dia in dias:
            i = dias.index(dia)
            dias.pop(i)
            temperaturas.pop(i) 
            print(f"Día {dia} eliminado.")
        else:
            print("Ese día no está en la lista.")

    elif opcion == 2:
        dia = pedir_dia("Día cuya temperatura quieres eliminar: ")
        if dia in dias and temperaturas[dias.index(dia)] is not None:
            temperaturas[dias.index(dia)] = None 
            print(f"Temperatura del {dia} eliminada.")
        else:
            print("Ese día no existe o no tiene temperatura.")

    elif opcion == 3:
        dia = pedir_dia("Día a asignar: ")
        if dia not in ORDEN:
            print("Día no válido.")
        elif dia in dias:
            print("Ese día ya existe.")
        else:
            i = posicion_para_insertar(dias, dia)
            dias.insert(i, dia)
            temperaturas.insert(i, None) 
            print(f"Día {dia} asignado.")

    elif opcion == 4:
        dia = pedir_dia("Asignar a qué día? (Lun, Mar, Mie, Jue, Vie, Sab, Dom): ")
        if dia in dias:
            temp = pedir_temperatura("Temperatura a asignar: ")
            if temp is not None:
                temperaturas[dias.index(dia)] = temp
                print(f"Temperatura {temp} asignada a {dia}.")
        else:
            print("Día no válido. Primero asígnalo con la opción 3.")

    elif opcion == 5:
        mostrar_datos(dias, temperaturas)

    elif opcion == 6:
        sin_temp = []
        for i in range(len(dias)):
            if temperaturas[i] is None:
                sin_temp.append(dias[i])
        faltan_dias = []
        for d in ORDEN:
            if d not in dias:
                faltan_dias.append(d)
        print(f"Días: {dias}")
        print(f"Temperaturas: {temperaturas}")
        print(f"Días sin temperatura: {sin_temp}")
        print(f"Días de la semana que faltan: {faltan_dias}")

    elif opcion == 7:
        print("\nByeeee :3.")

    else:
        print("Opción no válida. Elige del 1 al 7.")