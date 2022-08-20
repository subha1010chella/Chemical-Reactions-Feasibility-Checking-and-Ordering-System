class ChemicalsFlow:

    def __init__(self, chemicals):
        self.C = chemicals   
        self.flows = []     
        self.chem = ["Chemical A", "Chemical B", "Chemical C", "Chemical D", "Chemical E"]

    def add_path(self, s, d, w):
        self.flows.append([s, d, w])

    def print_solution(self, dist, src):
        print("Chemicals \tFeasibility from Source")
        for i in range(self.C):
            if dist[i]==float("Inf"):
                print("Reaching {0} is not feasible from {1}".format(self.chem[i], self.chem[src]))
            else:
                print("{0}\t\t{1}KJ".format(self.chem[i], dist[i]))
            

    def bellman_ford(self, src):
        
        dist = [float("Inf")] * self.C
        
        dist[src] = 0
        
        for _ in range(self.C - 1):
            for s, d, w in self.flows:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
        

        for s, d, w in self.flows:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("{0} takes a very huge amount of heat and is in a cycle, So it is not feasible to reach other chemicals.\n".format(self.chem[src]))
                return

        self.print_solution(dist, src)
        l = []
        i = 0
        while i < len(dist):
            if dist[i] == float("Inf"):
                l.append(0)
            else:
                l.append(dist[i])
            i = i + 1
        ma = dist.index(max(l))
        mi = dist.index(min(dist))
        
        print("\nMost Feasible result: {0}".format(self.chem[ma]))
        print("\nLeast Feasible Result: {0}\n".format(self.chem[mi]))


c = ChemicalsFlow(5)
c.add_path(0, 1, -1)
c.add_path(0, 2, 4)
c.add_path(1, 2, 3)
c.add_path(1, 3, 2)
c.add_path(1, 4, 2)
c.add_path(3, 2, 5)
c.add_path(3, 1, 1)
c.add_path(4, 3, -3)

print("Chemical List \n0 - Chemical A; 1 - Chemical B; 2 - Chemical C; 3 - Chemical D; 4 - Chemical E \nEnter your choice of source chemical: ")
a=int(input())
c.bellman_ford(a)
