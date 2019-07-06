'''
import sys
from queue import PriorityQueue
from heapq import heappush, heappop

def create_graph(filename):
	graph = {}
	file = open(filename, 'r')
	for line in file:
		if 'END OF INPUT' in line:
			return graph
		city1, city2, d = line.split()
		graph.setdefault(city1, []).append((city2, d))
		graph.setdefault(city2, []).append((city1, d))

def ucs(graph, start, goal):
	visited = set()
	path = []
	queue = PriorityQueue()
	
	queue.put((0, [start]))
	while queue:

		if queue.empty():
			print('distance: infinity\nroute: \nnone')
			return

		cost, path = queue.get()
		node = path[len(path)-1]
		if node not in visited:
			visited.add(node)
			if node == goal:
				path.append(cost)
				return path
			for n in neighbors(graph, node):
				if n not in visited:
					total_cost = cost + int(get_cost(graph, node, x))
					temp = path[:]
					temp.append(n)
					queue.put((total_cost, temp))

	def neighbors(graph, node):
		elem = graph[node]
		return [n[0] for n in elem]

	def get_cost(graph, s_node, e_node):
		pos =[n[0] for n in graph[s_node]].index(e_node)
		return graph[s_node][position][1]

	def display_path(graph, path):
		distance = path[-1]
		print('distance: '+ distance)
		print('route: ')
		
		for x in path[:-2]:
			y = path.index(x)
			position = [z[0] for z in graph[x]].index(path[y+1])
			cost = graph[x][position][1]
			print(x+ ' to '+ path[y+1]+ cost + ' km')

def main():
	filename = sys.argv[1]
	start = sys.argv[2]
	goal = sys.argv[3]

	graph = {}
	graph = create_graph(filename)

	if start not in graph.keys():
		print('Improper start node')
		sys.exit()
	if goal not in graph.keys():
		print('Improper goal node')
		sys.exit()

	path = []
	path = ucs(graph, start, goal)

	if path:
		display_path(graph, path)

if __name__ == '__main__':
	main()

'''

import sys
from queue import PriorityQueue
from heapq import heappush, heappop
'''
def main():
	filename = sys.argv[1]
	start = sys.argv[2]
	goal = sys.argv[3]
	
	graph = {}
	graph = create_graph(filename)
	
	if start not in graph.keys():
		print('Invalid input')
		sys.exit()
	if goal not in graph.keys():
		print('Invalid goal')
		sys.exit()

	path = []
	path = uniformed_cost_search(graph, start, goal)

	if path:
		display_path(graph, path)
'''
def create_graph(filename):
	graph = {}
	file = open(filename, 'r')
	
	for line in file:
		if 'END OF INPUT' in line:
			return graph
	
		nodeA, nodeB, d = line.split()
		graph.setdefault(nodeA, []).append((nodeB, d))
		graph.setdefault(nodeB, []).append((nodeA, d))

def uninformed_cost_search(graph, start, goal):
	visited = set()
	path = []
	queue = PriorityQueue()
	queue.put((0, [start]))

	while queue:
		if queue.empty():
			print('distance: infinity\nroute:\nnone')
			return
		cost, path = queue.get()
		node = path[len(path)-1]
	
		if node not in visited:
			visited.add(node)
			if node == goal:
				path.append(cost)
				return path
			
			for x in neighbors(graph, node):
				if x not in visited:
					total_cost = cost + int(get_cost(graph, node, x))
					temporary = path[:]
					temporary.append(x)
					queue.put((total_cost, temporary))

def neighbors(graph, node):
	elements = graph[node]
	return [x[0] for x in elements]

def get_cost(graph, from_node, to_node):
	position = [x[0] for x in graph[from_node]].index(to_node)
	return graph[from_node][position][1]

def display_path(graph, path):
	distance = path[-1]
	print('distance: %s'%(distance))
	print('route: ')

	for x in path[:-2]:
		y = path.index(x)
		position = [z[0] for z in graph[x]].index(path[y+1])
		cost = graph[x][position][1]
		print(x + ' to ' + path[y+1] + ',' + cost + ' km')

def main():
        filename = sys.argv[1]
        start = sys.argv[2]
        goal = sys.argv[3]
        
        graph = {}
        graph = create_graph(filename)
        
        if start not in graph.keys():
                print('No route can be found')
                sys.exit()
        if goal not in graph.keys():
                print('No route can be found')
                sys.exit()

        path = []
        path = uninformed_cost_search(graph, start, goal)

        if path:
                display_path(graph, path)




if __name__ == '__main__':
	main()

		
