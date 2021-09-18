from ExamenFinalEDA.arbolesBinarios.binarytree import Node
def compararNodos(nodo1, nodo2):
    return _compararNodos(nodo1.parent, nodo2.parent)


def _compararNodos(nodo1, nodo2):
    if nodo1 is None and nodo2 is None:
        return True
    if nodo1 is not None and nodo2 is None or nodo1 is None and nodo2 is not None:
        return False
    if nodo1.elem != nodo2.elem:
        return False
    else:
        return _compararNodos(nodo1.right, nodo2.right) and _compararNodos(nodo1.left, nodo2.left)


Nodo1 = Node(2)
Nodo1.right = Node(4)
Nodo1.left = Node(3)
Nodo2 = Node(2)
Nodo2.right = Node(4)
Nodo2.left = Node(3)
Nodo1.parent = Node(3)
Nodo2.parent = Node(3)
Nodo1.parent.left = Nodo1
Nodo2.parent.left = Nodo2
print(Nodo1.compararNodos(Nodo1,Nodo2))