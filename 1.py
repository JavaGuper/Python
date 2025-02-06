import json
# Abrir el fichero y leerlo con 'r' de read
with open('jugadors.json', 'r') as fitxer:
    llista_jugadors = json.load(fitxer)
#Funcion para ordenar la lista
ranking = sorted(llista_jugadors, key=lambda x: x["puntuacio"], reverse=True)
#Mostrar ranking
print("Ranking de jugadors")
for jugador in ranking:
    print(f"-{jugador['nom']} --> {jugador['puntuacio']}")