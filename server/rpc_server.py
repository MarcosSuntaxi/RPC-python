from xmlrpc.server import SimpleXMLRPCServer

# Función que será expuesta al cliente
def add(x, y):
    return x + y

# Configuración del servidor
server = SimpleXMLRPCServer(("localhost", 9000))
print("Servidor RPC en ejecución en el puerto 9000...")

# Registrar la función que será accesible
server.register_function(add, "add")

# Iniciar el servidor
server.serve_forever()
