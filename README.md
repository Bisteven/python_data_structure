# Python — Estructuras de Datos

Proyecto de práctica para el aprendizaje de las principales estructuras de datos en Python: listas, tuplas, diccionarios, sets y comprehensions.

---

## Descripción del proyecto

Este repositorio contiene ejercicios progresivos organizados por módulo. Cada módulo cubre una estructura de datos diferente, con ejemplos comentados y un reto final que integra los conceptos del módulo.

El objetivo es consolidar el manejo de colecciones en Python a través de la práctica directa, pasando de ejemplos simples a casos de uso reales como sistemas de inventario, catálogos de películas y reportes de ventas.

---

##  Temas aprendidos

### Módulo 1 — Listas

- Acceso por índice positivo y negativo (`tareas[0]`, `tareas[-1]`)
- Slicing con paso: `numeros[::2]`, `numeros[::-1]`
- Métodos de modificación: `append()`, `insert()`, `extend()`, `remove()`, `pop()`, `clear()`
- Diferencia entre `append()` (anida) y `extend()` (desempaqueta)
- Ordenamiento: `sort()` modifica la original, `sorted()` devuelve una nueva
- Iteración con `enumerate()` y `zip()`
- List comprehensions con y sin filtro
- Referencia compartida vs copia: `copy()` y `copy.deepcopy()`

```python
# Slicing
numeros = [10, 20, 30, 40, 50, 60, 70]
pares       = numeros[::2]   # [10, 30, 50, 70]
invertida   = numeros[::-1]  # [70, 60, 50, 40, 30, 20, 10]

# append vs extend
a = [1, 2, 3]
a.append([4, 5])  # → [1, 2, 3, [4, 5]]  ← lista anidada
a = [1, 2, 3]
a.extend([4, 5])  # → [1, 2, 3, 4, 5]    ← elementos sueltos

# Copia segura
b = a.copy()      # independiente de a
```

---

### Módulo 2 — Tuplas

- Creación: literales, `tuple()`, desde rangos y strings
- Inmutabilidad y por qué importa (claves de diccionario, integridad de datos)
- Slicing y métodos `count()`, `index()`
- Unpacking simple y extendido con `*`
- Uso de `_` para ignorar valores al desempaquetar
- Funciones que retornan múltiples valores mediante tupla
- Iteración sobre tuplas de tuplas

```python
# Unpacking extendido
numeros = (1, 2, 3, 4, 5)
primero, *medio, ultimo = numeros   # medio = [2, 3, 4]

# Swap en una línea
a, b = 5, 10
a, b = b, a   # a=10, b=5

# Función con retorno múltiple
def estadisticas(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

minima, maxima, promedio = estadisticas([4, 7, 2, 9, 5])
```

---

### Módulo 3 — Diccionarios

- Creación: literales, `dict()`, `zip()`, `dict.fromkeys()`
- Acceso seguro con `.get(clave, valor_por_defecto)`
- Métodos: `update()`, `pop()`, `popitem()`, `setdefault()`, `clear()`
- Fusión de dicts con el operador `|` (Python 3.9+)
- Iteración con `.items()`, `.keys()`, `.values()`
- Eliminación segura mientras se itera (usando `list(d.keys())`)
- Dicts anidados y acceso con doble corchete
- Dict comprehensions con filtro y transformación

```python
# Acceso seguro
contactos.get("Elena", "No encontrado")   # evita KeyError

# Fusión
unido = d1 | d2   # Python 3.9+

# Iteración segura con eliminación
for k in list(d.keys()):
    if k == "b":
        del d[k]
```

---

### Módulo 4 — Sets

- Creación con `{}` y `set()` — diferencia con dict vacío
- Operaciones: `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()`
- Operaciones de conjunto: `union()`, `intersection()`, `difference()`, `symmetric_difference()`
- Operadores equivalentes: `|`, `&`, `-`, `^`
- Comparaciones: `<=` (subconjunto), `>=` (superconjunto), `isdisjoint()`
- Set comprehensions para deduplicar y filtrar

```python
# Operadores de conjunto
comunes    = u1 & u2    # intersection
todos      = u1 | u2    # union
solo_en_u1 = u1 - u2    # difference
exclusivos = u1 ^ u2    # symmetric_difference

# Subconjunto
{2, 4} <= {1, 2, 3, 4, 5}   # True
```

---

### Módulo 5 — Comprehensions

- **List comp**: `[expr for x in it]`
- **List comp con filtro**: `[expr for x in it if cond]`
- **Dict comp**: `{k: v for x in it}`
- **Dict comp con filtro + ordenamiento**: combinando `sorted()` y `if`
- **Set comp**: `{expr for x in it}` — elimina duplicados
- **Generator expression**: `sum(expr for x in it)` — sin crear lista en memoria
- Unpacking de tuplas directamente en el `for`
- Cuándo preferir bucle tradicional sobre comprehension

```python
# List comp con unpacking
valor_total = [unidades * precio
               for nombre, unidades, precio, cat in ventas]

# Dict comp con filtro y orden
ranking = {
    nombre: round(unidades * precio, 2)
    for nombre, unidades, precio, cat in sorted(
        ventas, key=lambda x: x[1] * x[2], reverse=True
    )
    if precio > 50
}

# Generator (ahorra memoria)
gran_total = sum(unidades * precio
                 for nombre, unidades, precio, cat in ventas)
```

---

##  Evidencia de retos resueltos

### Reto Módulo 1 — Sistema de inventario

Sistema de gestión con listas anidadas que permite actualizar precios, registrar ventas con control de stock y añadir productos nuevos o incrementar existentes.

**Funciones implementadas:**
- `actualizar_precio(producto, nuevo_precio)` — modifica el precio en la lista anidada
- `registrar_venta(producto, cantidad)` — descuenta stock con validación
- `añadir_producto(nombre, cantidad, precio)` — inserta o actualiza según existencia
- `mostrar_inventario()` — imprime formato tabulado

```
--- Inventario ---
Manzana:  7 unidades a $1.50
Pera:     5 unidades a $1.20
Naranja:  8 unidades a $2.00
Huevos:  12 unidades a $3.50
```

---

### Reto Módulo 2 — Catálogo de películas

Catálogo inmutable de 5 películas representado como tupla de tuplas. Se implementa búsqueda por director y cálculo de estadísticas de puntuación.

**Funciones implementadas:**
- `buscar_por_director(catalogo, director)` — retorna tupla de coincidencias
- `obtener_estadisticas(peliculas)` — retorna `(minima, maxima, promedio)`

```
=== PELÍCULA DESTACADA ===
El Padrino (1972) - Dir: Francis Ford Coppola -  9.2

Películas encontradas: 2
  Inception (2010) -  8.8
  Interstellar (2014) -  8.6

Puntuación mínima:  8.1
Puntuación máxima:  9.2
Promedio:           8.66
```

---

### Reto Módulo 3 — Reporte de ventas por región

Dict anidado `{ región: { Q1, Q2, Q3, Q4 } }` con cálculo de totales anuales, detección de mejor región con `max(key=lambda)`, acumulación por trimestre con iteración anidada y porcentajes con dict comprehension.

```
══════════════════════════════════════
  REPORTE ANUAL DE VENTAS POR REGIÓN
══════════════════════════════════════
Región       Total anual       %
──────────────────────────────────────
Oeste          $103,000   34.3%
Norte           $82,000   27.3%
Este            $66,000   22.0%
Sur             $49,000   16.3%
──────────────────────────────────────
TOTAL          $300,000  100.0%

Mejor región: Oeste ($103,000)
```

---

### Reto Módulo 4 — Sistema de tiendas y recomendación de películas

Dos problemas integrados usando sets: análisis de catálogos de tiendas (exclusivos, solapamientos) y sistema de recomendación de géneros cinematográficos entre usuarios.

```
Solo en Centro: {'monitor'}
Solo en Norte:  {'micrófono'}
Solo en Sur:    {'impresora', 'tablet'}
¿Centro y Norte sin comunes? False

══════════════════════════════════════════════
  SISTEMA DE RECOMENDACIÓN DE PELÍCULAS
══════════════════════════════════════════════
  Universo de géneros (7): {'acción', 'drama', ...}
  U1 ∩ U2: {'drama', 'thriller'}
  ¿U3 ⊆ universo? True
```

---

### Reto Módulo 5 — Reporte consolidado de ventas con comprehensions

Comprehensions de los tres tipos (list, dict, set) combinadas sobre una misma fuente de datos con unpacking de tuplas, filtros, ordenamiento y generator expression para el total.

```
══════════════════════════════════════════
  REPORTE CONSOLIDADO DE VENTAS
══════════════════════════════════════════
  Categorías:        {'electrónica', 'periféricos', 'audio'}
  Productos baratos: {'mouse', 'teclado'}

  Ranking Premium (precio > $50):
    laptop      : $10,799.88 (electrónica)
    monitor     :  $6,999.80 (electrónica)
    auriculares :  $2,799.65 (audio)
    webcam      :  $1,079.82 (periféricos)
──────────────────────────────────────────
  GRAN TOTAL (todos): $ 26,802.70
══════════════════════════════════════════
```

---

##  Capturas de ejecución

Inventario: <img width="520" height="95" alt="image" src="https://github.com/user-attachments/assets/f12f214c-a916-42d5-8b54-f99ce3c590b9" />
Catalogo:  <img width="476" height="207" alt="image" src="https://github.com/user-attachments/assets/f98b9df5-922f-4943-807f-2fc8b1346b9b" />
Ventas:  <img width="336" height="333" alt="image" src="https://github.com/user-attachments/assets/b881970a-791f-42ca-8adb-df542429c169" />
Tiendas: <img width="911" height="102" alt="image" src="https://github.com/user-attachments/assets/04462ad4-20f6-4ff4-b65e-f56292f4d951" />
Comprehensions: <img width="432" height="234" alt="image" src="https://github.com/user-attachments/assets/bbd1ef3e-bed2-42d5-849d-b98fd01495ee" />







