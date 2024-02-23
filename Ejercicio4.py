# Definición: Nodo de un árbol binario.
class NodoArbol(object):
    def __init__(self, x):
        self.valor = x
        self.izquierda = None
        self.derecha = None

def eliminar_nodo(raiz, clave):
    # Si la raíz no existe, simplemente la retornamos.
    if not raiz:
        return raiz

    # Buscamos el nodo en el subárbol izquierdo si el valor de la clave es menor que el valor de la raíz.
    if clave < raiz.valor:
        raiz.izquierda = eliminar_nodo(raiz.izquierda, clave)
    # Buscamos el nodo en el subárbol derecho si el valor de la clave es mayor que el valor de la raíz.
    elif clave > raiz.valor:
        raiz.derecha = eliminar_nodo(raiz.derecha, clave)
    # Eliminamos el nodo si el valor de la raíz es igual a la clave.
    else:
        # Si no hay hijos derechos, eliminamos el nodo y la nueva raíz sería raiz.izquierda.
        if not raiz.derecha:
            return raiz.izquierda
        # Si hay hijos izquierdos y derechos, reemplazamos su valor con el valor mínimo en el subárbol derecho.
        raiz.valor = encontrar_minimo(raiz.derecha).valor
        # Eliminamos el nodo mínimo en el subárbol derecho.
        raiz.derecha = eliminar_nodo(raiz.derecha, raiz.valor)

    return raiz

def encontrar_minimo(nodo):
    actual = nodo
    while actual.izquierda:
        actual = actual.izquierda
    return actual

def preorden(nodo):
    if not nodo:
        return
    print(nodo.valor, end=" ")
    preorden(nodo.izquierda)
    preorden(nodo.derecha)

# Creación del árbol original
raiz = NodoArbol(5)
raiz.izquierda = NodoArbol(3)
raiz.derecha = NodoArbol(6)
raiz.izquierda.izquierda = NodoArbol(2)
raiz.izquierda.derecha = NodoArbol(4)
raiz.izquierda.derecha.izquierda = NodoArbol(7)

print("Nodo original:")
preorden(raiz)

# Eliminación del nodo especificado
resultado = eliminar_nodo(raiz, 4)

print("\nDespués de eliminar el nodo especificado:")
preorden(resultado)
