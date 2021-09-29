import Quick
from Bubble import bubble_sort
from Selection import selection_sort
from Insertion import insertion_sort
from Merge import merge_sort
from Quick import quick_sort
from timeit import timeit
import matplotlib.pyplot as plt
import random
vetor1000 = [random.randint(0, 1000) for _ in range(1000)]
vetor10000 = [random.randint(0, 1000) for _ in range(10000)]
vetor100000 = [random.randint(0, 1000) for _ in range(100000)]

print(vetor1000[:10])

print(vetor1000[::-1][:10])

# Verify it works
v1 = timeit('quick_sort(vetor1000)', 'from __main__ import quick_sort, vetor1000  ', number=100)
print(v1)
print(vetor1000[:10])
print(vetor1000[::-1][:10])
listX = ['Quick']
listY = [v1]
plt.bar(listX, listY)
plt.title('Comparativo de tempo vetor de tamanho 1000 aleatório')
plt.xlabel('Algoritmos')
plt.ylabel('Tempo (s)')
plt.show()

