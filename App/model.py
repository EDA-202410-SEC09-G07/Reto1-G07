"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(ARRAY_LIST):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {'jobs': None,
               'multilocations': None,
               'skills': None,
               'employments_types': None}

    data_structs['jobs'] = lt.newList('ARRAY_LIST')
    data_structs['multilocations'] = lt.newList('ARRAY_LIST')
    data_structs['skills'] = lt.newList('ARRAY_LIST')
    data_structs['employments_type'] = lt.newList('ARRAY_LIST')
               
    return data_structs


# Funciones para agregar informacion al modelo

def add_employments_type(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs['employments_type'], data)

    
    return data_structs

def add_jobs(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs['jobs'], data)

    
    return data_structs

def add_multilocations(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs['multilocations'], data)

    
    return data_structs

def add_skills(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs['skills'], data)

    
    return data_structs

def jobs_size(data_structs):
    return lt.size(data_structs['jobs'])

def multilocations_size(data_structs):
    return lt.size(data_structs['multilocations'])

def skills_size(data_structs):
    return lt.size(data_structs['skills'])

def employments_type_size(data_structs):
    return lt.size(data_structs['employments_type'])



# Funciones para creacion de datos

def new_data(id, info, data_structs, data):
    """
    Crea una nueva estructura para modelar los datos
    """
    data_n = {'id': None, 'info': None}
    data_n['id'] = id
    data_n['info'] = info
    
    return data_n


def newjobs(name,id ):
    job = {"name": "", "books": None }
    job["name"] = name
    job["jobs"] = lt.newList("ARRAY_LIST")
    return job

def newemployment(name,id ):
    job = {"name": "", "books": None }
    job["name"] = name
    job["jobs"] = lt.newList("ARRAY_LIST")
    return job
def newmultilocations(name,id ):
    job = {"name": "", "books": None }
    job["name"] = name
    job["jobs"] = lt.newList("ARRAY_LIST")
    return job
# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos = lt.isPresent(data_structs['id'], id)
    if pos > 0:
        data = lt.getElement(data_structs['id'], pos)
        return data
    return None



def data_size(data_structs, data):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs[data])
    


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass

def req_2_1(x, fecha, pais, ciudad, nombre_emp, titulo, expertise, formato_aplicacion, trabajo_remoto):
        x.fecha = fecha
        x.pais = pais
        x.ciudad = ciudad
        x.nombre_empresa = nombre_emp
        x.titulo = titulo
        x.expertise = expertise
        x.formato_aplicacion = formato_aplicacion
        x.trabajo_remoto = trabajo_remoto

def req_2_2(x, estructuras_de_datos):
    x.estructuras_de_datos = estructuras_de_datos
    
def req_2(x, n, nombre_emp, ciudad):
    ofertas_filtradas = [oferta for oferta in x.estructuras_de_datos if oferta.nombre_empresa == nombre_emp and oferta.ciudad == ciudad]
    ofertas_ordenadas = quk(ofertas_filtradas, key=lambda x: x.fecha, reverse=True)[:n]
    return ofertas_ordenadas


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req4_1 (x, pais, fecha, titulo, habilidad, nombre_emp, ciudad, localizacion, trabajo_remoto, contratar_uk):
        x.pais = pais
        x.fecha = fecha
        x.titulo = titulo
        x.habilidad = habilidad
        x.nombre_empresa = nombre_emp
        x.ciudad_empresa = ciudad
        x.ubicacion_trabajo = localizacion
        x.trabajo_remoto = trabajo_remoto
        x.contratar_ucranianos = contratar_uk
        
def req4_2(x, estructuras_de_datos):
        x.estructuras_de_datos = estructuras_de_datos
    
def req4 (x, pais_cod, fecha_inicio, fecha_fin):
        ofertas_filtradas = []
        for oferta in x.estructuras_de_datos:
            if (oferta.pais == pais_cod and 
                fecha_inicio <= oferta.fecha <= fecha_fin):
                ofertas_filtradas.append(oferta)
        return ofertas_filtradas



def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
