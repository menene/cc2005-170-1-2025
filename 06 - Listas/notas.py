
def menu():
    return "=== Selecciona una de las opciones ===\n\n1. Nuevo estudiante\n2.Nueva nota\n3.Promedio Estudiante\n4.Promedio General\n5. Salir\n"

def promedio(estudiante):
    datos_generales = estudiante[:3]
    notas = estudiante[3:]
    
    n = len(notas)
    suma = 0
    for nota in notas:
        suma += nota
        
    return (suma / n)


estudiantes = []
opcion = ""

while opcion != "5":
    
    print(menu())
    
    print("\n======================\n")
    print(estudiantes)
    print("\n======================\n")
    
    opcion = input("Ingrese su opcion:")
    
    if opcion == "1":
        
        est = []
        
        carnet = input("Ingrese el carnet: ")
        
        est.append(carnet)
        
        nombre = input("Ingrese el nombre: ")
        
        est.append(nombre)
        
        carrera = input("Ingrese la carrera: ")
        
        est.append(carrera)
        
        estudiantes.append(est)
        
    elif opcion == "2":
        
        carnet = input("Ingrese el carnet: ")
        
        for actual in estudiantes:
            
            if actual[0] == carnet:
                nota = input("Ingrese la nota: ")
                nota = int(nota)
                
                actual.append(nota)
                
        
    elif opcion == "3":
        
        carnet = input("Ingrese el carnet: ")
        
        for actual in estudiantes:
            
            if actual[0] == carnet:
                
                promedio = promedio(actual)
                
                print("El promedio de ", actual[1], "es de:", promedio)
        
    elif opcion == "4":
        print("promedio general")
        
    elif opcion == "5":
        print("Muchas gracias!")
        
    else:
        print("Opción invalida... Intentalo nuevamente")
    
    
    
    