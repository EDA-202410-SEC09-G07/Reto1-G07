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


import datetime
from os import F_OK
from re import sub
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


def new_data_structs():
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


{}
# Funciones para creacion de datos

def new_data(id, info):
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
    


def req_1(data_structs, N, code_country, level):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    
    jobs = data_structs['jobs']
    
    sublist = lt.newList(datastructure="ARRAY_LIST", cmpfunction=compare)
    
    for job in lt.iterator(jobs):
        if job['country_code'] == code_country and job['experience_level'] == level:
            lt.addLast(sublist, job)

    merg.sort(sublist, sort_by_date)
    
    if N > lt.size(sublist):
        return sublist
    
    sublist = lt.subList(sublist, 1, N)
    
    return sublist

        
    

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs, company_name, initial_date, final_date):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    
    initial_date = datetime.datetime.strptime(initial_date, '%Y-%m-%d')
    initial_date = initial_date.date()
    final_date = datetime.datetime.strptime(final_date, '%Y-%m-%d')
    final_date = final_date.date()
    
    jobs = data_structs['jobs']
    
    sublist = lt.newList(datastructure="ARRAY_LIST", cmpfunction=compare)
    
    junior = 0
    mid = 0
    senior = 0
    
    for job in lt.iterator(jobs):
        if job['company_name'] == company_name and job['published_at'].date() >= initial_date and job['published_at'].date() <= final_date:
            lt.addLast(sublist, job)
            if job['experience_level'] == 'junior':
                junior += 1
            elif job['experience_level'] == 'mid':
                mid += 1
            else:
                senior += 1
    
    merg.sort(sublist, sort_by_date_and_country)
    
    return sublist, junior, mid, senior
            
    
    


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


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
    
    if data_1['id'] == data_2['id']:
        return 0
    elif data_1['id'] > data_2['id']:
        return 1
    else:
        return -1
    
    
    

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

def sort_by_date_and_country(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    
    if data_1['published_at'] == data_2['published_at']:
        return data_1['country_code'] < data_2['country_code']
    elif data_1['published_at'] > data_2['published_at']:
        return True
    else:
        return False

def sort_by_date(data_1, data_2):
    
    return data_1['published_at'] > data_2['published_at']


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

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


import datetime
from os import F_OK
from re import sub
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


def new_data_structs():
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


{}
# Funciones para creacion de datos

def new_data(id, info):
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
    


def req_1(data_structs, N, code_country, level):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    
    jobs = data_structs['jobs']
    
    sublist = lt.newList(datastructure="ARRAY_LIST", cmpfunction=compare)
    
    for job in lt.iterator(jobs):
        if job['country_code'] == code_country and job['experience_level'] == level:
            lt.addLast(sublist, job)

    merg.sort(sublist, sort_by_date)
    
    if N > lt.size(sublist):
        return sublist
    
    sublist = lt.subList(sublist, 1, N)
    
    return sublist

        
    

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs, company_name, initial_date, final_date):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    
    initial_date = datetime.datetime.strptime(initial_date, '%Y-%m-%d')
    initial_date = initial_date.date()
    final_date = datetime.datetime.strptime(final_date, '%Y-%m-%d')
    final_date = final_date.date()
    
    jobs = data_structs['jobs']
    
    sublist = lt.newList(datastructure="ARRAY_LIST", cmpfunction=compare)
    
    junior = 0
    mid = 0
    senior = 0
    
    for job in lt.iterator(jobs):
        if job['company_name'] == company_name and job['published_at'].date() >= initial_date and job['published_at'].date() <= final_date:
            lt.addLast(sublist, job)
            if job['experience_level'] == 'junior':
                junior += 1
            elif job['experience_level'] == 'mid':
                mid += 1
            else:
                senior += 1
    
    merg.sort(sublist, sort_by_date_and_country)
    
    return sublist, junior, mid, senior
            
    
    


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


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
    
    if data_1['id'] == data_2['id']:
        return 0
    elif data_1['id'] > data_2['id']:
        return 1
    else:
        return -1
    
    
    

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

def sort_by_date_and_country(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    
    if data_1['published_at'] == data_2['published_at']:
        return data_1['country_code'] < data_2['country_code']
    elif data_1['published_at'] > data_2['published_at']:
        return True
    else:
        return False

def sort_by_date(data_1, data_2):
    
    return data_1['published_at'] > data_2['published_at']


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

