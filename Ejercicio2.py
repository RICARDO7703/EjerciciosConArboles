class NodoArbol(object):
    def __init__(self, x):
        self.valor = x
        self.izquierda = None
        self.derecha = None

def valor_mas_cercano(raiz, objetivo):
    a = raiz.valor
    hijo = raiz.izquierda if objetivo < a else raiz.derecha
    if not hijo:
        return a
    b = valor_mas_cercano(hijo, objetivo)
    return min((a, b), key=lambda x: abs(objetivo - x))

raiz = NodoArbol(8)
raiz.izquierda = NodoArbol(5)
raiz.derecha = NodoArbol(14)
raiz.izquierda.izquierda = NodoArbol(4)
raiz.izquierda.derecha = NodoArbol(6)
raiz.izquierda.derecha.izquierda = NodoArbol(8) 
raiz.izquierda.derecha.derecha = NodoArbol(7) 
raiz.derecha.derecha = NodoArbol(24) 
raiz.derecha.derecha.izquierda = NodoArbol(22)

resultado = valor_mas_cercano(raiz, 19) 
print(resultado)
