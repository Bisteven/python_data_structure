tareas = ["estudiar","ejercicio","programar","descansar"]
primera   = tareas[0]    # "estudiar"
ultima    = tareas[-1]   # "descansar"
penultima = tareas[-2]   # "programar"

print(len(tareas))           # 4
print("programar" in tareas) # True
print(tareas.count("ejercicio")) # 1
print(tareas.index("programar")) # 2


numeros = [10, 20, 30, 40, 50, 60, 70]

primeros_tres = numeros[0:3]   # [10, 20, 30]
del_1_al_3    = numeros[1:4]   # [20, 30, 40]
hasta_tercero = numeros[:3]    # [10, 20, 30]
desde_tercero = numeros[2:]    # [30, 40, 50, 60, 70]
pares         = numeros[::2]   # [10, 30, 50, 70]
ultimos_tres  = numeros[-3:]   # [50, 60, 70]
invertida     = numeros[::-1]  # [70, 60, 50, 40, 30, 20, 10]

tareas = ["estudiar", "ejercicio"]
tareas.append("programar")         # añade al final
tareas.insert(0, "llamar médico")  # inserta al inicio
tareas.extend(["lavar ropa", "cocinar"])

# append vs extend — diferencia importante
a = [1, 2, 3]
a.append([4, 5])   # → [1, 2, 3, [4, 5]]  ← lista anidada
a = [1, 2, 3]
a.extend([4, 5])   # → [1, 2, 3, 4, 5]    ← elementos sueltos

colores = ["rojo", "verde", "azul", "verde"]
colores.remove("verde")  # → ["rojo", "azul", "verde"]

nums = [10, 20, 30, 40]
ultimo  = nums.pop()   # retorna 40 → nums = [10, 20, 30]
segundo = nums.pop(1)  # retorna 20 → nums = [10, 30]

mi_lista = [1, 2, 3, 4]
mi_lista.clear()         # → []

nums = [3, 1, 4, 2]
nums.sort()              # [1, 2, 3, 4] — modifica la original
nums.sort(reverse=True)  # [4, 3, 2, 1]

letras = ["c", "a", "b"]
letras.reverse()         # ["b", "a", "c"]

original = [3, 1, 4, 2]
nueva = sorted(original) # nueva = [1, 2, 3, 4]
print(original)          # [3, 1, 4, 2] — sin cambios

frutas = ["manzana", "plátano", "naranja"]
for f in frutas:
    print(f"Me gusta {f}")

for i, f in enumerate(frutas, 1):
    print(f"{i}. {f}")

nombres = ["Ana","Carlos","Elena"]
edades  = [28, 35, 23]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre}: {edad} años")

cuadrados = [n**2 for n in range(5)]  # [0,1,4,9,16]
pares = [n for n in range(10) if n%2==0]

# Problema de referencia compartida
a = [1, 2, 3]
b = a        # misma referencia
b[0] = 100
print(a)     # [100, 2, 3] — ¡a también cambió!

# Solución: copy()
a = [1, 2, 3]
b = a.copy()
b[0] = 100
print(a)     # [1, 2, 3] — intacta

# Listas anidadas → deepcopy
import copy
anidada = [[1, 2], [3, 4]]
deep = copy.deepcopy(anidada)
deep[0][0] = 99
print(anidada) # [[1, 2], [3, 4]] — intacta

#RETO
inventario = [["Manzana", 10, 1.50],
              ["Pera", 5, 3.50],
              ["Naranja", 8, 2.0]]

def actualizar_precio(producto, nuevo_precio):
    producto[2] = nuevo_precio

def registrar_venta(producto, cantidad):
    if producto[1] >= cantidad:
        producto[1] -= cantidad
    else:
        print(f"Stock insuficiente para {producto[0]}")

def añadir_producto(nombre, cantidad, precio):
    for producto in inventario:
        if producto[0] == nombre:
            producto[1] += cantidad
            return
    inventario.append([nombre, cantidad, precio])

def mostrar_inventario():
    print("\n--- Inventario ---")
    for producto in inventario:
        print(f"{producto[0]}: {producto[1]} unidades a ${producto[2]:.2f}")

# Llamadas
actualizar_precio(inventario[1], 1.20)
registrar_venta(inventario[0], 3)
añadir_producto("Huevos", 12, 3.50)
mostrar_inventario()