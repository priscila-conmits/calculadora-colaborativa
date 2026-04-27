# calculadora.py - calculadora colaborativa
def sumar(a, b):
  """Suma dos numeros."""

def mostrar_menu():
  """Muestra el menu de opciones."""
  print("\n=== calculadora colaborativa ===")
  print("1. Suma")
  print("0. Salir")

def main():
  while True:
    mostrar_menu()
    opcion = input("\nElegi una opcion: ")

    if opcion == "0":
      print("¡Hasta luego!")
      break
    elif opcion == "1":
      a = float(input("Primer numero: "))
      b = float(input("Segundo numero: "))
      print(f"Resultado: {a} + {b} = {sumar(a, b)}")
    else:
      print("Opcion no valida.")

if __name__ == "__main__":
  main()
  
