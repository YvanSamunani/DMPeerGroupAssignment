# Assigning set A and B elements
A = {1,2,3,4,5}
B = {1,2,3}
# Question a) the truth value of B ⊆ A
# checks whether B is a subset of A or not and prints its truth value.
print(B.issubset(A))

# b) the set A − B
# Python code to get the difference between two sets using difference() between set A and set B
print(A.difference(B))

# c) the set A × B
# A×B = {(x, y) | x ∈ A and y ∈ B};  defines all pairs (x, y) such that x belongs to A and y
# belongs to B.
print({(x,y) for x in A for y in B})