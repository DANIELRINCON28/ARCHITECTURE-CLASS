"""
Principio: DRY (Don't Repeat Yourself - No te repitas)
Objetivo: Evitar la duplicación de código. La lógica debe definirse
una sola vez en un único lugar.
"""

# --- ANTES DE APLICAR DRY (CÓDIGO REPETIDO) ---
class ProcesadorReservasMalo:
    def procesar_reserva_web(self, usuario, pelicula):
        # Lógica repetida Bloque 1
        if not usuario or not pelicula:
            print("Error: Usuario o película no pueden estar vacíos.")
            return False
        
        # Lógica específica para web
        print(f"Procesando reserva WEB para '{usuario}' de la película '{pelicula}'...")
        
        # Lógica repetida Bloque 2
        print("Enviando email de confirmación...")
        print("Reserva completada.")
        return True

    def procesar_reserva_taquilla(self, usuario, pelicula):
        # Lógica repetida Bloque 1
        if not usuario or not pelicula:
            print("Error: Usuario o película no pueden estar vacíos.")
            return False

        # Lógica específica para taquilla
        print(f"Procesando reserva en TAQUILLA para '{usuario}' de la película '{pelicula}'...")

        # Lógica repetida Bloque 2
        print("Enviando email de confirmación...")
        print("Reserva completada.")
        return True


# --- DESPUÉS DE APLICAR DRY (REFACTORIZADO) ---
class ProcesadorReservasBueno:
    
    # 1. Se extrae la lógica repetida a métodos privados
    def _validar_datos(self, usuario, pelicula):
        if not usuario or not pelicula:
            raise ValueError("Usuario o película no pueden estar vacíos.")
        return True

    def _confirmar_reserva(self):
        print("Enviando email de confirmación...")
        print("Reserva completada.")

    # 2. Los métodos públicos ahora orquestan la llamada a los métodos privados
    def procesar_reserva(self, usuario, pelicula, canal):
        try:
            self._validar_datos(usuario, pelicula)
            print(f"Procesando reserva por canal '{canal.upper()}' para '{usuario}'...")
            # Aquí iría la lógica específica del canal si la hubiera
            self._confirmar_reserva()
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False


# --- DEMOSTRACIÓN ---
print("--- DEMOSTRACIÓN DE DRY ---\n")
print("-> Usando la clase refactorizada (Buena):")
procesador_bueno = ProcesadorReservasBueno()
procesador_bueno.procesar_reserva("Marta", "Oppenheimer", "Web")
print("-" * 20)
procesador_bueno.procesar_reserva("Luis", "Barbie", "Taquilla")
print("-" * 20)
procesador_bueno.procesar_reserva(None, "Interestellar", "Web") # Caso de error
