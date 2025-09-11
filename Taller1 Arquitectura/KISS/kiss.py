"""
Principio: KISS (Keep It Simple, Stupid - Mantenlo simple, tonto)
Objetivo: Preferir la simplicidad sobre la complejidad innecesaria.
Una solución más simple y clara es mejor que una rebuscada.
"""

peliculas = ["Matrix", "Inception", "Interstellar", "Dune"]

# --- FORMA COMPLICADA (VIOLA KISS) ---
def buscar_pelicula_complicado(titulo_buscado):
    """
    Busca una película recorriendo una lista con un índice manual
    y usando una bandera. Es innecesariamente complejo.
    """
    encontrada = False
    indice = 0
    resultado = ""
    while indice < len(peliculas):
        if peliculas[indice] == titulo_buscado:
            encontrada = True
            break # Romper el bucle es una complicación extra
        indice += 1

    if encontrada:
        resultado = f"'{titulo_buscado}' está en cartelera."
    else:
        resultado = f"'{titulo_buscado}' no está en cartelera."
    return resultado

# --- FORMA SIMPLE (APLICA KISS) ---
def buscar_pelicula_simple(titulo_buscado):
    """
    Usa el operador 'in' de Python, que es más legible, directo
    y menos propenso a errores.
    """
    if titulo_buscado in peliculas:
        return f"'{titulo_buscado}' está en cartelera."
    else:
        return f"'{titulo_buscado}' no está en cartelera."

# --- FORMA SIMPLE Y EFICIENTE USANDO UN SET ---
# Para listas muy grandes, la búsqueda 'in' en un set es mucho más rápida.
peliculas_set = {"Matrix", "Inception", "Interstellar", "Dune"}

def buscar_pelicula_eficiente(titulo_buscado):
    if titulo_buscado in peliculas_set:
        return f"'{titulo_buscado}' está en cartelera (búsqueda eficiente)."
    else:
        return f"'{titulo_buscado}' no está en cartelera (búsqueda eficiente)."


# --- DEMOSTRACIÓN ---
print("--- DEMOSTRACIÓN DE KISS ---\n")

print("-> Búsqueda complicada:")
print(buscar_pelicula_complicado("Inception"))
print(buscar_pelicula_complicado("Titanic"))

print("\n-> Búsqueda simple y legible:")
print(buscar_pelicula_simple("Inception"))
print(buscar_pelicula_simple("Titanic"))

print("\n-> Búsqueda simple y eficiente:")
print(buscar_pelicula_eficiente("Dune"))
print(buscar_pelicula_eficiente("Avatar"))
