"""
===========================================================================
    Universidad del Valle de Guatemala
    Algoritmos y Programación Básica
    Semestre 1, 2025
---------------------------------------------------------------------------
    Nombre del Archivo: nombre_del_script.py
    Autor: Erick Marroquin
    Carnet: 123456
    Fecha de Creación: 07/02/25
    Descripción:
        Programa para determininar impuestos
===========================================================================
"""

razon_social = input("Ingrese su razón social: ")
nit = input("Ingrese su NIT: ")
sueldo = int(input("Ingrese su sueldo: "))
print("------\n")

if sueldo <= 150000:
    print("Eres pequeño cotrobuyente")
    impuestos = (sueldo * 5) / 100
else:
    print("Eres cotribuyente ordinario")
    impuestos = (sueldo * 12) / 100
    
muni = (impuestos * 1.5) / 100
infra = (impuestos * 1) / 100
paz = (impuestos * 1) / 100

total = muni + infra + paz

print("\nEl total de tus impuestos es: ", impuestos)
print("------")
print("Para la muni (1.5%): ", muni)
print("Para la infraestructura (1%): ", infra)
print("Para la paz (1%): ", paz)
print("")
print("Total (3%): ", total)




