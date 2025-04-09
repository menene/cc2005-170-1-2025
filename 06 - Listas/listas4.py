
estudiante1 = ["1234", "Erick Marroquin", "Computacion", 100, 90, 75, 100, 80]

print(estudiante1)

datos_generales = estudiante1[:3]
notas = estudiante1[3:]

print(datos_generales)
print(notas)


n = len(notas)
suma = 0

for nota in notas:
    suma += nota
    
print(suma)
print(n)

promedio = (suma / n)

print("El promedio de", datos_generales[1], "es de:", promedio)




