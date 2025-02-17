# -*- coding: utf-8 -*-
"""BTree Module.

BTree class definition and standard methods and functions.

*Warning:*  Set ``BTree.degree`` before any tree instanciation.

"""

from . import queue
from .queue import Queue


class BTree:
    """BTree class.

    Attributes:
        degree (int): Degree for all existing trees.
        keys (list[Any]): List of node keys.
        children (list[BTree]): List of children.
    """
    
    degree = None

    def __init__(self, keys=None, children=None):
        """BTree instance constructor.

        Args:
            keys (list[Any]).
            children (list[BTree])

        """
        self.keys = keys if keys else []
        self.children = children if children else []

    @property
    def nbkeys(self):
        """Number of keys in node.

        Returns:
            int.
        """
        return len(self.keys)



#to build examples linear rep -> B-tree
def __fromlinear(s, i=0): 
    if i < len(s) and s[i] == '(':   #useless if string well-formed
        i = i + 2 # to pass the '(<'
        B = BTree()
        while s[i] != '>':
            key = ""            
            while not(s[i] in ',>'):
                key += s[i]
                i += 1
            B.keys.append(int(key))
            if s[i] == ',':
                i += 1 
        i += 1  # to pass the '>'
        B.children = []
        while s[i] != ')':
            (C, i) = __fromlinear(s, i)
            B.children.append(C)
        i = i + 1   # to pass the ')'
        return (B, i)
    else:
        return None

def from_linear(s, d):
    BTree.degree = d
    (B, _) = __fromlinear(s)
    return B



# B-tree -> linear rep.
def __tolinear(B):
    s = '(<' 
    for i in range(B.nbkeys-1):
        s += str(B.keys[i]) + ','
    s += str(B.keys[B.nbkeys-1]) + '>'
    for child in B.children:
        s += __tolinear(child)
    s += ')'
    return s

def to_linear(B):
    if B:
        return __tolinear(B)
    else:
        return ""
        


################ Display: Serval's version

def __node_dot(ref):
    """Gets node into dot proper shape.

    Args:
        ref (BTree).

    """

    s = str(id(ref)) + '[label="'
    for i in range(ref.nbkeys-1):
        s += '<'+str(ref.keys[i])+'>'+str(ref.keys[i]) + ' | '
    s += '<'+str(ref.keys[ref.nbkeys-1])+'>'+str(ref.keys[ref.nbkeys-1])
    s +=  '"];\n'
    return s


def __link_dot(ref_a, ref_b,chid):
    """Writes down link between two BTree nodes in dot format.

    Args:
        ref_A (BTree).
        ref_B (BTree).

    """
    key=str(ref_a.keys[0 if chid==0 else chid-1])
    compass=":"+key+":s"+("w" if chid == 0 else "e")
    return "   " + str(id(ref_a)) + compass + " -- " + str(id(ref_b)) + ":n;\n"


def dot(ref):
    """Writes down dot format of tree.

    Args:
        ref (BTree).

    Returns:
        str: String storing dot format of BTree.

    """

    s = "graph " + str(ref.degree) + " {\n"
    s += "node [shape = record, height=.1];splines=false;\n"
    q = Queue()
    q.enqueue(ref)
    s += __node_dot(ref)
    while not q.isempty():
        ref = q.dequeue()
        if ref.children:
            for i in range(ref.nbkeys+1):
                child = ref.children[i]
                s += __node_dot(child)
                s += __link_dot(ref, child, i)
                q.enqueue(child)
    s += "}"
    return s

def display(ref):
    """Render a BTree to for in-browser display.

    *Warning:* Made for use within IPython/Jupyter only.

    Args:
        ref (BTree).

    Returns:
        Source: Graphviz wrapper object for BinTree rendering.

    """

    # Ensure all modules are available
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz.")
    # Generate dot and return display object
    dot_source = dot(ref)
    display(Source(dot_source))
    
    

