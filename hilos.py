# -*- coding: utf-8 -*-

import threading
import time


def ejecutar_hilo(funcion, parametros=(), daemon=True, func_rta=None,
                  no_bloquear=False):
    '''
        Este método se encarga de ejecutar una función en un hilo.

        Argumentos:
            funcion (function)
            parametros (tuple)
            deamon (bool)
            func_rta (function)

        Retorna:
            None
    '''

    # Si tengo una función de respuesta
    if func_rta is not None:
        # Agrego a la función principal un decorador con la función de respuesta
        funcion = con_rta(funcion, func_rta)

    # Si tengo una función que bloque el proceso.
    if no_bloquear is True:
        funcion = func_no_bloquear(funcion)

    # Creo un hilo con la función recibida y sus parámetros
    hilo = threading.Thread(
        target=funcion,
        args=parametros,
    )
    # Si es un demonio
    if daemon is True:
        # Seteo deamon en True para que se muera junto con la función
        hilo.daemon = True
    # Inicio el hilo
    hilo.start()


def ejecutar_tarea(funcion, parametros, segundos):
    '''
        Este método se encarga de ejecutar una función como una tarea en un hilo
        cada el tiempo que se le indique en segundos.

        Argumentos:
            funcion (function)
            parametros (tuple)
            segundos (int)

        Funciones:
            ejecutar_hilo

        Retorna:
            None
    '''

    # Creo una función
    def tarea():
        # Esta se va a ejecutar infinitamente
        while True:
            # Cada tanto tiempo según los segundos seteados
            time.sleep(segundos)
            # Ejecuto la función dada con sus parámetros
            funcion(*parametros)
    # Ejecuto la función "tarea" en un hilo
    ejecutar_hilo(tarea)


# Este decorador ejecuta una función de respuesta al terminar la ejecución
# de la función principal
def con_rta(func, func_rta):
    def ejecutar(*args, **kwargs):
        # Ejecuto la función decorada
        rta = func(*args, **kwargs)
        # Ejecuto la función de respuesta pasandole como parámetro el resultado
        # de la función original
        func_rta(rta)
        return rta
    return ejecutar


# Este decorador ejecuta una función bloqueante.
def func_no_bloquear(func):
    def ejecutar(*args, **kwargs):

        # Pongo un sleep para que no me bloquee el proceso.
        time.sleep(0.00001)

        # Ejecuto la función decorada
        rta = func(*args, **kwargs)
        # Ejecuto la función de respuesta pasandole como parámetro el resultado
        # de la función original

        return rta
    return ejecutar

