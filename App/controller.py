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
 """

import config as cf
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {'model': None}
    control['model'] = model.new_data_structs()
    return control
    

# Funciones para la carga de datos

def load_data(control, siz):
    """
    Carga los datos del reto
    """
    
    # TODO: Realizar la carga de datos
    size = tamaño_archivo(siz)
    control['model'] = model.new_data_structs()
    catalog = control['model']
    
    jobs = load_jobs(catalog, size)
    skills = load_skills(catalog, size)
    employment_types = load_employment_types(catalog, size)
    multilocation = load_multilocation(catalog, size)

    return jobs, skills, employment_types, multilocation

#funciones axuliares de carga 
def tamaño_archivo (size):
    tamaño = int(size)
    size1 = 'small'
    if tamaño == 2:
        size1 = "10-por"
    if tamaño == 3:
        size1 = "20-por"
    if tamaño == 4:
        size1 = "30-por"
    if tamaño == 5:
        size1 = "40-por"
    if tamaño == 6:
        size1 = "50-por"
    if tamaño == 7:
        size1 = "60-por"
    if tamaño == 8:
        size1 = "70-por"
    if tamaño == 9:
        size1 = "80-por"
    if tamaño == 10:
        size1 = "90-por"
    if tamaño == 11:
        size1 = "small"
    if tamaño == 12:
        size1 = "medium"
    if tamaño == 13:
        size1 = "large"
    return size1
        
    
def load_jobs(catalog, size):
    jobs = cf.data_dir + "archivos/data/"+ str(size) + "-jobs.csv"
    input_file = csv.DictReader(open(jobs, encoding="utf-8"), delimiter=";")
    for job in input_file:
        model.add_jobs(catalog, job)
    return model.jobs_size(catalog)

def load_skills(catalog, size):
    skills = cf.data_dir + "archivos/data/"+ size + "-skills.csv"
    input_file = csv.DictReader(open(skills, encoding="utf-8"),  delimiter=";")
    for skill in input_file:
        model.add_skills(catalog, skill)
    return model.skills_size(catalog)

def load_employment_types(catalog, size):
    employment_types = cf.data_dir + "archivos/data/"+ size + "-employments_types.csv"
    input_file = csv.DictReader(open(employment_types, encoding="utf-8"),  delimiter=";")
    for employment_type in input_file:
        model.add_employments_type(catalog, employment_type)
    return model.employments_type_size(catalog)

def load_multilocation(catalog, size):
    multilocations = cf.data_dir + "archivos/data/"+ size + "-multilocations.csv"
    input_file = csv.DictReader(open(multilocations, encoding="utf-8"),  delimiter=";")
    for multilocation in input_file:
        model.add_multilocations(catalog, multilocation)
    return model.multilocations_size(catalog)

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    catalog = control['model']
    model.sort_data(catalog)
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    catalog = control['model']
    return model.get_data(catalog, id)
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass

def req_2_1(x, repositorio):
        x.repositorio = repositorio
    
def req_2(x, n, nombre_empresa, ciudad):
        return x.repositorio.req_2_1(n, nombre_empresa, ciudad)


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


 
def req4_1(x, repositorio):
        x.repositorio = repositorio
    
def req_4(x, codigo_pais, fecha_inicio, fecha_fin):
        return x.repositorio.obtener_ofertas_en_periodo(codigo_pais, fecha_inicio, fecha_fin)

   # TODO: Modificar el requerimiento 4
def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
