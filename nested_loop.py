for i in range(2):
    print("i = ",i)
    for j in range (3):
        print("j = ",j)
    print()

for i in range(2):
    # print("i = ",i)
    for j in range (3):
        print("{} {}".format(i, j) ,end="")
    print()

for i in range(3):
    # print("i = ",i)
    for j in range (3):
        print("a".format(i,j) ,end="")
    print()

for i in range(3):
    # print("i = ",i)
    print()

list_data = [[1,2],[3,4]]
for i in list_data:
    for j in i:
        print(j*5)
