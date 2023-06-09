# -*- coding: utf-8 -*-
"""Copia de LogicBot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pSr_PrUMOeF6djDfUm59jFjYFWbJTw05
"""

from kanren import Relation, facts, run, conde, var

father = Relation()
mother = Relation()

facts(
    father,
    ("Vito", "Michael"),
    ("Vito", "Sonny"),
    ("Vito", "Fredo"),
    ("Michael", "Anthony"),
    ("Michael", "Mary"),
    ("Sonny", "Vicent"),
    ("Sonny", "Francesca"),
    ("Sonny", "Kathryn"),
    ("Sonny", "Frank"),
    ("Sonny", "Santino"),
)

facts(
    mother,
    ("Carmela", "Michael"),
    ("Carmela", "Sonny"),
    ("Carmela", "Fredo"),
    ("Kay", "Mary"),
    ("Kay", "Anthony"),
    ("Sandra", "Francesca"),
    ("Sandra", "Kathryn"),
    ("Sandra", "Frank"),
    ("Sandra", "Santino"),
)

q = var()
def buscar_hijos(papa): 
  print((run(0, q, father(papa, q))))
# ('Sonny', 'Michael', 'Fredo')

def agregar_vinculo_padre(a,b):
  facts(father,(a,b))

def agregar_vinculo_madre(a,b):
  facts(mother,(a,b))

def parent(p, child): 
    return conde([father(p, child)], [mother(p, child)])
# devuelve ambos padres del sujeto

def grandparent(gparent, child):
    p = var()
    return conde((parent(gparent, p), parent(p, child)))

def sibling(a, b):
    p = var()
    return conde((parent(p, a), parent(p, b)))


while True:
    opcion = input("Ingresa una opción (1: Añadir vínculo familiar, 2: Buscar hermanos, 3: Salir): ")
    if opcion == "1":
        papa = input("Ingresa el nombre del padre: ")
        hijo = input("Ingresa el nombre del hijo: ")
        agregar_vinculo_padre(papa,hijo)
    elif opcion == "2":
        a = input("Ingresa el nombre de a: ")
        b = input("Ingresa el nombre de b: ")
        print((run(0, q, sibling(a,b))))
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intenta nuevamente.")