from list_ import List

# 1. Definimos las clases basándonos en los datos del enunciado
class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"  -> {self.nombre} | Nivel: {self.nivel} | Tipo: {self.tipo}/{self.subtipo}"

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        # Aquí aplicamos la lista de listas para los pokémons
        self.pokemons = List()

    def __str__(self):
        return f"Entrenador: {self.nombre} | Torneos: {self.torneos_ganados} | Victorias: {self.batallas_ganadas} | Derrotas: {self.batallas_perdidas}"


# 2. Inicializamos la lista principal y funciones de criterio
lista_entrenadores = List()

def by_nombre_entrenador(item):
    return item.nombre

def by_torneos(item):
    return item.torneos_ganados

def by_nombre_pokemon(item):
    return item.nombre

def by_nivel_pokemon(item):
    return item.nivel

lista_entrenadores.add_criterion('nombre', by_nombre_entrenador)
lista_entrenadores.add_criterion('torneos', by_torneos)

# Cargamos entrenadores de prueba
datos_entrenadores = [
    ("Ash Ketchum", 5, 20, 100),
    ("Misty", 4, 10, 80),
    ("Brock", 1, 40, 50),
    ("Rojo", 10, 0, 200)
]

for d in datos_entrenadores:
    lista_entrenadores.append(Entrenador(d[0], d[1], d[2], d[3]))

# Función auxiliar para inicializar las sublistas y agregar Pokémons rápido
def agregar_pokemon(nombre_entrenador, datos_pokemons):
    pos = lista_entrenadores.search(nombre_entrenador, 'nombre')
    if pos is not None:
        entrenador = lista_entrenadores[pos]
        entrenador.pokemons.add_criterion('nombre', by_nombre_pokemon)
        entrenador.pokemons.add_criterion('nivel', by_nivel_pokemon)
        for p in datos_pokemons:
            entrenador.pokemons.append(Pokemon(p[0], p[1], p[2], p[3]))

# Cargamos los Pokémons de cada entrenador
agregar_pokemon("Ash Ketchum", [
    ("Pikachu", 90, "Eléctrico", ""),
    ("Charizard", 85, "Fuego", "Volador"),
    ("Charizard", 85, "Fuego", "Volador"), # Repetido para el inciso i
    ("Wingull", 30, "Agua", "Volador")
])

agregar_pokemon("Misty", [
    ("Starmie", 65, "Agua", "Psíquico"),
    ("Psyduck", 25, "Agua", "")
])

agregar_pokemon("Brock", [
    ("Onix", 60, "Roca", "Tierra"),
    ("Terrakion", 70, "Roca", "Lucha")
])

agregar_pokemon("Rojo", [
    ("Venusaur", 95, "Planta", "Veneno"),
    ("Tyrantrum", 88, "Roca", "Dragón")
])


# --- RESOLUCIÓN DE LOS INCISOS ---

print("\n--- a. Cantidad de Pokémons de un entrenador (Ej: Ash) ---")
pos_ash = lista_entrenadores.search("Ash Ketchum", 'nombre')
if pos_ash is not None:
    print(f"Ash tiene {lista_entrenadores[pos_ash].pokemons.size()} Pokémons.")


print("\n--- b. Entrenadores con más de 3 torneos ganados ---")
for entrenador in lista_entrenadores:
    if entrenador.torneos_ganados > 3:
        print(f"{entrenador.nombre} ({entrenador.torneos_ganados} torneos)")


print("\n--- c. Pokémon de mayor nivel del entrenador con más torneos ---")
lista_entrenadores.sort_by_criterion('torneos') # El último será el de más torneos
mejor_entrenador = lista_entrenadores[-1]
mejor_entrenador.pokemons.sort_by_criterion('nivel') # El último será el de mayor nivel
mejor_pokemon = mejor_entrenador.pokemons[-1]
print(f"El mejor entrenador es {mejor_entrenador.nombre} y su mejor Pokémon es {mejor_pokemon.nombre} (Nivel {mejor_pokemon.nivel}).")


print("\n--- d. Mostrar todos los datos de un entrenador y sus Pokémons (Ej: Misty) ---")
pos_misty = lista_entrenadores.search("Misty", 'nombre')
if pos_misty is not None:
    print(lista_entrenadores[pos_misty])
    lista_entrenadores[pos_misty].pokemons.show()


print("\n--- e. Entrenadores con porcentaje de victorias mayor al 79% ---")
for entrenador in lista_entrenadores:
    total_batallas = entrenador.batallas_ganadas + entrenador.batallas_perdidas
    if total_batallas > 0:
        porcentaje = (entrenador.batallas_ganadas / total_batallas) * 100
        if porcentaje > 79:
            print(f"{entrenador.nombre}: {porcentaje:.2f}% de victorias")


print("\n--- f. Tienen Pokémons de tipo (Fuego y Planta) o (Agua/Volador) ---")
for entrenador in lista_entrenadores:
    for p in entrenador.pokemons:
        if (p.tipo == "Fuego" and p.subtipo == "Planta") or (p.tipo == "Agua" and p.subtipo == "Volador"):
            print(f"{entrenador.nombre} tiene a {p.nombre} ({p.tipo}/{p.subtipo})")
            break # Si ya cumple, pasamos al siguiente entrenador


print("\n--- g. Promedio de nivel de Pokémons de un entrenador (Ej: Brock) ---")
pos_brock = lista_entrenadores.search("Brock", 'nombre')
if pos_brock is not None:
    entrenador = lista_entrenadores[pos_brock]
    suma_niveles = 0
    for p in entrenador.pokemons:
        suma_niveles += p.nivel
    promedio = suma_niveles / entrenador.pokemons.size() if entrenador.pokemons.size() > 0 else 0
    print(f"El promedio de nivel del equipo de {entrenador.nombre} es {promedio:.2f}")


print("\n--- h. Cuántos entrenadores tienen a un Pokémon (Ej: Wingull) ---")
buscado = "Wingull"
contador = 0
for entrenador in lista_entrenadores:
    if entrenador.pokemons.search(buscado, 'nombre') is not None:
        contador += 1
print(f"{contador} entrenador(es) tienen a {buscado}.")


print("\n--- i. Entrenadores con Pokémons repetidos ---")
for entrenador in lista_entrenadores:
    nombres_pokemons = []
    for p in entrenador.pokemons:
        nombres_pokemons.append(p.nombre)
    
    # Si al convertir la lista a Set (que borra duplicados) el tamaño baja, hay repetidos
    if len(nombres_pokemons) != len(set(nombres_pokemons)):
        print(f"{entrenador.nombre} tiene Pokémons repetidos en su equipo.")


print("\n--- j. Entrenadores con Tyrantrum, Terrakion o Wingull ---")
buscados = ["Tyrantrum", "Terrakion", "Wingull"]
for entrenador in lista_entrenadores:
    for pokemon_buscado in buscados:
        if entrenador.pokemons.search(pokemon_buscado, 'nombre') is not None:
            print(f"{entrenador.nombre} tiene a {pokemon_buscado}.")


print("\n--- k. ¿El entrenador 'Ash Ketchum' tiene a 'Pikachu'? ---")
entrenador_x = "Ash Ketchum"
pokemon_y = "Pikachu"

pos_e = lista_entrenadores.search(entrenador_x, 'nombre')
if pos_e is not None:
    entrenador = lista_entrenadores[pos_e]
    pos_p = entrenador.pokemons.search(pokemon_y, 'nombre')
    if pos_p is not None:
        print(f"Sí, lo tiene. Datos:\n {entrenador}\n {entrenador.pokemons[pos_p]}")
    else:
        print(f"No, {entrenador.nombre} no tiene a {pokemon_y}.")
else:
    print(f"El entrenador {entrenador_x} no está en la lista.")