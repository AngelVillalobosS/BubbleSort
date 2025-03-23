import random  # Importa la librería para generar números aleatorios
import time  # Importa la librería para medir el tiempo de ejecución
import multiprocessing  # Importa la librería para ejecutar procesos en paralelo

# Algoritmo de ordenación Burbuja (Bubble Sort) secuencial
def bubble_sort(arr):
    n = len(arr)  # Obtiene el tamaño de la lista
    for i in range(n):  # Itera sobre la lista n veces
        swapped = False  # Bandera para detectar si hubo intercambios
        for j in range(0, n - i - 1):  # Itera sobre la lista hasta la posición correcta
            if arr[j] > arr[j + 1]:  # Compara elementos adyacentes
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambia si están en el orden incorrecto
                swapped = True  # Marca que hubo un intercambio
        if not swapped:
            break  # Si no hubo intercambios en una pasada, la lista ya está ordenada
    return arr  # Devuelve la lista ordenada

# Algoritmo de ordenación Burbuja utilizando paralelismo
def parallel_bubble_sort(arr):
    n = len(arr)  # Obtiene el tamaño de la lista
    num_processes = multiprocessing.cpu_count()  # Obtiene el número de CPUs disponibles
    chunk_size = n // num_processes  # Divide la lista en fragmentos según el número de CPUs
    
    with multiprocessing.Pool(num_processes) as pool:  # Crea un pool de procesos
        # Divide la lista en sublistas de tamaño chunk_size
        sublists = [arr[i * chunk_size:(i + 1) * chunk_size] for i in range(num_processes)]
        sorted_sublists = pool.map(bubble_sort, sublists)  # Ordena cada sublista en paralelo
        
        # Fusiona las sublistas ordenadas
        sorted_arr = merge(sorted_sublists)
    
    return sorted_arr  # Devuelve la lista ordenada

# Función para fusionar sublistas ordenadas
def merge(sublists):
    result = []  # Lista donde se almacenará el resultado final
    for sublist in sublists:
        result.extend(sublist)  # Une todas las sublistas en una sola lista
    return bubble_sort(result)  # Se aplica Bubble Sort nuevamente para asegurar el orden

# Función para probar los algoritmos de ordenación
def test_sorting():
    sizes = [10000, 100000]  # Lista de tamaños a probar (usamos tamaños pequeños para mostrar los datos)
    for size in sizes:
        arr = [random.randint(0, 1000000) for _ in range(size)]  # Genera una lista de números aleatorios
        arr_copy = arr[:]  # Crea una copia de la lista para la versión paralela

        print("\n---- Generando el chunk de datos -----\n")
        print(f"Ordenando arreglo de tamaño {size}: \n")

        # Mostrar datos antes de ordenar
        print("Datos originales:", arr[:size])

        # Prueba Bubble Sort secuencial
        start = time.time()  # Captura el tiempo de inicio
        sorted_arr = bubble_sort(arr)  # Ordena la lista con el algoritmo secuencial
        end = time.time()  # Captura el tiempo de finalización
        #Muestra los datos ordenados y el tiempo que tardo en ejecutarlos
        print("\nOrdenado secuencial:", sorted_arr[:size])
        print(f"Tiempo de ordenación sin paralelismo: {end - start:.4f} segundos")  # Muestra el tiempo transcurrido
        
        # Prueba Bubble Sort paralelo
        start = time.time()  # Captura el tiempo de inicio
        sorted_parallel_arr = parallel_bubble_sort(arr_copy)  # Ordena la lista con el algoritmo paralelo
        end = time.time()  # Captura el tiempo de finalización
        print("\nOrdenado con paralelismo:", sorted_parallel_arr[:size])
        print(f"Tiempo de ordenación con paralelismo: {end - start:.4f} segundos")  # Muestra el tiempo transcurrido

# Punto de entrada del programa
if __name__ == "__main__":
    test_sorting()  # Ejecuta la función de prueba
