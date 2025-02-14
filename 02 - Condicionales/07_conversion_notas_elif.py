"""
===========================================================================
    Universidad del Valle de Guatemala
    Algoritmos y Programación Básica
    Semestre 1, 2025
---------------------------------------------------------------------------
    Nombre del Archivo: nombre_del_script.py
    Autor: Erick Marroquin
    Carnet: 123456
    Fecha de Creación: 11/02/25
    Descripción:
        Traduccion de notas
===========================================================================
"""

nota = input("Ingrese su nota: ")

nota = float(nota)

if nota >= 0 and nota <= 100:
    
    if nota >= 90:
        print("La nota es A")
    elif nota >= 80 and nota < 90:
        print("La nota es B")
    elif nota >= 70 and nota < 80:
        print("La nota es C")
    else:
        print("La nota es F")
else:
    print("Nota inválida")














