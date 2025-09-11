"""
Principios: SOLID
Aquí se demuestran dos de los principios más comunes:
1. SRP (Single Responsibility Principle): Una clase debe tener una sola razón para cambiar.
2. OCP (Open/Closed Principle): El software debe estar abierto a la extensión,
   pero cerrado a la modificación.
"""
from abc import ABC, abstractmethod

# --- 1. SRP: Single Responsibility Principle ---
# La clase Validador solo valida. La clase RepositorioUsuario solo guarda.
class ValidadorUsuario:
    """SRP: Su única responsabilidad es validar datos de usuario."""
    def validar(self, nombre, email):
        if not nombre:
            raise ValueError("El nombre es requerido.")
        if "@" not in email:
            raise ValueError("El email es inválido.")
        return True

class RepositorioUsuario:
    """SRP: Su única responsabilidad es interactuar con el almacenamiento de usuarios."""
    def guardar(self, nombre, email):
        print(f"Guardando usuario '{nombre}' con email '{email}' en la base de datos.")

# --- 2. OCP: Open/Closed Principle ---
# Podemos agregar nuevos tipos de descuento sin modificar el código de la calculadora.

# Abstracción
class ReglaDescuento(ABC):
    @abstractmethod
    def calcular_descuento(self, precio_base):
        pass

# Extensiones (abierto a la extensión)
class DescuentoEstudiante(ReglaDescuento):
    def calcular_descuento(self, precio_base):
        return precio_base * 0.20  # 20% de descuento

class DescuentoJubilado(ReglaDescuento):
    def calcular_descuento(self, precio_base):
        return precio_base * 0.30  # 30% de descuento

class DescuentoNavidad(ReglaDescuento):
    def calcular_descuento(self, precio_base):
        return 5.0 # $5 de descuento fijo

# Módulo cerrado a la modificación
class CalculadoraPrecios:
    """OCP: Esta clase no necesita ser modificada para añadir nuevos descuentos."""
    def calcular_precio_final(self, precio_base, reglas: list[ReglaDescuento]):
        descuento_total = 0
        for regla in reglas:
            descuento_total += regla.calcular_descuento(precio_base)
        
        precio_final = precio_base - descuento_total
        return max(0, precio_final) # Evita precios negativos

# --- DEMOSTRACIÓN ---
print("--- DEMOSTRACIÓN DE SOLID ---\n")

print("1. SRP en acción:")
validador = ValidadorUsuario()
repo = RepositorioUsuario()
nombre, email = "Juan", "juan@mail.com"
if validador.validar(nombre, email):
    repo.guardar(nombre, email)

print("\n2. OCP en acción:")
calculadora = CalculadoraPrecios()
precio_ticket = 20.0

# Aplicar un solo descuento
reglas_estudiante = [DescuentoEstudiante()]
precio_estudiante = calculadora.calcular_precio_final(precio_ticket, reglas_estudiante)
print(f"Precio para estudiante: ${precio_estudiante:.2f}")

# Aplicar múltiples descuentos (incluyendo el nuevo de Navidad) sin cambiar la calculadora
reglas_combo = [DescuentoJubilado(), DescuentoNavidad()]
precio_combo = calculadora.calcular_precio_final(precio_ticket, reglas_combo)
print(f"Precio para jubilado en Navidad: ${precio_combo:.2f}")
