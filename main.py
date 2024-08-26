# main.py
import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def menu():
    while True:
        print("\nCalculadora")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Dividir dos números")
        print("5. Sumar varios números")
        print("6. Salir")
        
        choice = input("Selecciona una opción (1-6): ")
        
        if choice == '1':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"La suma de {a} y {b} es {sumar.sumar(a, b)}")
        elif choice == '2':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"La resta de {a} y {b} es {resta.resta(a, b)}")
        elif choice == '3':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"La multiplicación de {a} y {b} es {multiplicacion.multiplicar(a, b)}")
        elif choice == '4':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            if b != 0:
                print(f"La división de {a} y {b} es {dividir.dividir(a, b)}")
            else:
                print("Error: División por cero no permitida.")
        elif choice == '5':
            numbers = list(map(float, input("Introduce los números separados por espacios: ").split()))
            print(f"La suma de los números es {suma_avanzada.suma_avanzada(*numbers)}")
        elif choice == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
