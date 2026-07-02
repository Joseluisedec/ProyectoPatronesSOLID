from pedido_factory import PedidoFactory
from conexion_bd import ConexionBD
from usuario import Usuario
from evento import Evento

# Singleton
bd1 = ConexionBD()
bd2 = ConexionBD()

print("¿Misma instancia?:", bd1 is bd2)

# Observer
evento = Evento()

u1 = Usuario("José")
u2 = Usuario("María")

evento.suscribir(u1)
evento.suscribir(u2)

# Factory
pedido = PedidoFactory.crear_pedido("urgente")
pedido.procesar()

# Notificación
evento.notificar("Se creó un nuevo pedido")