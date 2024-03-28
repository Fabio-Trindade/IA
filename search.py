from abc import ABC
import heapq

class IBoundary(ABC):
    def __init__(self):
        pass
    def append(self,state,cost):
        pass
    def pop(self):
        pass
    def is_empty(self):
        pass

class MyQueue(IBoundary):
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list) == 0
    
    def pop(self):
        return self.list.pop(0)
    
    def append(self,state,cost):
        self.list.append((cost, state))

class MyStack(IBoundary):
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list) == 0
    
    def pop(self):
        return self.list.pop()
    
    def append(self, state,cost):
        self.list.append((cost,state))

class MyHeap(IBoundary):
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list) == 0
    
    def pop(self):
        return heapq.heappop(self.list)
    
    def append(self, state, cost):
        heapq.heappush(self.list,(cost,state))

    

def base_search(init_state, final_state,level, get_valid_transictions, boundary: IBoundary, h_func = None,enable_cost = False):
    boundary.append(init_state,0)

    visited = {init_state:True}
    father = {}
    if enable_cost:
        cost = {}
        cost[init_state] = 0

    while not boundary.is_empty():
        _,curr_state = boundary.pop()

        if curr_state == final_state:
            aux = final_state
            path = []
            while aux != init_state:
                path.append(aux)
                aux = father[aux]
            path.append(aux)
            return path, visited

        for neighboor_state,neighboor_cost in get_valid_transictions(level,curr_state):
            if enable_cost:
                child_cost = cost[curr_state] + neighboor_cost

            if neighboor_state not in visited.keys() or (enable_cost and child_cost < cost[neighboor_state]):
                h_cost = h_func(final_state,neighboor_state) if h_func != None else 0
                boundary.append(neighboor_state,(0 if  not enable_cost else child_cost) + h_cost)
                visited[neighboor_state] = True
                father[neighboor_state] = curr_state
                if enable_cost:
                    cost[neighboor_state] = child_cost

    return [],visited