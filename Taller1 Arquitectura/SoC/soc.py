"""
Principio: SoC (Separation of Concerns - Separación de Intereses)
Objetivo: Dividir un programa en distintas secciones, donde cada sección
aborda una preocupación o interés separado. Un ejemplo clásico es
el patrón Modelo-Vista-Controlador (MVC).
"""
import time

# --- CAPA DE MODELO ---
# Preocupación: Representar los datos y la lógica de negocio fundamental.
# No sabe cómo se mostrarán los datos ni cómo interactúa el usuario.
class Pelicula:
    def __init__(self, titulo, anio):
        self.titulo = titulo
        self.anio = anio

class Cartelera:
    def __init__(self):
        self._peliculas = []
    
    def agregar_pelicula(self, pelicula):
        self._peliculas.append(pelicula)
        
    def obtener_peliculas(self):
        return self._peliculas

# --- CAPA DE VISTA ---
# Preocupación: Mostrar los datos al usuario.
# No sabe de dónde vienen los datos, solo los recibe y los presenta.
class VistaConsola:
    def mostrar_cartelera(self, lista_peliculas):
        print("\n--- CINEPLANET - CARTELERA ACTUAL ---")
        if not lista_peliculas:
            print("No hay películas disponibles.")
        else:
            for p in lista_peliculas:
                print(f"- {p.titulo} ({p.anio})")
        print("-------------------------------------")
        
    def mostrar_mensaje(self, mensaje):
        print(f"\n[SISTEMA] {mensaje}")

# --- CAPA DE CONTROLADOR ---
# Preocupación: Orquestar la interacción entre el Modelo y la Vista.
# Recibe las entradas del usuario y decide qué hacer.
class ControladorCine:
    def __init__(self, modelo_cartelera, vista):
        self._modelo = modelo_cartelera
        self._vista = vista

    def iniciar_aplicacion(self):
        self._vista.mostrar_mensaje("Cargando películas...")
        # Simula la carga de datos
        self._modelo.agregar_pelicula(Pelicula("Matrix", 1999))
        self._modelo.agregar_pelicula(Pelicula("Inception", 2010))
        time.sleep(1) # Simula una demora
        self._vista.mostrar_mensaje("¡Carga completa!")
        
    def solicitar_mostrar_cartelera(self):
        peliculas = self._modelo.obtener_peliculas()
        self._vista.mostrar_cartelera(peliculas)

# --- PUNTO DE ENTRADA (main) ---
# Se encarga de ensamblar las piezas y poner en marcha la aplicación.
def main():
    print("--- DEMOSTRACIÓN DE SEPARACIÓN DE INTERESES (SoC) ---\n")
    
    # 1. Crear las instancias de cada capa
    modelo = Cartelera()
    vista = VistaConsola()
    controlador = ControladorCine(modelo, vista)
    
    # 2. Iniciar el flujo de la aplicación
    controlador.iniciar_aplicacion()
    
    # 3. Simular una acción del usuario
    controlador.solicitar_mostrar_cartelera()

if __name__ == "__main__":
    main()
