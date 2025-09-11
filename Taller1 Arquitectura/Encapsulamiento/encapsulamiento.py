"""
Principio: ENCAPSULAMIENTO
Objetivo: Ocultar el estado interno de un objeto y requerir que toda la
interacción se realice a través de los métodos de un objeto.
"""

class Usuario:
    def __init__(self, nombre, email):
        # Atributos privados (se denotan con __)
        # Su valor no puede ser accedido o modificado directamente desde fuera de la clase.
        self.__nombre = nombre
        self.__email = email
        self.__validar_email()

    # Método privado para lógica interna
    def __validar_email(self):
        """Un método privado que solo la clase puede usar internamente."""
        if "@" not in self.__email:
            raise ValueError("Email no válido: debe contener un '@'.")

    # Getters: Métodos públicos para obtener el valor de atributos privados
    def get_nombre(self):
        """Permite el acceso de solo lectura al nombre."""
        return self.__nombre

    def get_email(self):
        """Permite el acceso de solo lectura al email."""
        return self.__email
        
    # Setter: Método público para modificar un atributo privado con validación
    def set_email(self, nuevo_email):
        """Permite la modificación controlada del email."""
        print(f"Intentando cambiar el email de {self.__nombre} a {nuevo_email}...")
        self.__email = nuevo_email
        self.__validar_email() # Se asegura de que el nuevo estado sea válido
        print("Email actualizado correctamente.")


# --- DEMOSTRACIÓN ---
print("--- DEMOSTRACIÓN DE ENCAPSULAMIENTO ---\n")

# 1. Creación de un objeto válido
usuario = Usuario("Ana", "ana@correo.com")
print(f"Usuario creado: {usuario.get_nombre()}, Email: {usuario.get_email()}")

# 2. Intentando acceder directamente a un atributo privado (fallará)
try:
    print(usuario.__nombre)
except AttributeError as e:
    print(f"\nError esperado: No se puede acceder a 'usuario.__nombre'. ({e})")

# 3. Usando un 'setter' para modificar el estado de forma controlada
usuario.set_email("ana.lopez@web.co")
print(f"Email actualizado a través del setter: {usuario.get_email()}")

# 4. Intentando crear un objeto con estado inválido (fallará)
try:
    usuario_malo = Usuario("Carlos", "carlos-sin-arroba")
except ValueError as e:
    print(f"\nError esperado al crear usuario: {e}")
