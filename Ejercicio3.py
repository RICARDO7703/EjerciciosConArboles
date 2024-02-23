class NodoArbol(object):
    def __init__(self, x):
        self.valor = x
        self.izquierda = None
        self.derecha = None

def es_ABB(raiz):
    pila = []
    prev = None
    
    while raiz or pila:
        while raiz:
            pila.append(raiz)
            raiz = raiz.izquierda
            
        raiz = pila.pop()
        
        if prev and raiz.valor <= prev.valor:
            return False
        
        prev = raiz
        raiz = raiz.derecha
    
    return True

raiz = NodoArbol(2)
raiz.left = NodoArbol(1)
raiz.right = NodoArbol(3)
resultado = es_ABB(raiz)
print(resultado)

raiz = NodoArbol(1)
raiz.left = NodoArbol(2)
raiz.right = NodoArbol(3)
resultado = es_ABB(raiz)
print(resultado)
