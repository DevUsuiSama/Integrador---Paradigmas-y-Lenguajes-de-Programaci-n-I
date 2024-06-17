import os
import matplotlib.pyplot as plt

# ((dT)/(dt))=k(T-T_{m})

'''
La ecuación diferencial ((dT)/(dt))=k(T-T_{m}) describe la tasa de cambio de la temperatura (T) con respecto al tiempo (t). Aquí está el significado de cada variable:

( ((dT)/(dt)) ): Es la derivada de la temperatura respecto al tiempo, que indica cómo cambia la temperatura en un instante dado.
( T ): Es la temperatura del objeto o sistema en estudio en un tiempo (t).
( T_{m} ): Es la temperatura del medio ambiente o una temperatura de referencia constante.
( k ): Es una constante de proporcionalidad que representa la tasa de enfriamiento o calentamiento y depende del sistema específico y sus propiedades.
Esta ecuación es un modelo simplificado que se usa comúnmente para describir procesos de enfriamiento o calentamiento, como la Ley de Enfriamiento de Newton.
'''

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
    def buscar_en_lista(lista, tiempo_buscado):
        actual = lista.cabeza
        while actual:
            if actual.tiempo == tiempo_buscado:
                return actual.valor
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
    plt.pause(0.05)
    euler_method(max_time, t + dt, T_next, dt)

def main():
    while True:
        print('Menu:')
        print('1> Mostrar los datos calculados')
        print('2> Ingresar una coordenada para el cálculo de error')
        print('3> Mostrar historial de coordenadas')
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
                clear()
            elif opcion == 3:
                clear()
            elif opcion == 4:
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