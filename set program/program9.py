'''
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

print(A ^ B)
print(B ^ A)

print(A ^ A)
print(B ^ B)
'''

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print(A.symmetric_difference(C))
print(B.symmetric_difference(C))