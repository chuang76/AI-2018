import numpy as np
import copy
from math import factorial
import sys

def read_coord():
    '''
    read file and create coordinates
    '''
    lines = []
    with open('input.txt', 'r') as fp:
        for line in fp.readlines():
            line = line.strip('\n')
            lines.append(line)

    lines[0] = lines[0].split(" ")
    lines[1] = lines[1].split(" ")
    x = []
    y = []
    for i in lines[0]:
        x.append(float(i))
    for i in lines[1]:
        y.append(float(i))
        
    coords = []
    for i in range(len(x)):
        coords.append((x[i], y[i]))
    return coords

def cartesian_matrix(coords):
    '''
    create a distance matrix for the city coords
    '''
    matrix = {}
    for i, (x1, y1) in enumerate(coords):
        for j, (x2, y2) in enumerate(coords):
            dx, dy = x1-x2, y1-y2
            r = np.sqrt(dx*dx + dy*dy)
            matrix[i, j] = r
    return matrix

def tour_length(matrix, tour):      # matrix 存原本的 , tour 是新交換的
    total = 0
    for i in range(len(tour)):      # len(coords) is the number of cities
        j = (i + 1) % len(tour)     # mod 是為了讓它繞回來
        total += matrix[tour[i], tour[j]]
    return total

def path(coords, tour):
    print("\nPath:")
    for i in tour:
        print(coords[i][0], end=' ')
    print('\n', end='')
    for i in tour:
        print(coords[i][1], end=' ')

def all_pairs(size):
    '''
    create all possible pairs
    '''
    pairs = []
    arr = np.arange(size)
    for i in arr:
        for j in arr:
            if i < j:
                pairs.append([i, j])
    return pairs    

def select(size, selected):      # keep unique
    '''
    select one of all pairs to generate new list
    '''
    pairs = all_pairs(size)
    count = int (factorial(size) / (factorial(2) * factorial(size-2)))  
    s = np.random.randint(0, count)     # random select
    
    while(selected[s][1] == 1):    
        s = np.random.randint(0, count)
   
    selected[s][1] = 1
    p = pairs[s]
    return (p, selected)
    
def generate(best, size, selected):   
    new = copy.copy(best)
    p, selected = select(size, selected)
    new[p[0]], new[p[1]] = new[p[1]], new[p[0]]  # swap
    return (p, new, selected)

def hill_climb(coords, matrix, init_tour, size):
    best = init_tour
    path(coords, best)
    print("\n\nLength = %f" % tour_length(matrix, best))
    max_step = int (factorial(size) / (factorial(2) * factorial(size-2)))    # 15
    selected = list([i,0] for i in range(max_step))

    while(1):
        p, new, selected = generate(best, size, selected)
        
        if(tour_length(matrix, new) < tour_length(matrix, best)):
            print("\nSwap %d and %d" % (p[0], p[1]))
            path(coords, new)
            print("\n\nLength = %f" % tour_length(matrix, new))
            best = new
            
        index = 0
        for i in range(len(selected)):
            if(selected[i][1] == 0):
                index = 1
        if(index == 0):
            print("\nEnd of hill climbing")
            break

def main():
    coords = read_coord()
    size = len(coords)
    matrix = cartesian_matrix(coords)
    init_tour = np.arange(size)
    hill_climb(coords, matrix, init_tour, size)

if __name__ == "__main__":
    main()