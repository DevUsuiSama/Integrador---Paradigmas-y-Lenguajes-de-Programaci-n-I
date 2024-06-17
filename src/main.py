import os
import matplotlib.pyplot as plt
import numpy as np

# ((dT)/(dt))=k(T-T_{m})


# La ecuación diferencial ((dT)/(dt))=k(T-T_{m}) describe la tasa de cambio de la temperatura (T) con respecto al tiempo (t). Aquí está el significado de cada variable:

# ( ((dT)/(dt)) ): Es la derivada de la temperatura respecto al tiempo, que indica cómo cambia la temperatura en un instante dado.
# ( T ): Es la temperatura del objeto o sistema en estudio en un tiempo (t).
# ( T_{m} ): Es la temperatura del medio ambiente o una temperatura de referencia constante.
# ( k ): Es una constante de proporcionalidad que representa la tasa de enfriamiento o calentamiento y depende del sistema específico y sus propiedades.
# Esta ecuación es un modelo simplificado que se usa comúnmente para describir procesos de enfriamiento o calentamiento, como la Ley de Enfriamiento de Newton.

# Función para limpiar la pantalla
clear = lambda: os.system('cls')

class Nodo:
    def __init__(self, tiempo, temperatura):
        self.tiempo = tiempo
        self.temperatura = temperatura
        self.siguiente = None

class LinkedList:
    def __init__(self):
        self.cabecera = None
    def insertar(self, nodo: Nodo):
        if self.cabecera:
            ultimo_nodo = self.cabecera
            while ultimo_nodo.siguiente != None:
                ultimo_nodo = ultimo_nodo.siguiente
            ultimo_nodo.siguiente = nodo
        else:
            self.cabecera = nodo
    # Respuesta ante un eventual pregunta para este método.

    # La búsqueda binaria requiere acceso aleatorio a los elementos de la estructura de datos,
    # lo cual es posible en una lista o un arreglo, pero no en una lista enlazada debido a su naturaleza de acceso secuencial.
    # Por lo tanto, no se puede aplicar directamente la búsqueda binaria en una lista enlazada.

    # Sin embargo, si necesitas buscar un elemento en una lista enlazada,
    # puedes convertir la lista enlazada en una lista o arreglo y luego aplicar la búsqueda binaria.
    # Otra opción es realizar una búsqueda secuencial, que es más lenta (tiempo de ejecución (O(n))) pero funciona con listas enlazadas.

    # Si aún deseas implementar una búsqueda que se aproxime a la eficiencia de la búsqueda binaria en una lista enlazada,
    # podrías considerar transformar tu lista enlazada en otra estructura de datos que permita acceso aleatorio,
    # como un árbol de búsqueda equilibrado (por ejemplo, un AVL o un árbol rojo-negro),
    # donde las operaciones de búsqueda tienen un tiempo de ejecución (O(\log n)).
    def buscar_en_lista_metodo_binario(self, tiempo_buscado):
        # Convertir la lista enlazada en una lista para aplicar la búsqueda binaria
        lista_temporal = []
        nodo_actual: Nodo = self.cabecera
        while nodo_actual:
            lista_temporal.append([nodo_actual.tiempo, nodo_actual.temperatura])
            nodo_actual = nodo_actual.siguiente
        # Aplicar búsqueda binaria en la lista temporal
        inicio = 0
        fin = len(lista_temporal) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if lista_temporal[medio][0] == tiempo_buscado:
                return lista_temporal[medio][1]  # Retorna la temperatura correspondiente
            elif lista_temporal[medio][0] < tiempo_buscado:
                inicio = medio + 1
            else:
                fin = medio - 1
        return None  # Valor no encontrado
    def buscar(self, tiempo):
        if self.cabecera:
            actual = self.cabecera
            while actual:
                if actual.tiempo == tiempo:
                    return actual
                actual = actual.siguiente
            return None
    def recorrer_e_imprimir(self):
        aux = self.cabecera
        while aux:
            print(f"Tiempo: {aux.tiempo:.2f}, Temperatura: {aux.temperatura:.2f}")
            aux = aux.siguiente
    def esta_vacio(self, puntero):
        if puntero == None:
            return True
        else:
            return False

# Nos permite verificar si la opción está dentro del conjunto "lista_de_opcion"
def controlar_opcion(opcion: int, conjunto: list):
    for x in conjunto:
        if opcion == x:
            return True
    return False

# Parámetros de la ecuación diferencial
k = 0.1  # valor de ejemplo
Tm = 25  # valor de ejemplo

# Estructura para almacenar los datos
lista_de_datos = LinkedList()

# Función recursiva del método de Euler
def euler_method(max_time, t, T, dt):
    if t >= max_time:  # caso base
        return
    T_next = T + dt * k * (T - Tm)
    lista_de_datos.insertar(Nodo(t, T))
    plt.scatter(t, T)  # Graficar en tiempo real
    plt.xlabel("Tiempo (t)")
    plt.ylabel("Temperatura (T)")
    plt.pause(0.05)
    euler_method(max_time, t + dt, T_next, dt)

def calcular_error(punto_ingresado, tiempo_dado):
    temperatura_correspondiente = lista_de_datos.buscar_en_lista_metodo_binario(tiempo_dado)
    if temperatura_correspondiente is not None:
        error = abs(punto_ingresado - temperatura_correspondiente)
        return error
    else:
        print("-- Informe -- Tiempo no encontrado en la lista.")
        return None

def main():
    historial_coordenadas_y_error = []
    while True:
        print('Menu:')
        print('1> Mostrar los datos calculados')
        print('2> Ingresar una coordenada para el cálculo de error')
        print('3> Mostrar historial de coordenadas y resultado del cálculo de error')
        print('4> Buscar un dato en la lista')
        print('5> Limpiar la consola')
        print('6> Salir del programa')
        print()
        try:
            opcion = int(input('Ingrese una opcion: '))
        except ValueError:
            print('-- Error -- Ingrese un opción valida')
            input('Presione cualquier tecla para continuar...')
            clear()
            continue
        print()
        if controlar_opcion(opcion, [1, 2, 3, 4, 5, 6]):
            if opcion == 1:
                # Configuración de la gráfica en tiempo real
                plt.ion()
                plt.title("Evolución de la Temperatura con el Método de Euler")  # Título de la gráfica
                # Iniciar cálculo recursivo con el método de Euler
                max_time = 10  # valor de ejemplo
                euler_method(max_time, 0, 100, 0.1)  # tiempo inicial, T inicial, paso de tiempo
                plt.ioff()  # Desactivar modo interactivo
                plt.show()
                # Mostrar los datos en crudo
                lista_de_datos.recorrer_e_imprimir()
                input('\nPresione cualquier tecla para continuar...')
                clear()
            elif opcion == 2:
                # =================================================================
                # ESTRUCTURA DE CONTROL 1
                while True:
                    try:
                        t = float(input("Ingrese el tiempo: "))
                        T = float(input("Ingrese la temperatura: "))
                        break
                    except ValueError:
                        print('-- Error -- Ingrese un valor valido')
                        continue
                # =================================================================
                plt.ion()
                plt.title("Punto en la Gráfica [Tiempo, Valor Imagen]")  # Título de la gráfica
                plt.scatter(t, T)  # Gráfica en tiempo real
                plt.xlabel("Tiempo (t)")
                plt.ylabel("Temperatura (T)")
                plt.ioff()  # Desactivar modo interactivo
                plt.show()
                error = calcular_error(T, t)
                if error is not None:
                    print(f"El error entre el punto ingresado y el punto correspondiente es: {error:.2f}")
                    historial_coordenadas_y_error.append({
                        'tiempo': t,
                        'temperatura': T,
                        'error': error
                    })
                input('\nPresione cualquier tecla para continuar...')
                clear()
            elif opcion == 3:
                for x in historial_coordenadas_y_error:
                    print(f"Tiempo: {x['tiempo']:.2f}, Temperatura: {x['temperatura']:.2f}, Error: {x['error']:.2f}")
                input('\nPresione cualquier tecla para continuar...')
                clear()
            elif opcion == 4:
                # =================================================================
                # ESTRUCTURA DE CONTROL 1
                while True:
                    try:
                        t = float(input("Ingrese el tiempo: "))
                        break
                    except ValueError:
                        print('-- Error -- Ingrese un valor valido')
                        continue
                # =================================================================
                nodo_buscado = lista_de_datos.buscar(t)
                if nodo_buscado:
                    print(f"Tiempo: {nodo_buscado.tiempo:.2f}, Temperatura: {nodo_buscado.temperatura:.2f}")
                else:
                    print("-- Informe -- Tiempo no encontrado en la lista.")
                input('\nPresione cualquier tecla para continuar...')
                clear()
            elif opcion == 5:
                clear()
            elif opcion == 6:
                break
        else:
            print('-- Error -- La opcion ingresada no existe')
            input('Presione cualquier tecla para continuar...')
            clear()

if __name__ == '__main__':
    main()