from typing import Any, Optional
from list_ import List
class List(list):
    __CRITERION_FUNCTION = {}

    def add_criterion(self, criterion_key: str, criterion_function) -> None:
        self.__CRITERION_FUNCTION[criterion_key] = criterion_function

# 1. Definimos la clase Superheroe basándonos en los datos del enunciado

class Superheroe:

    def __init__(self, nombre, anio_aparicion, casa_comic, biografia):

        self.name = nombre

        self.year = anio_aparicion

        self.house = casa_comic

        self.bio = biografia



    def __str__(self):

        return f"Nombre: {self.name} | Año: {self.year} | Casa: {self.house} | Bio: {self.bio[:30]}..."



# 2. Inicializamos la lista y cargamos algunos datos de prueba

lista_superheroes = List()



datos_prueba = [

    ("Linterna Verde", 1940, "DC", "Posee un anillo de poder."),

    ("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor de curación."),

    ("Dr. Strange", 1963, "DC", "Hechicero supremo, maestro de las artes místicas."), # Lo ponemos en DC a propósito para el punto c

    ("Iron Man", 1963, "Marvel", "Genio millonario con un traje de armadura tecnológica."),

    ("Capitana Marvel", 1968, "Marvel", "Piloto que obtuvo poderes cósmicos."),

    ("Mujer Maravilla", 1941, "DC", "Princesa amazona."),

    ("Flash", 1940, "DC", "El hombre más rápido del mundo."),

    ("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia."),

    ("Batman", 1939, "DC", "Usa un traje oscuro y artilugios."),

    ("Superman", 1938, "DC", "El último hijo de Krypton."),

    ("Spider-Man", 1962, "Marvel", "Trepamuros de Nueva York.")

]



for d in datos_prueba:

    lista_superheroes.append(Superheroe(d[0], d[1], d[2], d[3]))





# --- RESOLUCIÓN DE LOS INCISOS ---



# Funciones de criterio para usar con nuestro TDA List

def by_name(item):

    return item.name



def by_year(item):

    return item.year



lista_superheroes.add_criterion('name', by_name)

lista_superheroes.add_criterion('year', by_year)





print("\n--- a. Eliminar Linterna Verde ---")

eliminado = lista_superheroes.delete_value("Linterna Verde", 'name')

if eliminado:

    print(f"Eliminado: {eliminado.name}")





print("\n--- b. Mostrar año de aparición de Wolverine ---")

pos_wolverine = lista_superheroes.search("Wolverine", 'name')

if pos_wolverine is not None:

    print(f"Wolverine apareció en: {lista_superheroes[pos_wolverine].year}")





print("\n--- c. Cambiar la casa de Dr. Strange a Marvel ---")

pos_strange = lista_superheroes.search("Dr. Strange", 'name')

if pos_strange is not None:

    lista_superheroes[pos_strange].house = "Marvel"

    print(f"Dr. Strange ahora pertenece a: {lista_superheroes[pos_strange].house}")





print("\n--- d. Biografía con 'traje' o 'armadura' ---")

# Usamos el método de tu clase List

lista_superheroes.filter_contain_on_bio(["traje", "armadura"])





print("\n--- e. Superhéroes anteriores a 1963 (Nombre y Casa) ---")

# Ordenamos por año para que quede prolijo (opcional, pero buena práctica)

lista_superheroes.sort_by_criterion('year')

for heroe in lista_superheroes:

    if heroe.year < 1963:

        print(f"{heroe.name} ({heroe.house}) - {heroe.year}")





print("\n--- f. Mostrar casa de Capitana Marvel y Mujer Maravilla ---")

for nombre in ["Capitana Marvel", "Mujer Maravilla"]:

    pos = lista_superheroes.search(nombre, 'name')

    if pos is not None:

        print(f"{nombre} pertenece a: {lista_superheroes[pos].house}")





print("\n--- g. Mostrar información de Flash y Star-Lord ---")

for nombre in ["Flash", "Star-Lord"]:

    pos = lista_superheroes.search(nombre, 'name')

    if pos is not None:

        print(lista_superheroes[pos])





print("\n--- h. Superhéroes que comienzan con B, M y S ---")

# Tu clase List tiene un método específico para esto

lista_superheroes.filter_start_with(("B", "M", "S"))





print("\n--- i. Cuántos superhéroes hay de cada casa (Marvel y DC) ---")

contador_marvel = 0

contador_dc = 0



for heroe in lista_superheroes:

    if heroe.house == "Marvel":

        contador_marvel += 1

    elif heroe.house == "DC":

        contador_dc += 1



print(f"Total Marvel: {contador_marvel}")

print(f"Total DC: {contador_dc}") 





