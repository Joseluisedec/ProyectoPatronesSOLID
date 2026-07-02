from abc import ABC, abstractmethod

# Clase base (abstracción)
class Pedido(ABC):

    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def procesar(self):
        pass


# Pedido Normal
class PedidoNormal(Pedido):

    def __init__(self):
        super().__init__("Normal")

    def procesar(self):
        print("Procesando pedido NORMAL")


# Pedido Urgente
class PedidoUrgente(Pedido):

    def __init__(self):
        super().__init__("Urgente")

    def procesar(self):
        print("Procesando pedido URGENTE")