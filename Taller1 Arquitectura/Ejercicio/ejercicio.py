class Cine:
    """
    Clase que simula la gestión de usuarios, películas y reservas de un cine.
    """
    def __init__(self):
        """
        Constructor para inicializar las listas de la instancia.
        """
        self.usuarios = []
        self.peliculas = ["Matrix", "Inception", "Interstellar"]
        self.reservas = []

    def registrar_usuario(self, nombre, email):
        """
        Registra un nuevo usuario en la lista.
        """
        # Añade un diccionario con los datos del usuario a la lista
        self.usuarios.append({"nombre": nombre, "email": email})
        print(f"Usuario {nombre} registrado.")

    def mostrar_cartelera(self):
        """
        Muestra todas las películas disponibles en la cartelera.
        """
        print("\n--- Cartelera ---")
        for p in self.peliculas:
            print(p)
        print("-----------------\n")

    def reservar(self, nombre_usuario, pelicula):
        """
        Realiza una reserva para un usuario y una película.
        """
        # Comprueba si existe algún usuario con ese nombre
        usuario_encontrado = any(u["nombre"] == nombre_usuario for u in self.usuarios)

        if not usuario_encontrado:
            print("Usuario no registrado")
            return

        # Comprueba si la película está en la lista de películas
        if pelicula in self.peliculas:
            self.reservas.append({"usuario": nombre_usuario, "pelicula": pelicula})
            print(f"Reserva exitosa para {nombre_usuario} - Película: {pelicula}")
        else:
            print("Película no disponible")

    def duplicar_validacion_email(self, email):
        """
        Valida si un email contiene el carácter '@'.
        """
        return "@" in email

    def duplicar_validacion_email2(self, email):
        """
        Segunda validación de email (idéntica a la primera).
        """
        return "@" in email

# --- Bloque de ejecución principal ---
# Esta es la forma estándar en Python para ejecutar código cuando
# el archivo es llamado directamente.
if __name__ == "__main__":
    c = Cine()
    c.registrar_usuario("Pedro", "pedro@mail.com")
    c.mostrar_cartelera()
    c.reservar("Pedro", "Matrix")