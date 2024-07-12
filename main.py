import random
import statistics
import csv

trabajadores = ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Pedro Rodríguez', 
                'Laura Hernández', 'Miguel Sánchez', 'Isabel Gómez', 'Francisco Díaz', 'Elena Fernández']

def agregar_sueldos(trabajadores):
    for index, trabajador in enumerate(trabajadores):
        sueldo = round(random.uniform(300000, 2500000), 2)
        trabajadores[index] = {'trabajador': trabajador, 'sueldo': sueldo}

def agrupar_sueldos():
    menores_800 = []
    entre_800_2m = []
    mayores_2m = []

    for trabajador in trabajadores:
        nombre = trabajador['trabajador']
        sueldo = trabajador['sueldo']

        if sueldo < 800000:
            menores_800.append((nombre, sueldo))
        elif sueldo >= 800000 and sueldo <= 2000000:
            entre_800_2m.append((nombre, sueldo))
        else:
            mayores_2m.append((nombre, sueldo))

    print(f"Sueldos menores a 800,000:")
    for nombre, sueldo in menores_800:
        print(f"{nombre}: {sueldo}")

    print(f"\nSueldos entre 800,000 y 2,000,000: ")
    for nombre, sueldo in entre_800_2m:
        print(f"{nombre}: {sueldo}")

    print(f"\nSueldos mayores a 2,000,000: ")
    for nombre, sueldo in mayores_2m:
        print(f"{nombre}: {sueldo}")

def estadisticas_sueldos(trabajadores):
    sueldos = [trabajador['sueldo'] for trabajador in trabajadores]
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    promedio_sueldos = statistics.mean(sueldos)

    print(f"\nSueldo más alto: {sueldo_mas_alto}")
    print(f"Sueldo más bajo: {sueldo_mas_bajo}")
    print(f"Promedio de sueldos: {promedio_sueldos:.2f}")

def detalle_sueldos(trabajadores):
    detalles = []

    for trabajador in trabajadores:
        nombre = trabajador['trabajador']
        sueldo_base = trabajador['sueldo']
        descuento_salud = sueldo_base * 0.07
        descuento_afp = sueldo_base * 0.12
        liq = sueldo_base - descuento_salud - descuento_afp

        detalles.append([nombre, sueldo_base, descuento_salud, descuento_afp, liq])

    return detalles


estadisticas_sueldos(trabajadores)

archivo_csv = 'detalle_sueldos.csv'

detalles = detalle_sueldos(trabajadores)

with open(archivo_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Sueldo Base', 'Descuento Salud (7%)', 'Descuento AFP (12%)', 'Sueldo Líquido'])
    writer.writerows(detalles)

print(f"Se ha exportado exitosamente el detalle de sueldos a {archivo_csv}")

print("Bienvenido al MENU!!!!")

while True:
    print('1  Para Asignar los sueldos')
    print('2.    Para agrupar los sueldos')
    print('3 Para mostrar estadisticas')
    print('4      . Para revisar el detalle de sueldos')

    opcion = int(input("INGRESE una  OPCION !!! : "))

    if opcion == 1:
        print("Se asiganaran los sueldos a todos los trabajadores ")
        for trabajador in trabajadores:
            print(trabajador)
        agregar_sueldos(trabajadores)
    elif opcion == 2:
        print("Se agruparan los sueldos de trabajadores en funcion del monto")
        agrupar_sueldos()
    elif opcion == 3:
        print("Se mostraran estadisticas de los sueldos")
        print("\n")
        estadisticas_sueldos(trabajadores)
    elif opcion == 4:
        print("Se mostrará el detalle de cada trabajador")
        print("\n")
        detalle_sueldos(trabajadores)
