#1.print sample spacea
import itertools
from itertools import product
n = 3
sample_space = list(product(['1','2','3','4','5','6'],repeat=n))
print(sample_space)
print(len(sample_space))

#2. Assuming all the outcomes equally likely. make a choice for outcome.
A = {two for two in sample_space if two[0] =='2'}
print(A)
print(len(A))

B = { two for two in sample_space if two.count('2') == 2 }
print(B)
print(len(B))

def prob(x):
    return len(x) / len(sample_space)

print(prob(A))
print(prob(B))