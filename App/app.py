"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time

"""
LABORATORIO #2
----------------------------------------------------------------------
"""

from Sorting import sorting_path as sort
# 1 - Selection Sort
# 2 - Insertion Sort
# 3 - Shell Sort

def less_v2(element1, element2):
    if int(element1["vote_count"]) <  int(element2["vote_count"]):
        return True
    return False

def greater(element1, element2):
    if int(element1["vote_average"]) >  int(element2["vote_average"]):
        return True
    return False

"""
----------------------------------------------------------------------
"""

def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(file, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            lt.addLast(lst,row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    """
    LABORATORIO #1
    """
    print("4- Consultar elementos a partir de dos listas")
    """
    LABORATORIO #2
    """
    print("5- Organizar elementos por vote_count (menor a mayor) eligiendo el algoritmo de ordenamiento")
    print("6- Organizar elementos por vote_average (mayor a menor) eligiendo el algoritmo de ordenamiento")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0

def main():
    ratings_list = None
    casting_list = None
    datos_cargados = False
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                ratings_list = loadCSVFile("Data/AllMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                print("Datos cargados, ",ratings_list['size']," elementos cargados")
                casting_list = loadCSVFile("Data/AllMoviesCastingRaw.csv") #llamar funcion cargar datos
                print("Datos cargados, ",casting_list['size']," elementos cargados")

                print(" 1 - Selection Sort")
                print(" 2 - Insertion Sort")
                print(" 3 - Shell Sort")
                option = input('Con que algoritmo desea organizar los datos?\n')

                """
                TOCA CAMBIAR
                """
                #Crear catálogos: - vote_average - vote_count - directores - actores - género
                #Organizarlos
                datos_cargados = True

            elif int(inputs[0])==2: #opcion 2
                if not datos_cargados:
                    print("Debe cargar los datos primero")
                else:
                    if casting_list==None or casting_list['size']==0: #obtener la longitud de la lista
                        print("La lista esta vacía")    
                    else:
                        print("La lista tiene ",casting_list['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if not datos_cargados:
                    print("Debe cargar los datos primero")
                else:
                    if casting_list==None or casting_list['size']==0: #obtener la longitud de la lista
                        print("La lista esta vacía")
                    else:   
                        criteria =input('Ingrese el criterio de búsqueda\n')
                        counter=countElementsFilteredByColumn(criteria, "nombre", casting_list) #filtrar una columna por criterio  
                        print("Coinciden ",counter," elementos con el criterio: ", criteria)

            elif int(inputs[0]) == 4:#opcion 4
                if not datos_cargados:
                    print("Debe cargar los datos primero")
                else:
                    if casting_list==None or casting_list['size']==0: #obtener la longitud de la lista
                        print("La lista esta vacía")
                    else:
                        criteria =input('Ingrese el criterio de búsqueda\n')
                        counter=countElementsByCriteria(criteria,0,casting_list)
                        print("Coinciden ",counter," elementos con el criterio: ", criteria ," (en construcción ...)")
                        
            elif int(inputs[0])==5: #opcion 5
                if not datos_cargados:
                    print("Debe cargar los datos primero")
                else:
                    if casting_list==None or casting_list['size']==0: #obtener la longitud de la lista
                        print("La lista esta vacía")
                    else:
                        print(" 1 - Selection Sort")
                        print(" 2 - Insertion Sort")
                        print(" 3 - Shell Sort")
                        option = input('Seleccione una opción para continuar\n')
                        #Hacer sort con less_v2
            elif int(inputs[0])==6: #opcion 6
                if not datos_cargados:
                    print("Debe cargar los datos primero")
                else:
                    if casting_list==None or casting_list['size']==0: #obtener la longitud de la lista
                        print("La lista esta vacía")
                    else:
                        print(" 1 - Selection Sort")
                        print(" 2 - Insertion Sort")
                        print(" 3 - Shell Sort")
                        option = input('Seleccione una opción para continuar\n')
                        #Hacer sort con greater
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()