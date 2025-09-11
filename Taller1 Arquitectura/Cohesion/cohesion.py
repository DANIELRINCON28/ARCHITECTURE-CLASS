"""
Principio: COHESIÓN (Buscando una alta cohesión)
Objetivo: Asegurar que una clase tenga una única responsabilidad bien enfocada.
Todos sus métodos y atributos deben estar estrechamente relacionados.
"""

# --- EJEMPLO DE BAJA COHESIÓN (QUÉ EVITAR) ---
class GestorCineAntiguo:
    def registrar_usuario(self, nombre):
        print(f"Registrando usuario {nombre} en la base de datos...")
        # ...lógica de base de datos...

    def agregar_pelicula_a_cartelera(self, titulo):
        print(f"Agregando '{titulo}' a la cartelera...")

    def imprimir_ticket_reserva(self, usuario, pelicula):
        # Lógica de formato de texto e impresión
        print("--- TICKET CINEPLEX ---")
        print(f"Usuario: {usuario}")
        print(f"Película: {pelicula}")
        print("-----------------------")
# Esta clase hace demasiadas cosas no relacionadas: maneja usuarios,
# películas e impresión. Es poco cohesiva.

# --- EJEMPLO DE ALTA COHESIÓN (CORRECTO) ---

class GestorUsuarios:
    """Responsabilidad: Solo manejar usuarios."""
    def __init__(self):
        self._usuarios = []
    
    def registrar(self, nombre):
        print(f"Registrando a {nombre} en el sistema de usuarios.")
        self._usuarios.append(nombre)

class Cartelera:
    """Responsabilidad: Solo manejar la lista de películas."""
    def __init__(self):
        self._peliculas = []

    def agregar_pelicula(self, titulo):
        print(f"Agregando '{titulo}' a la cartelera.")
        self._peliculas.append(titulo)

class ImpresoraTickets:
    """Responsabilidad: Solo formatear e imprimir tickets."""
    def imprimir(self, usuario, pelicula):
        print("\n--- TICKET IMPRESO ---")
        print(f"Usuario: {usuario}")
        print(f"Película: {pelicula}")
        print("----------------------")

# --- DEMOSTRACIÓN ---
print("--- DEMOSTRACIÓN DE ALTA COHESIÓN ---\n")

# Cada objeto tiene una responsabilidad clara.
gestor_usuarios = GestorUsuarios()
cartelera = Cartelera()
impresora = ImpresoraTickets()

# Usamos los objetos especializados para cada tarea.
gestor_usuarios.registrar("Elena")
cartelera.agregar_pelicula("Dune")
impresora.imprimir("Elena", "Dune")
