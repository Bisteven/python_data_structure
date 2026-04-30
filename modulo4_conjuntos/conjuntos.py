colores = {"rojo","verde","azul","rojo"}
print(colores)  # {'verde','azul','rojo'} — sin "rojo" duplicado

numeros = set([1, 2, 3, 2, 1])
print(numeros)  # {1, 2, 3}

# Búsqueda eficiente
frutas = {"manzana","naranja","plátano"}
print("manzana" in frutas)  # True — O(1)

# Conjunto vacío
vacio = set()
print(type({}))   # <class 'dict'>   — NO es un set
print(type(set())) # <class 'set'>   — correct


tecnologias = {"Python","JavaScript","SQL"}
tecnologias.add("Java")
tecnologias.update(["Go","Rust"])

frutas = {"manzana","naranja","platano"}
frutas.remove("naranja")    # OK
frutas.discard("kiwi")      # silencioso — kiwi no existe
elem = frutas.pop()         # aleatorio
frutas.clear()              # set()

# issubset / issuperset
pares = {2,4,6,8}
nums  = {1,2,3,4,5,6,7,8,9}
print(pares.issubset(nums))   # True
print(nums.issuperset(pares)) # True

grupo_a = {"Ana","Carlos","Elena","David"}
grupo_b = {"Carlos","Elena","Fernando"}

comunes     = grupo_a.intersection(grupo_b)  # {'Carlos','Elena'}
todos       = grupo_a.union(grupo_b)
solo_en_a   = grupo_a.difference(grupo_b)    # {'Ana','David'}
exclusivos  = grupo_a.symmetric_difference(grupo_b)

vegetales = {"zanahoria","pepino"}
frutas    = {"manzana","platano"}
print(vegetales.isdisjoint(frutas))  # True — sin elementos comunes

# Encadenamiento
resultado = grupo_a.intersection(grupo_b).difference({"Elena"})
# → {'Carlos'}

u1 = {"acción","comedia","ciencia ficción","aventura"}
u2 = {"drama","comedia","romance","documental"}
u3 = {"acción","aventura","fantasía","ciencia ficción"}

comunes_1_3  = u1 & u3   # {'acción','ciencia ficción','aventura'}
todos_1_2    = u1 | u2
solo_u1      = u1 - u2   # excluye lo de u2
excl_2_3     = u2 ^ u3   # en uno pero no en ambos

# Operadores de comparación
print(u3 <= u1)  # False — u3 NO es subconjunto de u1
print({2,4} <= {1,2,3,4,5})  # True

#RETO

# ── 1. Sets de tiendas ───────────────────────────────────────────────
tienda_centro = {"laptop", "mouse", "teclado", "monitor", "auriculares"}
tienda_norte  = {"mouse", "teclado", "webcam", "micrófono", "auriculares"}
tienda_sur    = {"laptop", "impresora", "webcam", "tablet"}

# ── 2. union() e intersection() ─────────────────────────────────────
catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)

# ── 3. difference() e isdisjoint() ──────────────────────────────────
exclusivos_centro = tienda_centro.difference(tienda_norte, tienda_sur)
exclusivos_norte  = tienda_norte.difference(tienda_centro, tienda_sur)
exclusivos_sur    = tienda_sur.difference(tienda_centro, tienda_norte)

print(f"Solo en Centro: {exclusivos_centro}")
print(f"Solo en Norte:  {exclusivos_norte}")
print(f"Solo en Sur:    {exclusivos_sur}")
print(f"¿Centro y Norte sin comunes? {tienda_centro.isdisjoint(tienda_norte)}")
print(f"¿Norte y Sur sin comunes?   {tienda_norte.isdisjoint(tienda_sur)}")
print(f"¿Centro y Sur sin comunes?  {tienda_centro.isdisjoint(tienda_sur)}")

# ── 4. Sets de géneros ───────────────────────────────────────────────
usuario1 = {"acción", "drama", "thriller", "ciencia ficción"}
usuario2 = {"drama", "comedia", "thriller", "romance"}
usuario3 = {"acción", "comedia", "animación"}

# ── 5. Operadores & | - ^ ────────────────────────────────────────────
generos_comunes_12   = usuario1 & usuario2
universo_generos     = usuario1 | usuario2 | usuario3
exclusivos_u1        = usuario1 - usuario2
diferencia_simetrica = usuario1 ^ usuario2

# ── 6. Subconjunto <= y resumen final ───────────────────────────────
print(f"¿U3 subconjunto del universo? {usuario3 <= universo_generos}")
print(f"¿universo superconjunto de U1? {universo_generos >= usuario1}")

print("\n" + "═" * 45)
print("  SISTEMA DE RECOMENDACIÓN DE PELÍCULAS")
print("═" * 45)
print(f"  Universo de géneros ({len(universo_generos)}): {universo_generos}")
print(f"\n  U1 ∩ U2: {usuario1 & usuario2}")
print(f"  U1 ∩ U3: {usuario1 & usuario3}")
print(f"  U2 ∩ U3: {usuario2 & usuario3}")
print(f"\n  Solo U1: {usuario1 - usuario2 - usuario3}")
print(f"  Solo U2: {usuario2 - usuario1 - usuario3}")
print(f"  Solo U3: {usuario3 - usuario1 - usuario2}")
print(f"\n  ¿U3 ⊆ universo? {usuario3 <= universo_generos}")

print("\n── TIENDAS ─────────────────────────────────────")
print(f"  Catálogo global ({len(catalogo_completo)}): {catalogo_completo}")
print(f"  Comunes 3 tiendas: {productos_comunes}")
print(f"  Solo Centro: {exclusivos_centro}")
print(f"  Solo Norte:  {exclusivos_norte}")
print(f"  Solo Sur:    {exclusivos_sur}")