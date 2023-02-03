import math
import time
import random

def example(func_list):
	n = len(func_list)

	arr2 = [0,0,0,0,0]

	for i in range(0,n):

		if func_list[i] == 0:

			for t1 in range(i,n):
				p1 = math.sqrt(t1)
				x1 = n + 1

				while x1 >= 1:
					x1 = x1 // 2
					arr2[i%5] = arr2[i%5] + 1

		elif func_list[i] == 1:
			for t2 in range(1,n+1):
				for p2 in range(1,n+1):
					x2 = n+1

					while x2>0:
						x2 = x2 //2
						arr2[i%5] = arr2[i%5] + 1

		elif func_list[i] == 2:
			for t3 in range(1, n+1):
				x3 = t3 + 1
				ran = t3**2 -1
				for p3 in range(0,ran):
					arr2[i%5] = arr2[i%5] + 1

	return arr2


def average_case(input_size):
	
	arr = [random.randint(0,2) for i in range(0,input_size)]
	return arr

def best_case(input_size):
	return [0]*input_size

def worst_case(input_size):
	return [2]*input_size

'''
Case: xxx Size:yyy Elapsed Time: zzz where, xxx denotes “best”, “worst” or “average”, yyy
denotes the data size, and zzz denotes the time 
s n {1, 5, 10, 25, 50, 75, 100, 150, 200, 250}
'''

best_case1 = best_case(1)
best_case5 = best_case(5)
best_case10 = best_case(10)
best_case25 = best_case(25)
best_case50 = best_case(50)
best_case75 = best_case(75)
best_case100 = best_case(100)
best_case150 = best_case(150)
best_case200 = best_case(200)
best_case250 = best_case(250)

worst_case1 = worst_case(1)
worst_case5 = worst_case(5)
worst_case10 = worst_case(10)
worst_case25 = worst_case(25)
worst_case50 = worst_case(50)
worst_case75 = worst_case(75)
worst_case100 = worst_case(100)
worst_case150 = worst_case(150)
worst_case200 = worst_case(200)
worst_case250 = worst_case(250)



start = time.time()
example(best_case1)
end = time.time()
print("Case: best Size: 1 Elapsed Time: %f" % (end-start))

start = time.time()
example(worst_case1)
end = time.time()
print("Case: worst Size: 1 Elapsed Time: %f" % (end-start))

value = 0
for i in range(0,3):
	average = []
	average = average_case(1)
	start = time.time()
	example(average)
	end = time.time()
	value += end-start

print("Case: average Size: 1 Elapsed Time: %f" % (value/3))

start = time.time()
example(best_case5)
end = time.time()
print("Case: best Size: 5 Elapsed Time: %f" % (end-start))

start = time.time()
example(worst_case5)
end = time.time()
print("Case: worst Size: 5 Elapsed Time: %f" % (end-start))

value = 0
for i in range(0,3):
	average = average_case(5)
	start = time.time()
	example(average)
	end = time.time()
	value += end-start

print("Case: average Size: 5 Elapsed Time: %f" % (value/3))

start = time.time()
example(best_case10)
end = time.time()
print("Case: best Size: 10 Elapsed Time: %f" % (end-start))

start = time.time()
example(worst_case10)
end = time.time()
print("Case: worst Size: 10 Elapsed Time: %f" % (end-start))


value = 0
for i in range(0,3):
	average = average_case(10)
	start = time.time()
	example(average)
	end = time.time()
	value += end-start

print("Case: average Size: 10 Elapsed Time: %f" % (value/3))

start = time.time()
example(best_case25)
end = time.time()
print("Case: best Size: 25 Elapsed Time: %f" % (end-start))

start = time.time()
example(worst_case25)
end = time.time()
print("Case: worst Size: 25 Elapsed Time: %f" % (end-start))

value = 0
for i in range(0,3):
	average = average_case(25)
	start = time.time()
	example(average)
	end = time.time()
	value += end-start

print("Case: average Size: 25 Elapsed Time: %f" % (value/3))

start = time.time()
example(best_case50)
end = time.time()
print("Case: best Size: 50 Elapsed Time: %f" % (end-start))

start = time.time()
example(worst_case50)
end = time.time()
print("Case: worst Size: 50 Elapsed Time: %f" % (end-start))

value = 0
for i in range(0,3):
	average = average_case(50)
	start = time.time()
	example(average)
	end = time.time()
	value += end-start

print("Case: average Size: 50 Elapsed Time: %f" % (value/3))

start = time.time()
example(best_case75)
end = time.time()
print("Case: best Size: 75 Elapsed Time: %f" % (end-start))

start = time.time()
example(worst_case75)
end = time.time()
print("Case: worst Size: 75 Elapsed Time: %f" % (end-start))


value = 0
for i in range(0,3):
	average = average_case(75)
	start = time.time()
	example(average)
	end = time.time()
	value += end-start

print("Case: average Size: 75 Elapsed Time: %f" % (value/3))

start = time.time()
example(best_case100)
end = time.time()
print("Case: best Size: 100 Elapsed Time: %f" % (end-start))

start = time.time()
example(worst_case100)
end = time.time()
print("Case: worst Size: 100 Elapsed Time: %f" % (end-start))

value = 0
for i in range(0,3):
	average = average_case(100)
	start = time.time()
	example(average)
	end = time.time()
	value += end-start

print("Case: average Size: 100 Elapsed Time: %f" % (value/3))

start = time.time()
example(best_case150)
end = time.time()
print("Case: best Size: 150 Elapsed Time: %f" % (end-start))

start = time.time()
example(worst_case150)
end = time.time()
print("Case: worst Size: 150 Elapsed Time: %f" % (end-start))

value = 0
for i in range(0,3):
	average = average_case(150)
	start = time.time()
	example(average)
	end = time.time()
	value += end-start

print("Case: average Size: 150 Elapsed Time: %f" % (value/3))

start = time.time()
example(best_case200)
end = time.time()
print("Case: best Size: 200 Elapsed Time: %f" % (end-start))

start = time.time()
example(worst_case200)
end = time.time()
print("Case: worst Size: 200 Elapsed Time: %f" % (end-start))

value = 0
for i in range(0,3):
	average = average_case(200)
	start = time.time()
	example(average)
	end = time.time()
	value += end-start

print("Case: average Size: 200 Elapsed Time: %f" % (value/3))



start = time.time()
example(best_case250)
end = time.time()
print("Case: best Size: 250 Elapsed Time: %f" % (end-start))

start = time.time()
example(worst_case250)
end = time.time()
print("Case: worst Size: 250 Elapsed Time: %f" % (end-start))

value = 0
for i in range(0,3):
	average = average_case(250)
	start = time.time()
	example(average)
	end = time.time()
	value += end-start

print("Case: average Size: 250 Elapsed Time: %f" % (value/3))



