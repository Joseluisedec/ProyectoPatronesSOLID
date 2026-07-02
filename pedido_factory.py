from pedido import PedidoNormal, PedidoUrgente

class PedidoFactory:

    @staticmethod
    def crear_pedido(tipo):

        if tipo.lower() == "normal":
            return PedidoNormal()

        elif tipo.lower() == "urgente":
            return PedidoUrgente()

        else:
            raise ValueError("Tipo de pedido no válido")