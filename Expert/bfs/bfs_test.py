from bfs import Node, bfs

def test():
    failed = []
    passed = []

    # 1
    t0 = Node(1, [Node(2), Node(4, [Node(3)])])
    (passed if bfs(t0, 3) == True else failed).append(1)

    # 2
    t1 = Node(1, [Node(3, [Node(4)]), Node(2)])
    (passed if bfs(t1, 3) == True else failed).append(2)

    # 3
    t2 = Node(3, [Node(1, [Node(4)]), Node(2)])
    (passed if bfs(t2, 3) == True else failed).append(3)
    
    # 4
    t3 = Node(1, [Node(2), Node(3, [Node(4)])])
    (passed if bfs(t3, 3) == True else failed).append(4)

    # 5
    t4 = Node(1, [Node(2), Node(5, [Node(4)])])
    (passed if bfs(t4, 3) == False else failed).append(5)

    # 6
    t5 = Node(1, [Node(2, [Node(3), Node(20)]), Node(5, [Node(6, [Node(21, [Node(8), Node(9), Node(10), Node(11)])])])])
    (passed if bfs(t5, 2) == True else failed).append(6)
    # 7
    (passed if bfs(t5, 4) == False else failed).append(7)
    # 8
    (passed if bfs(t5, 6) == True else failed).append(8)
    # 9
    (passed if bfs(t5, 7) == False else failed).append(9)
    # 10
    (passed if bfs(t5, 10) == True else failed).append(10)
    # 11
    (passed if bfs(t5, 11) == True else failed).append(11)

    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")

if __name__ == "__main__":
    test()
    
