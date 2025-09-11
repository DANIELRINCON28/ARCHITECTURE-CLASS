"""
Principio: ACOPLAMIENTO (Buscando un bajo acoplamiento)
Objetivo: Reducir las dependencias entre las clases. Una clase no debe
conocer los detalles internos de otra. Se logra usando abstracciones (interfaces).
"""
from abc import ABC, abstractmethod

# 1. Abstracción (Interfaz)
# Define un contrato sin una implementación concreta.
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje, destinatario):
        pass

# 2. Implementaciones Concretas
# Cada clase implementa la interfaz pero tiene su propia lógica.
class NotificadorEmail(Notificador):
    def enviar(self, mensaje, email):
        print(f"Enviando EMAIL a {email}: '{mensaje}'")

class NotificadorSMS(Notificador):
    def enviar(self, mensaje, telefono):
        print(f"Enviando SMS al {telefono}: '{mensaje}'")

# 3. Clase que depende de la ABSTRACCIÓN, no de la implementación
# SistemaReservas no sabe si está usando Email o SMS, solo sabe que usa un Notificador.
# Esto es bajo acoplamiento.
class SistemaReservas:
    def __init__(self, notificador: Notificador):
        # Inyección de dependencias: recibe la herramienta (notificador) que usará.
        self.__notificador = notificador

    def crear_reserva(self, pelicula, usuario_contacto):
        print(f"Creando reserva para la película '{pelicula}'...")
        # Lógica de reserva...
        print("¡Reserva creada!")
        
        # Usa el notificador sin saber cuál es.
        self.__notificador.enviar(f"Tu reserva para '{pelicula}' ha sido confirmada.", usuario_contacto)

# --- DEMOSTRACIÓN ---
print("--- DEMOSTRACIÓN DE BAJO ACOPLAMIENTO ---\n")

# Podemos cambiar el comportamiento del sistema sin modificar la clase SistemaReservas.
notificador_email = NotificadorEmail()
notificador_sms = NotificadorSMS()

print("-> Usando el sistema de reservas con notificaciones por Email:")
sistema_con_email = SistemaReservas(notificador_email)
sistema_con_email.crear_reserva("Inception", "pedro@mail.com")

print("\n-> Usando el MISMO sistema, pero con notificaciones por SMS:")
sistema_con_sms = SistemaReservas(notificador_sms)
sistema_con_sms.crear_reserva("Interstellar", "+123456789")
