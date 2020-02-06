
"""
LABORATORIO #2
----------------------------------------------------------------------
"""

from Sorting import selectionsort as selsort
from Sorting import insertionsort as inssort
from Sorting import shellsort as shellsort

from time import process_time

def sort(option, elements, function):
    if option == 1:
        print ("sorting by selection sort....")
        t1_start = process_time() #tiempo inicial
        selsort.selectionSort(elements, function)
    if option == 2:
        print ("sorting by insertion sort....")
        t1_start = process_time() #tiempo inicial
        inssort.insertionSort(elements, function)
    if option == 3:
        print ("sorting by shell sort....")
        t1_start = process_time() #tiempo inicial
        shellsort.shellSort(elements, function)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")