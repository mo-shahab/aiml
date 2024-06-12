class graph:
    def __init__(self, graph, h, start):
        self.graph = graph
        self.h = h
        self.start = start
        self.parent = {}
        self.status = {}
        self.solutiongraph = {}
    
    def applyaostar(self):
        self.aostar(self.start, False)
    
    def getneighbors(self, n):
        return self.graph.get(n, '')

    def getstatus(self, n):
        return self.status.get(n, 0)

    def setstatus(self, n, val):
        self.status[n] = val

    def getheuristic(self, n):
        return self.h.get(n, 0)

    def setheuristic(self, n, val):
        self.h[n] = val

    def printsolution(self):
        print("the start node: ", self.start)
        print("the solution graph: ", self.solutiongraph)

    def computeminimumcost(self, v):
        mincost = 0
        costtochildnode = {}
        costtochildnode[mincost] = []
        flag = True
        for nodeinfotuplelist in self.getneighbors(v):
            cost = 0
            nodelist = []
            for nodeinfo in nodeinfotuplelist:
                c, weight = nodeinfo
                cost = cost + self.getheuristic(c) + weight
                nodelist.append(c)
            if flag == True:
                mincost = cost
                costtochildnode[mincost] = nodelist
                flag = False
            else:
                if mincost > cost:
                    mincost = cost
                    costtochildnode[mincost] = nodelist
        return mincost, costtochildnode[mincost]

    def aostar(self, v, backtracking):
        print("the heuristic: ", self.h)
        print("the start node: ", self.start)
        print("the solution graph: ", self.solutiongraph)
        if self.getstatus(v) >= 0:
            mincost, childnodelist = self.computeminimumcost(v)
            print(mincost, childnodelist)
            self.setstatus(v, len(childnodelist))
            self.setheuristic(v, mincost)
            solved = True
            for childnode in childnodelist:
                self.parent[childnode] = v
                if self.getstatus(childnode) != -1:
                    solved = solved & False
            if solved == True:
                self.setstatus(v, -1)
                self.solutiongraph[v] = childnodelist
            if self.start != v:
                self.aostar(self.parent[v], True)
            if backtracking == False:
                for childnode in childnodelist:
                    self.setstatus(childnode, 0)
                    self.aostar(childnode, False)

print("graph")

h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I':
7, 'J': 1}

gra = {
'A': [[('B', 1), ('C', 1)], [('D', 1)]],
'B': [[('G', 1)], [('H', 1)]],
'C': [[('J', 1)]],
'D': [[('E', 1), ('F', 1)]],
'G': [[('I', 1)]]
}

gr = graph(gra, h1, 'A')
gr.applyaostar()
gr.printsolution()
