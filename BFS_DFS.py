from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph,start):
    visited = set()
    Queue = deque([start])
    while Queue:
        node = Queue.popleft()
        if node not in visited:
            print(node,end =" ")
            visited.add(node)
            Queue.extend(graph[node])



def dfs(graph,strat,visit=None):
    if visit is  None:
        visit = set()
    visit.add(strat)
    print(strat,end=" ")
    for side in graph[strat]:
        if side not in visit:
            dfs(graph,side,visit)
        

bfs(graph,'A')
print(end="  ")
dfs(graph,'A')

