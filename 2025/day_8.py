"""My solution to day 8 of advent of code 2025"""
from math import sqrt

def get_puzzle_input() -> list[list]:
    """Gets the puzzle input"""

    with open('input_day_8.txt', 'r') as f:
        return [[int(x) for x in line.replace('\n', '').split(',')] for line in f.readlines()]

def process_part_one(data: list[list]) -> int:
    """Returns my answer to part one"""
    
    pairings = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            distance = sqrt(sum([(x-y)**2 for x, y in zip(data[i], data[j])]))
            pairings.append((distance, i, j))
  
    pairings.sort()
    
    parent = list(range(len(data)))
    
    for connection in range(1000):
        _, box_a, box_b = pairings[connection]
        root_a, root_b = box_a, box_b

        while parent[root_a] != root_a:
            parent[root_a] = parent[parent[root_a]]
            root_a = parent[root_a]

        while parent[root_b] != root_b:
            parent[root_b] = parent[parent[root_b]]
            root_b = parent[root_b]

        if root_a != root_b:
            parent[root_a] = root_b
    
    circuits = {}
    for i in range(len(data)):
        root = i
        while parent[root] != root:
            root = parent[root]
            
        circuits[root] = circuits.get(root, 0) + 1
    
    sizes = sorted(circuits.values(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

def process_part_two(data: list[list]) -> int:
    """Returns my answer to part two"""
    
    pairings = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            distance = sqrt(sum([(x-y)**2 for x, y in zip(data[i], data[j])]))
            pairings.append((distance, i, j))
  
    pairings.sort()
    
    parent = list(range(len(data)))
    
    for connection in range(len(pairings)):
        _, box_a, box_b = pairings[connection]
        root_a, root_b = box_a, box_b
        
        while parent[root_a] != root_a:
            parent[root_a] = parent[parent[root_a]]
            root_a = parent[root_a]
        
        while parent[root_b] != root_b:
            parent[root_b] = parent[parent[root_b]]
            root_b = parent[root_b]
        
        if root_a != root_b:
            parent[root_a] = root_b
            
            circuits = set()
            for i in range(len(data)):
                root = i
                while parent[root] != root:
                    root = parent[root]
                circuits.add(root)
            
            if len(circuits) == 1:
                return data[box_a][0] * data[box_b][0]
    
    return 0

if __name__ == '__main__':
    puzzle_input = get_puzzle_input()
    print(f'Part one: {process_part_one(puzzle_input)}')
    print(f'Part two: {process_part_two(puzzle_input)}')