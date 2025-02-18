
print("Ingresa tu nota: ")
nota = input()

print("Ingresa tu asistencia (en porcentaje): ")
asistencia = input()

nota = float(nota)
asistencia = int(asistencia)

if nota >= 61 and asistencia >= 80:
    print("Ganaste")
    print("te felicito!!!")
    print("sos el mejor")

else:
    print("Perdiste 😭")