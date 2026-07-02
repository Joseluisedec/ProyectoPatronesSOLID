class Evento:

    def __init__(self):
        self.usuarios = []

    def suscribir(self, usuario):
        self.usuarios.append(usuario)

    def notificar(self, mensaje):
        for u in self.usuarios:
            u.actualizar(mensaje)