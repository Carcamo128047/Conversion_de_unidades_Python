def mostrar_menu_principal():
    print("=" * 45)
    print("      CONVERSOR DE UNIDADES FUNDAMENTALES")
    print("=" * 45)
    print("1. Longitud (Metros, Kilómetros, Centímetros, Millas, Pies)")
    print("2. Masa (Kilogramos, Gramos, Libras, Onzas)")
    print("3. Tiempo (Segundos, Minutos, Horas, Días)")
    print("4. Salir")
    print("=" * 45)


def convertir_longitud():
    print("\n--- CONVERSIÓN DE LONGITUD ---")
    print("Unidad base de referencia: Metro (m)")
    print("Escalas de conversión relativas al metro:")
    print(" • 1 Metro (m) = 1,000 milímetros (mm)")
    print(" • 1 Metro (m) = 100 centímetros (cm)")
    print(" • 1 Metro (m) = 0.001 kilómetros (km)")
    print(" • 1 Metro (m) ≈ 3.28084 pies (ft)")
    print(" • 1 Metro (m) ≈ 0.000621371 millas (mi)")
    print("-" * 40)

    print("Seleccione la unidad de origen:")
    print("1. Metros (m) | 2. Kilómetros (km) | 3. Centímetros (cm) | 4. Pies (ft) | 5. Millas (mi)")
    origen = input("Opción de origen (1-5): ")

    val = float(input("Ingrese el valor a convertir: "))

    # Factores para convertir cualquier unidad a metros (m)
    a_metros = {
        '1': 1.0,
        '2': 1000.0,
        '3': 0.01,
        '4': 0.3048,
        '5': 1609.34
    }

    if origen in a_metros:
        metros = val * a_metros[origen]
        print("\n--- RESULTADOS DE LA CONVERSIÓN ---")
        print(f"• Metros (m):        {metros:.4f}")
        print(f"• Kilómetros (km):   {metros / 1000.0:.6f}")
        print(f"• Centímetros (cm):  {metros * 100.0:.2f}")
        print(f"• Pies (ft):         {metros / 0.3048:.4f}")
        print(f"• Millas (mi):       {metros / 1609.34:.6f}")
    else:
        print("Opción no válida.")


def convertir_masa():
    print("\n--- CONVERSIÓN DE MASA ---")
    print("Unidad base de referencia: Kilogramo (kg)")
    print("Escalas de conversión relativas al kilogramo:")
    print(" • 1 Kilogramo (kg) = 1,000 gramos (g)")
    print(" • 1 Kilogramo (kg) = 1,000,000 miligramos (mg)")
    print(" • 1 Kilogramo (kg) ≈ 2.20462 libras (lb)")
    print(" • 1 Kilogramo (kg) ≈ 35.274 onzas (oz)")
    print("-" * 40)

    print("Seleccione la unidad de origen:")
    print("1. Kilogramos (kg) | 2. Gramos (g) | 3. Libras (lb) | 4. Onzas (oz)")
    origen = input("Opción de origen (1-4): ")

    val = float(input("Ingrese el valor a convertir: "))

    # Factores para convertir cualquier unidad a kilogramos (kg)
    a_kg = {
        '1': 1.0,
        '2': 0.001,
        '3': 0.453592,
        '4': 0.0283495
    }

    if origen in a_kg:
        kg = val * a_kg[origen]
        print("\n--- RESULTADOS DE LA CONVERSIÓN ---")
        print(f"• Kilogramos (kg): {kg:.4f}")
        print(f"• Gramos (g):      {kg * 1000.0:.2f}")
        print(f"• Libras (lb):     {kg / 0.453592:.4f}")
        print(f"• Onzas (oz):      {kg / 0.0283495:.4f}")
    else:
        print("Opción no válida.")


def convertir_tiempo():
    print("\n--- CONVERSIÓN DE TIEMPO ---")
    print("Unidad base de referencia: Segundo (s)")
    print("Escalas de conversión relativas al segundo:")
    print(" • 1 Minuto (min) = 60 segundos (s)")
    print(" • 1 Hora (h)     = 3,600 segundos (s)")
    print(" • 1 Día (d)      = 86,400 segundos (s)")
    print("-" * 40)

    print("Seleccione la unidad de origen:")
    print("1. Segundos (s) | 2. Minutos (min) | 3. Horas (h) | 4. Días (d)")
    origen = input("Opción de origen (1-4): ")

    val = float(input("Ingrese el valor a convertir: "))

    # Factores para convertir cualquier unidad a segundos (s)
    a_seg = {
        '1': 1.0,
        '2': 60.0,
        '3': 3600.0,
        '4': 86400.0
    }

    if origen in a_seg:
        seg = val * a_seg[origen]
        print("\n--- RESULTADOS DE LA CONVERSIÓN ---")
        print(f"• Segundos (s): {seg:.2f}")
        print(f"• Minutos (min): {seg / 60.0:.4f}")
        print(f"• Horas (h):     {seg / 3600.0:.4f}")
        print(f"• Días (d):      {seg / 86400.0:.6f}")
    else:
        print("Opción no válida.")


def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == '1':
            convertir_longitud()
        elif opcion == '2':
            convertir_masa()
        elif opcion == '3':
            convertir_tiempo()
        elif opcion == '4':
            print("\n¡Gracias por utilizar el conversor de unidades!")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.\n")
        
        input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()