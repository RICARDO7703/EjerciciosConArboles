class NodoArbol(object):
    def __init__(self, x):
        self.valor = x
        self.izquierda = None
        self.derecha = None

def kth_menor(root, k):
    pila = []
    while root or pila:
        while root:
            pila.append(root)
            root = root.izquierda
        root = pila.pop()
        k -= 1
        if k == 0:
            break
        root = root.derecha
    return root.valor

raiz = NodoArbol(8)
raiz.izquierda = NodoArbol(5)
raiz.derecha = NodoArbol(14)
raiz.izquierda.izquierda = NodoArbol(4)
raiz.izquierda.derecha = NodoArbol(6)
raiz.izquierda.derecha.izquierda = NodoArbol(8)
raiz.izquierda.derecha.derecha = NodoArbol(7)
raiz.derecha.derecha = NodoArbol(24)
raiz.derecha.derecha.izquierda = NodoArbol(22)

print(kth_menor(raiz, 2))
print(kth_menor(raiz, 3))
