"""
This entire section which is not defined as a function simply initializes both lists.
It adds values to both lists and sets the stage ready for what follows
"""

listOne = []
listTwo = []
listONeSize = int(input("Enter size of list one: "))
listTwoSize = int(input("Enter size of list two: "))
print("Appending list one...")
for i in range(listONeSize):
  inputValue = int(input(f"Enter value {i+1}:"))
  listOne.append(inputValue)
print("Appending list two...")
for i in range(listTwoSize):
  inputValue = int(input(f"Enter value {i+1}:"))
  listTwo.append(inputValue)
# End of initialization of start of list


def BinA():
  #This function checks if set B is a subset of set A
  if(all(x in listOne for x in listTwo)):
    # iterates through all values in B and returns the appropriate value depending on whether or not all the values are in A
    print("B is a subset of A")
  else:
    print( "B is not a subset of A!")




def AminusB():
  #Simply returns the result of subtracting A from B
  newList = [listOne[i]-listTwo[i] for i in range(len(listOne))]
  print("A - B is: ", newList)

def AtimesB():
  #returns the product of multiplying A by B
  newList = [listOne[i]*listTwo[i] for i in range(len(listOne))]
  print("A * B is: ", newList)


def allSetsinAandB():
  #returns a list which has all values of both set that satisfy the indicated condition!
  newList = []
  for i in listOne:
    for j in  listTwo:
      if i == j:
        pass
      else:
        newList.append((i, j))
  print("Results: ", newList)

BinA()
AminusB()
AtimesB()
allSetsinAandB()
