class ConexionBD:

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Creando conexión a la base de datos...")
            cls._instancia = super().__new__(cls)
        return cls._instancia