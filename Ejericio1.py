class arboles_nodos(object):
    def __int__(self,x):
        self.val = x
        self.izquierda = None
        self.derecha = None

def sorted_array_to_bst(num):
    if not num:
        return None
    mid_vad = len(num)//2
    node = arboles_nodos(num[mid_vad])
    node.izquierda = sorted_array_to_bst(num[:mid_vad])
    node.derecha = sorted_array_to_bst(num[:mid_vad+1:])
    return node

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.izquierda)
    preOrder(node.derecha)
    
    resultado = sorted_array_to_bst([1,2,3,4,5,6,7])
    preOrder(resultado)