proyecto Final: Implementación de Patrones de Diseño y Principios SOLID
Descripción

Este proyecto consiste en el desarrollo de un sistema de gestión de pedidos para una tienda en línea utilizando Python.

El objetivo es demostrar la implementación de los patrones de diseño Factory, Singleton y Observer, así como la aplicación de los principios SOLID para desarrollar un código organizado, reutilizable y fácil de mantener.

Patrones implementadosPr
Factory
Singleton
Observer
Principios SOLID
Responsabilidad Única (SRP)
Abierto/Cerrado (OCP)
Sustitución de Liskov (LSP)
Segregación de Interfaces (ISP)
Inversión de Dependencias (DIP)
Estructura del proyecto
ProyectoPatronesSOLID/
│
├── src/
│   ├── pedido.py
│   ├── pedido_factory.py
│   ├── conexion_bd.py
│   ├── usuario.py
│   ├── evento.py
│   └── main.py
│
├── Documentacion/
├── README.md
├── requirements.txt
└── .gitignore
Cómo ejecutar
Abrir una terminal.
Ubicarse en la carpeta del proyecto.
Ejecutar:
python src/main.py
Resultado esperado
Creando conexión a la base de datos...
¿Misma instancia?: True
Procesando pedido URGENTE
José recibió: Se creó un nuevo pedido
María recibió: Se creó un nuevo pedido
