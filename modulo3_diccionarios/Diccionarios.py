contactos = {
    "Ana":    "612345678",
    "Carlos": "698765432"
}
print(contactos["Ana"])                    # 612345678
print(contactos.get("Elena", "No encontrado"))  # No encontrado

# Claves válidas (inmutables)
valido = {"nombre":"Juan", 42:"respuesta", (1,2):"coord"}

# INVÁLIDAS
# invalido = {[1,2]: "x"}  # TypeError: unhashable type: 'list'

colores = dict(rojo="#FF0000", verde="#00FF00", azul="#0000FF")

claves  = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Madrid"]
persona = {k: v for k, v in zip(claves, valores)}

# Diccionario anidado
usuario = {
    "nombre": "Miguel", "edad": 30,
    "direccion": {"calle":"Calle Mayor","ciudad":"Madrid"}
}
ciudad = usuario["direccion"]["ciudad"]  # "Madrid"

califs = {"Mates": 85, "Historia": 72}
califs.update({"Inglés": 88, "Mates": 87, "Arte": 95})

vendido = califs.pop("Inglés")      # retorna 88
par_final = califs.popitem()        # último par insertado

contador = {}
contador.setdefault("hola", 0)
contador["hola"] += 1               # → {"hola": 1}

materias = ["Mates","Historia","Arte"]
notas = dict.fromkeys(materias, 0)  # → {"Mates":0, ...}

d1 = {"nombre":"Carlos","edad":28}
d2 = {"email":"c@e.com"}
unido = d1 | d2                     # fusión Python 3.9+

califs = {"Mates":85, "Historia":72, "Ciencias":90}

for asig, nota in califs.items():
    print(f"{asig}: {nota}")

# Orden alfabético de claves
for asig in sorted(califs):
    print(f"{asig}: {califs[asig]}")

# Iteración segura: eliminar mientras recorres
d = {"a":1, "b":2, "c":3}
for k in list(d.keys()):
    if k == "b": del d[k]   # OK — iterando copia
print(d)  # {"a":1, "c":3}


precios = {"laptop":899, "tablet":349}

# Aplicar descuento del 10%
rebaja = {p: round(v*0.9, 2) for p,v in precios.items()}

# Filtrar productos disponibles
stock = {"manzanas":10, "peras":0, "naranjas":25}
disponibles = {f:c for f,c in stock.items() if c > 0}

# Invertir clave-valor
original  = {"a":1, "b":2, "c":3}
invertido = {v:k for k,v in original.items()}

# Porcentaje del total
gran_total = sum(precios.values())
pct = {p: round(v/gran_total*100,1) for p,v in precios.items()}

#RETO# 
 
# ── 1. Dict anidado ──────────────────────────────────────────────────
ventas_por_region = {
    "Norte": {"Q1": 15000, "Q2": 18000, "Q3": 22000, "Q4": 27000},
    "Sur":   {"Q1":  9000, "Q2": 11000, "Q3": 13000, "Q4": 16000},
    "Este":  {"Q1": 12000, "Q2": 14000, "Q3": 19000, "Q4": 21000},
    "Oeste": {"Q1": 20000, "Q2": 24000, "Q3": 28000, "Q4": 31000},
}

# ── 2. Total anual con items() y sum(values()) ───────────────────────
ventas_anuales = {}
for region, trimestres in ventas_por_region.items():
    ventas_anuales[region] = sum(trimestres.values())

# ── 3. Región con max() key=lambda ───────────────────────────────────
mejor_region = max(ventas_anuales, key=lambda r: ventas_anuales[r])

# ── 4. Acumular por trimestre con iteración anidada ──────────────────
totales_por_trimestre = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
for trimestres in ventas_por_region.values():
    for q, valor in trimestres.items():
        totales_por_trimestre[q] += valor

# ── 5. Gran total y porcentajes con dict comprehension ───────────────
gran_total = sum(ventas_anuales.values())
porcentajes = {
    region: round(total / gran_total * 100, 1)
    for region, total in ventas_anuales.items()
}

# ── 6. Reporte ordenado de mayor a menor ─────────────────────────────
print(f"\n{'═' * 38}")
print(f"  REPORTE ANUAL DE VENTAS POR REGIÓN")
print(f"{'═' * 38}")
print(f"{'Región':<10} {'Total anual':>12} {'%':>7}")
print(f"{'─' * 38}")
for region, total in sorted(ventas_anuales.items(),
                              key=lambda x: x[1],
                              reverse=True):
    print(f"{region:<10} ${total:>11,} {porcentajes[region]:>6.1f}%")
print(f"{'─' * 38}")
print(f"{'TOTAL':<10} ${gran_total:>11,}  100.0%")
print(f"\nMejor región: {mejor_region} (${ventas_anuales[mejor_region]:,})")
print(f"\nTrimestres globales:")
for q, val in totales_por_trimestre.items():
    print(f"  {q}: ${val:,}")