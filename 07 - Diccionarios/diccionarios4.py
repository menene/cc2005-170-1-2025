
cursos = [
    {
        "nombre": "Progra",
        "secciones":[
            {"nombre": "170", "dias": "M y V", "hora": "10:40 a 12:15"}
        ]
    }
]

curso = input("Ingrese el nombre del curso: ")
seccion = input("Ingrese el nombre de la seccion para el curso " + curso +": ")
dias = input("Ingrese los días de la seccion " + seccion + ": ")
horas = input("Ingrese el horario de la seccion " + seccion + ": ")

c = {
    "nombre": curso,
    "secciones": []
}

s = {
    "nombre": seccion,
    "dias": dias,
    "horas": horas
}

c["secciones"].append(s)

cursos.append(c)

print(cursos)
