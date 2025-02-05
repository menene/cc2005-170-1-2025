
print("Ingresa tu nota: ")
nota = input()

nota = float(nota)


if nota >= 61:
    print("Ingresa tu asistencia (en porcentaje): ")
    asistencia = input()
    
    asistencia = int(asistencia)
    
    if asistencia >= 80:
        print("Ganaste")
        print("te felicito!!!")
        print("sos el mejor")
        print("y vas a clase")
    else:
        print("Perdiste por asistencia 😭")
else:
    print("Perdiste por puntos 😭")
