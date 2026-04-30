# Bucle tradicional
cuadrados = []
for n in range(10):
    cuadrados.append(n**2)

# List comprehension — equivalente más conciso
cuadrados = [n**2 for n in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Con filtro
pares = [n for n in range(10) if n%2 == 0]
# [0, 2, 4, 6, 8]

# Transformación + extracción
celsius = [0, 10, 20, 30, 40]
fahr = [(9/5)*t + 32 for t in celsius]

usuarios = [{"nombre":"Ana","edad":28},{"nombre":"Carlos","edad":35}]
nombres = [u["nombre"] for u in usuarios]  # ['Ana','Carlos']

# Cuadrados
cuadrados = {n: n**2 for n in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}

# Filtrar stock disponible
stock = {"manzanas":10,"platanos":3,"naranjas":25,"peras":0}
disponibles = {f:c for f,c in stock.items() if c > 0}

# Invertir diccionario
original  = {"a":1, "b":2, "c":3}
invertido = {v:k for k,v in original.items()}  # {1:"a", 2:"b", 3:"c"}

# Desde lista de dicts
estudiantes = [{"id":1,"nombre":"Ana"},{"id":2,"nombre":"Carlos"}]
id_nombre = {e["id"]: e["nombre"] for e in estudiantes}

# Eliminar duplicados con transformación
numeros = [1,2,2,3,4,3,5,5,1]
unicos  = {n for n in numeros}  # {1,2,3,4,5}

# Iniciales únicas
palabras   = ["manzana","banana","mango","mora","naranja"]
iniciales  = {p[0] for p in palabras}  # {'m','b','n'}

# Vocales únicas en un texto
texto  = "python es un lenguaje versátil"
vocales = {l for l in texto.lower() if l in "aeiou"}

# Filtro: cuadrados de pares únicos
pares_cuad = {n**2 for n in range(10) if n%2==0}
# {0, 4, 16, 36, 64}

ventas = [
    {"producto":"laptop",  "unidades":20, "precio":800},
    {"producto":"teclado", "unidades":50, "precio":25},
    {"producto":"mouse",   "unidades":30, "precio":15},
    {"producto":"monitor", "unidades":10, "precio":200}
]
# List comp: valor total por producto
valor_por_producto = [i["unidades"]*i["precio"] for i in ventas]
# [16000, 1250, 450, 2000]

# List comp con filtro: alto valor
alto_valor = [i["producto"] for i in ventas
              if i["unidades"]*i["precio"] > 1000]
# ['laptop','teclado','monitor']

# Dict comp: nombre → valor total
resumen = {i["producto"]: i["unidades"]*i["precio"] for i in ventas}

# Gran total
gran_total = sum(valor_por_producto)  # 19700



#RETO
# ── 0. Datos base ────────────────────────────────────────────────────
ventas = [
    ("laptop",     12, 899.99, "electrónica"),
    ("mouse",      85,  24.99, "periféricos"),
    ("monitor",    20, 349.99, "electrónica"),
    ("teclado",    60,  49.99, "periféricos"),
    ("auriculares",35,  79.99, "audio"),
    ("webcam",     18,  59.99, "periféricos"),
]

# ── 1. List comp: valor total por producto ───────────────────────────
valor_total = [unidades * precio
               for nombre, unidades, precio, cat in ventas]

# ── 2. List comp con filtro: productos destacados ────────────────────
productos_destacados = [nombre
                        for nombre, unidades, precio, cat in ventas
                        if unidades * precio > 5000]

# ── 3. Dict comp: producto_info nombre → {valor, unidades} ──────────
producto_info = {
    nombre: {"valor": round(unidades * precio, 2), "unidades": unidades}
    for nombre, unidades, precio, cat in ventas
}

# ── 4. Dict comp con filtro: ranking_premium desc ────────────────────
ranking_premium = {
    nombre: round(unidades * precio, 2)
    for nombre, unidades, precio, cat in sorted(
        ventas, key=lambda x: x[1] * x[2], reverse=True
    )
    if precio > 50
}

# ── 5. Set comp: categorías y productos baratos ──────────────────────
categorias_unicas = {cat for nombre, unidades, precio, cat in ventas}
productos_baratos = {nombre for nombre, unidades, precio, cat in ventas
                     if precio <= 50}

# ── 6. Combinar + gran_total ─────────────────────────────────────────
resumen_formateado = {
    nombre: f"${unidades * precio:,.2f} ({cat})"
    for nombre, unidades, precio, cat in sorted(
        ventas, key=lambda x: x[1] * x[2], reverse=True
    )
    if precio > 50
}

gran_total = sum(unidades * precio
             for nombre, unidades, precio, cat in ventas)

print("═" * 42)
print("  REPORTE CONSOLIDADO DE VENTAS")
print("═" * 42)
print(f"  Categorías:        {categorias_unicas}")
print(f"  Productos baratos: {productos_baratos}")
print("\n  Ranking Premium (precio > $50):")
for prod, detalle in resumen_formateado.items():
    print(f"    {prod:<12}: {detalle}")
print("─" * 42)
print(f"  GRAN TOTAL (todos): ${gran_total:>11,.2f}")
print("═" * 42)