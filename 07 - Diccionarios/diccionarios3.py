
cursos = {}

for i in range(5):
    curso = input("Ingrese el nombre del curso: ")
    seccion = input("Ingrese el nombre de la seccion para el curso " + curso +": ")
    dias = input("Ingrese los días de la seccion " + seccion + ": ")
    horas = input("Ingrese el horario de la seccion " + seccion + ": ")

    cursos[curso] = {
        seccion: {
            "dias": dias,
            "horas": horas
        }
    }

print(cursos)



