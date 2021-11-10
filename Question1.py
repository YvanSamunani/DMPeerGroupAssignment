a_list = input("Please enter a list of numbers separated by space: ").split()
a_set = set(a_list)
if len(a_list) == len(a_set):
    print(True)
else:
    print("False, the set should be: ", a_set)
