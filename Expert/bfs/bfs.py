def bfs(t, val):
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

    def __repr__(self):
        return f"tree: val={self.value} ({len(self.children)} children)"

if __name__ == "__main__":
    t = Node(1, [Node(2), Node(4, [Node(3)])])
    print(f"tree value: {t.value}")
    print(f"tree children: {t.children}")
    print(f"first child value: {t.children[0].value}")
    print(f"second child value: {t.children[1].value}")
    print(f"second child's children: {t.children[1].children}")
