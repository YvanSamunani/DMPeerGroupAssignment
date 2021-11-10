
# List one

# creating an empty list_one
X = []
# number of elements as input
n = int(input("Enter number of elements for the first list : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    X.append(ele)  # adding the element

print(X)
# creating an empty list_two
Y = []

# number of elements as input
n = int(input("Enter number of elements for the second list: "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    Y.append(ele)  # adding the element
print(Y)
# Checking whether ∀x ∈ X, ∃y ∈ Y such that y | x
count = 0
for i in X:
    for j in Y:
        if j%i == 0:
            count +=1

if count > 1:
    print("True")
else:
    print("false")
