
"""
===========================================================================
    Universidad del Valle de Guatemala
    Algoritmos y Programación Básica
    Semestre 1, 2025
---------------------------------------------------------------------------
    Nombre del Archivo: menu.py
    Autor: Erick Marroquin
    Fecha de Creación: 18/02/25
    Descripción:
        Ejemplo de un menu con while
===========================================================================
"""


opcion = ""

while opcion != "salir":
    print("\n============================")
    print("=== BINEVENIDOS A MI APP ===")
    print("============================\n")
    print("Selecciona una de las siguientes opciones: \n")
    print("1. Proceso A")
    print("2. Proceso B\n")
    print("o escribe 'salir' para terminar\n")
    
    opcion = input("¿Cuál es tu opción? ")
    
    if opcion == "1":
        print("Ejecutanto proceso A....")
        
    elif opcion == "2":
        print("Ejecutando proceso B...")
        
    elif opcion == "salir":
        print("Que tengas lindo día!")
        
    else:
        print("Opción inválida... intentalo nuevamente 😫")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
