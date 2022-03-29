
#Este es un juego en el que el el montañero Fausto te irá haciendo unas preguntas

#Por favor completa cada reto

#1. Definiendo la aventura

#Reto 1 - Pon tu respuesta después del print

print("Define el equipamiento para tu aventura de trekking Pokemon y su valor en Pokécuarto (moneda del juego):")
print()

repelente_max = 700
superpocion = 700
curatotal = 700
linterna = 350
cuerdahuida = 500
revivir = 1500
superball = 600

#Reto 2 - Pon tu respuesta después de cada print
print("Lista tres objetos del equipamiento: Nombre y valor")
print()

print('Repelente Máximo: ',repelente_max)
print('Superpoción: ',superpocion)
print('Cura total: ',curatotal)
print()

print("¿Puedes combinar elementos de tu equipo para prepararte mejor?")
print()

curar = superpocion + curatotal
capturar = superball + repelente_max
sobrevivir = linterna + cuerdahuida

print('Curar Pokémon: ',curar)
print('Capturar Pokémon: ',capturar)
print('Sobrevivir: ',sobrevivir)
print()

print("¿El precio de curar es menor al de capturar Pokémon?")
print()

print(curar < capturar)

print()

print("¿Cuanto valdría comprar una superball y una cuerda huida?")
print()

print('Valor: ',superball + cuerdahuida)
print()

print("¿Si tienes 700 puntos, te alcanza para comprar una cura total?")
print()

print(curatotal <= 700)

print()

#2. Tomando decisiones

#Reto 3 - Pon tu respuesta después del print
print("El montañero te dice: No debes colocar más de 5 tipos de objetos en tu mochila, y tampoco pasarte de 4000 Pokécuartos: ¿Cuales elementos colocarías?")
print()

if  linterna + cuerdahuida + superball + revivir + superpocion <= 4000:
    mochila = linterna + cuerdahuida + superball + revivir + superpocion
    print("El valor de los elementos es menor a 4000", mochila)

elif linterna + cuerdahuida + superball + revivir + curatotal <= 4000:
    mochila = linterna + cuerdahuida + superball + revivir + curatotal
    print("El valor de los elementos es menor a 4000", mochila)

else:
    print("Ninguna de tus elecciones era menor a 4000")
print()

#Reto 4 - Pon tu respuesta después del print
print ("¡Es tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle superballs")
print()

mochila2 = 0
while (mochila2 <= 4000):
    mochila2 += superball

mochila2 -= superball
print("Mochila 2 =", mochila2)
print()

#3. Almacenando equipamimento

#Reto 4 - Pon tu respuesta después del segundo print
print("Le hice una actualización a tu mochila, te dice el montañero, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")

mochila_nueva = {
    "linterna" : {"cantidad": 1, "valor unitario": linterna},
    "cuerda huida" : {"cantidad": 1, "valor unitario": cuerdahuida},
    "superpocion" : {"cantidad": 1, "valor unitario": superpocion},
    "repelente máximo" : {"cantidad": 1, "valor unitario": repelente_max},
    "revivir" : {"cantidad": 1, "valor unitario": revivir}
}

mochila2_nueva = {
    "superball" : {"cantidad": 6, "valor unitario": superball}
}

#Reto 5 - Pon tu respuesta después del print

print("Ahora, en esta aventura te van a acompañar 8 integrantes más, y te voy a pedir que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")
print()

Coche = [{}] * 8

for compartimiento in range(8):
    Coche[compartimiento] = {
        "linterna" : {"cantidad": 1, "valor unitario": linterna},
        "cuerda huida" : {"cantidad": 1, "valor unitario": cuerdahuida},
        "superpocion" : {"cantidad": 1, "valor unitario": superpocion},
        "repelente máximo" : {"cantidad": 1, "valor unitario": repelente_max},
        "revivir" : {"cantidad": 1, "valor unitario": revivir}
    }
    print("Ya esta lista la mochila para el compartimiento: ", compartimiento + 1)

for mochila in Coche:
    print(mochila)
    print()

#4. Organizandonos un poco

#Reto 6 - Pon tu respuesta después del segundo print
print("Te pido que para cuatro integrantes recolectes 3 elementos sin importar las cantidades que quieras adicionarles, y te da las siguientes opciones: cura total, superball y revivir")
print("Pero necesito que calcules el total de elementos que hay en tu equipo")
print()

def AgregarElementos():
    for compartimiento in range(4):
        Coche[compartimiento] = {
            "superball" : {"cantidad": 16, "valor unitario": superball},
            "curatotal" : {"cantidad": 10, "valor unitario": curatotal},
            "revivir" : {"cantidad": 12, "valor_unitario": revivir}
        }
    imprimir(Coche)
    TotalElementosEnMochilas(Coche)

def TotalElementosEnMochilas(Coche):
    total_elementos = {}
    
    print("Calculo del total de elementos:")
    for mochila in Coche: 
        for elemento, detalle in mochila.items(): 
            if elemento in total_elementos:
                total_elementos[elemento] += detalle["cantidad"]
            else:
                total_elementos[elemento] = detalle["cantidad"]
    print(total_elementos)
    print()
def imprimir(estructura):
    for objeto in estructura:
        print(objeto)
        print()

AgregarElementos()