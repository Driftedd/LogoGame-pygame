Augusto = 10
Carlos = 20
Maria = 30

# Filtrar las variables personalizadas
variables_personalizadas = {k: v for k, v in vars().items() if not k.startswith('__')}

for nombre_variable, valor in variables_personalizadas.items():
    print(f"La variable se llama {nombre_variable} y su valor es {valor}")