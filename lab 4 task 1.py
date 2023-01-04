class Node :

    def __init__(self,state,parent,actions,totalCost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.totalCost=totalCost
def DFS():
    initial= input("Enter initial Node: ")
    goal = input("Enter destination Node: ")
    
    graph={
        'Oradea' : Node('Oradea',None,['Zerind','Sibiu'],[71,151] ),
        'Zerind' : Node('Zerind',None,['Arad', 'Oradea'],[75,71 ]),
        'Arad' : Node('Arad',None,['Zerind','Timisoara','Sibiu'],[75,118,140] ),
        'Sibiu' : Node('Sibiu',None,['Fagaras','Rimnicu Vilcea','Oradea','Arad'],[99,80,151,140] ),
        'Fagaras' : Node('Fagaras',None,['Sibiu','Bucharest'],[99,211] ),
        'Bucharest' : Node('Bucharest',None,['Fagaras','Pitesti','Urziceni','Giurgiu'],[211,101,85,90] ),
        'Pitesti' : Node('Pitesti',None,['Rimnicu Vilcea','Bucharest','Craiova'],[97,101,138] ),
        'Urziceni' : Node('Urziceni',None,['Bucharest','Hirsova','Vaslui'],[85,98,142] ),
        'Hirsova' : Node('Hirsova',None,['Urziceni','Eforie'],[98,86] ),
        'Timisoara':Node('Timisoara',None,['Lugoj','Arad'],[111,118]),
        'Lugoj':Node('Lugoj',None,['Mehadia','Timisoara'],[70,111]),
        'Mehadia':Node('Mehadia',None,['Drobeta','Lugoj'],[75,70]),
        'Rimnicu Vilcea':Node('Rimnicu Vilcea',None,['Sibiu','Pitesti'],[70,111]),
        'Drobeta' : Node('Drobeta',None,['Craiova','Mehadia'],[120,75] ),
        'Craiova' : Node('Craiova',None,['Pitesti','Rimnicu Vilcea'],[138,146] ),
        'Eforie' : Node('Eforie',None,['Hirsova'],[86] ),
        'Vaslui' : Node('Vaslui',None,['Urziceni','Iasi'],[142,92] ),
        'Iasi' : Node('Iasi',None,['Vaslui','Neamt'],[92,87] ),
        'Giurgiu' : Node('Giurgiu',None,[],[]),
        'Neamt' : Node('Neamt',None,[],[] ),
        }
    front=[initial]
    explore=[]
    while(len(front)!=0):
         cNode=front.pop(len(front)-1)
         print (cNode)
         explore.append(cNode)
         cChild=0
         for i in graph[cNode].actions :
            if i not in front and i not in explore : 
                if graph[i].state==goal:
                    return actionSequence(graph,initial,goal)
                cChild=cChild+1
                front.append(i)
         if cChild==0:
            del explore[len(explore)-1]
def actionSequence(graph,initial,goal):
    sol=[goal]
    cp=graph[goal].parent
    while cp!=None:
        sol.append(cp)
        cp=graph[cp].parent
    sol.reverse()
    return sol

sol=DFS()
print(sol)

//Enter initial Node: Arad
//Enter destination Node: Bucharest
//Arad
//Sibiu
//Oradea
//Rimnicu Vilcea
//Pitesti
//['Bucharest']
          
