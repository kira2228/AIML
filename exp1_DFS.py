graph={
    '1':['2','3'],
    '2':['4','5'],
    '3':[],
    '4':[],
    '5':['6'],
    '6':[]
}
visited=[]
stack=[]
def dfs(visited,graph,node):
    if node not in visited:
        visited.append(node)
        stack.append(node)
       
        n=stack.pop(0)
        print(n,end=" ")
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
print("DFS nodes are:")
dfs(visited,graph,'1')
               
