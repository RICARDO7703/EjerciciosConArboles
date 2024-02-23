class NodoArbol(object):
    def __init__(self, x):
        self.valor = x
        self.izquierda = None
        self.derecha = None

def array_a_arbol_bst(array_nums):
    if not array_nums:
        return None
    
    mitad_num = len(array_nums) // 2
    nodo = NodoArbol(array_nums[mitad_num])
    nodo.izquierda = array_a_arbol_bst(array_nums[:mitad_num])
    nodo.derecha = array_a_arbol_bst(array_nums[mitad_num + 1:])
    
    return nodo

def preorden(nodo):
    if not nodo:
        return
    print(nodo.valor, end=" ")
    preorden(nodo.izquierda)
    preorden(nodo.derecha)

array_nums = [1, 2, 3, 4, 5, 6, 7]
print("Arreglo original:")
print(array_nums)

resultado = array_a_arbol_bst(array_nums)
print("\nArreglo a un BST balanceado en altura:")
preorden(resultado)
