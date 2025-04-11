
cursos = {
    "progra": [
        {"nombre": "170", "horario": "Martes y Viernes de 10:40 a 12:15"},
        {"nombre": "110", "horario": "Martes y Viernes de 10:40 a 12:15"}
    ],
    "quimica": [
        {"nombre": "20", "horario": "Lunes y Miércoles de 7:00 a 8:40"}
    ]
}

# print(cursos["guate"])

curso_seleccionado = input("Ingrese el curso: ")


if curso_seleccionado in cursos:
    
    seccion_seleccionada = input("Ingrese el nombre de la sección")
    
    for seccion in cursos[curso_seleccionado]:
        if seccion["nombre"] == seccion_seleccionada:
            print(seccion)
    
else:
    print("NO")
