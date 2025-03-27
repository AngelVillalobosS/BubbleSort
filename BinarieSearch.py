import random  # Para generar números aleatorios
import time  # Para medir el tiempo de ejecución
import multiprocessing  # Para ejecutar procesos en paralelo

def binary_search(arr, target):
    """Realiza una búsqueda binaria en una lista ordenada y muestra el proceso."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Buscando en índice {left + 1} - {right + 1}, medio: {mid + 1}, valor: {arr[mid]}")
        if arr[mid] == target:
            print(f"Elemento encontrado en índice {mid + 1}")
            return mid + 1  # Retorna la posición donde se encuentra el elemento, ajustada a empezar desde 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Elemento no encontrado")
    return -1  # Retorna -1 si no se encuentra

def parallel_binary_search(args):
    """Ejecuta búsqueda binaria en un fragmento de la lista."""
    arr, target, offset = args
    index = binary_search(arr, target)
    return index + offset if index != -1 else -1

def search_in_parallel(arr, target):
    """Divide la lista y realiza la búsqueda binaria en paralelo."""
    num_processes = multiprocessing.cpu_count()
    chunk_size = len(arr) // num_processes
    
    sublists = [(arr[i * chunk_size:(i + 1) * chunk_size], target, i * chunk_size) for i in range(num_processes)]
    
    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(parallel_binary_search, sublists)
    
    for res in results:
        if res != -1:
            return res  # Retorna el primer índice encontrado
    return -1  # Si no se encuentra el elemento

def test_search():
    sizes = [10, 100]  # Tamaños de prueba
    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))  # Genera y ordena datos únicos
        target = random.choice(arr)  # Elige un elemento al azar para buscar
        
        print(f"\n---- Generando el chunk de datos -----")
        print(f"Datos generados ({size} elementos): {arr}")
        print(f"\nDato a buscar: {target}")
        
        # Búsqueda binaria secuencial
        start = time.time()
        index = binary_search(arr, target)
        end = time.time()
        print(f"\nÍndice encontrado (secuencial): {index}")
        print(f"Tiempo de búsqueda secuencial: {end - start:.4f} segundos")
        
        # Búsqueda binaria paralela
        start = time.time()
        index_parallel = search_in_parallel(arr, target)
        end = time.time()
        print(f"\nÍndice encontrado (paralelo): {index_parallel}")
        print(f"Tiempo de búsqueda paralela: {end - start:.4f} segundos")

if __name__ == "__main__":
    test_search()
