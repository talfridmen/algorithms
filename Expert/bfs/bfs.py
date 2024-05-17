def search(t, val):
    pass # implement here


class Node:
    def __init__(self, val, children=None) -> None:
        self._val = val
        self._children = children or list()
    
    @property
    def value(self):
        return self._val
    
    @property
    def children(self):
        return tuple(self._children)
    
    def append(self, child):
        if isinstance(child, int):
            child = self.__class__(child)
        if isinstance(child, self.__class__):
            self._children.append(child)
        else:
            raise ValueError("child must be int or Node")
        
    def _to_string(self, indent=0, last=False):
        sign = '\u2514' if last else '\u251c'
        st = f"{'| ' * indent}{sign} {self._val}\n"
        if self._children:
            for child in self._children[:-1]:
                st += child._to_string(indent+1)
            st += self._children[-1]._to_string(indent+1, last=True)
        return st

    def __str__(self) -> str:
        return self._to_string(last=True)

if __name__ == "__main__":
    t0 = Node(1, [Node(2), Node(4, [Node(3)])])
    print(search(t0, 3))  # True

    t1 = Node(1, [Node(3, [Node(4)]), Node(2)])
    print(search(t1, 3))  # True

    t2 = Node(3, [Node(1, [Node(4)]), Node(2)])
    print(search(t2, 3))  # True

    t3 = Node(1, [Node(2), Node(3, [Node(4)])])
    print(search(t3, 3))  # True

    t4 = Node(1, [Node(2), Node(5, [Node(4)])])
    print(search(t4, 3))  # False

    t5 = Node(1, [Node(2, [Node(3), Node(20)]), Node(5, [Node(6, [Node(21, [Node(8), Node(9), Node(10), Node(11)])])])])
    print(search(t5, 2))  # True
    print(search(t5, 4))  # False
    print(search(t5, 6))  # True
    print(search(t5, 7))  # False
    print(search(t5, 10)) # True
    print(search(t5, 11)) # True
