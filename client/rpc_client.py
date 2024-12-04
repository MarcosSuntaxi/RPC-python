import xmlrpc.client

# Conexión al servidor
proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

# Llamada a la función remota
result = proxy.add(5, 3)
print(f"El resultado de la suma es: {result}")
