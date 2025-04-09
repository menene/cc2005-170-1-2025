
def es_vocal(letra):
    letra = letra.lower()
    
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    else:
        return False
    
def cuenta_vocales(palabra):
    cuenta = 0
    
    for letra in palabra:
        r = es_vocal(letra)
        
        if r:
            cuenta += 1
            
    return cuenta

def cuenta_consonantes(palabra):
    largo_total = len(palabra)
    vocales = cuenta_vocales(palabra)
    
    return largo_total - vocales
    
    
# print(es_vocal("A"))
# print(es_vocal("b"))
# print(es_vocal("c"))
# print(es_vocal("d"))
# print(es_vocal("e"))

print(cuenta_vocales("HOLA"))
print(cuenta_vocales("CACOFONIA"))
print(cuenta_vocales("CHANFLE"))
print(cuenta_vocales("ESTERNOCLEIDOMASTOIDEO"))

print(cuenta_consonantes("CHANFLE"))

palabra = "Hola"
primera_letra = palabra[0]
print(primera_letra)

ultima_letra = palabra[len(palabra) - 1]
ultima_letra = palabra[-1]
print(ultima_letra)


