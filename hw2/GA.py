import numpy as np
size = 100

def attack(arr):
    '''
    return a list which contains the number of attacked queens
    '''
    score = []
    for i in range(8):
        tmp = 0
        for j in range(8):
            if(i == j):
                continue
            if(arr[i] == arr[j]):
                tmp += 1
            elif(abs((arr[j]-arr[i])/(j-i)) == 1):
                tmp += 1
        score.append(tmp)
    return score

def sort_rule(element):
    return sum(attack(element))

def genetic():
    '''
    implement genetic algorithm and return 1 if success
    '''
    population = []
    pool = []
    for i in range(size * 10):    # generate 100 randomly
        arr = []
        for j in range(8):
            arr.append(np.random.randint(8))
        pool.append(arr)
    pool.sort(key=sort_rule)
    pool = pool[:size]
    population.append(pool)
    for i in pool:
        if(sum(attack(i)) == 0):
            print(i, end=' ')
            print("search cost: %d" % len(population))
            return 1
    
    while(len(population) < 15):
        pool = []
        for i in range(size * 10):
            a, b = np.random.randint(size), np.random.randint(size)
            cut = np.random.randint(8)
            new = population[-1][a][:cut] + population[-1][b][cut:]    # -1 represents last one
            pool.append(new)
        pool.sort(key=sort_rule)
        pool = pool[:size]
        population.append(pool)
        for i in pool:
            if(sum(attack(i)) == 0):
                print(i, end=' ')
                print("search cost: %d" % len(population))
                return 1
    return 0

def main():
	count = 0
	for i in range(100):
		if(genetic()):
			count += 1
	print("percentage of solved problems: %d%%" % count)

if __name__ == "__main__":
    main()