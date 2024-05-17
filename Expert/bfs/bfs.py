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

def test():
    failed = []
    passed = []

    # 1
    t0 = Node(1, [Node(2), Node(4, [Node(3)])])
    (passed if search(t0, 3) == True else failed).append(1)

    # 2
    t1 = Node(1, [Node(3, [Node(4)]), Node(2)])
    (passed if search(t1, 3) == True else failed).append(2)

    # 3
    t2 = Node(3, [Node(1, [Node(4)]), Node(2)])
    (passed if search(t2, 3) == True else failed).append(3)
    
    # 4
    t3 = Node(1, [Node(2), Node(3, [Node(4)])])
    (passed if search(t3, 3) == True else failed).append(4)

    # 5
    t4 = Node(1, [Node(2), Node(5, [Node(4)])])
    (passed if search(t4, 3) == False else failed).append(5)

    # 6
    t5 = Node(1, [Node(2, [Node(3), Node(20)]), Node(5, [Node(6, [Node(21, [Node(8), Node(9), Node(10), Node(11)])])])])
    (passed if search(t5, 2) == True else failed).append(6)
    # 7
    (passed if search(t5, 4) == False else failed).append(7)
    # 8
    (passed if search(t5, 6) == True else failed).append(8)
    # 9
    (passed if search(t5, 7) == False else failed).append(9)
    # 10
    (passed if search(t5, 10) == True else failed).append(10)
    # 11
    (passed if search(t5, 11) == True else failed).append(11)

    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")

if __name__ == "__main__":
    print(Node(1, [Node(2), Node(4, [Node(3)])]))
    test()
    
