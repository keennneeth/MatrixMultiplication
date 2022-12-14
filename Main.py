import random
from itertools import chain



randomlist = [random.randrange(10) for i in range (30)]
chunked_list = list()                       #Creating a random number from 0-10, 30 times
chunk_size = 6

for i in range(0, len(randomlist), chunk_size):
    chunked_list.append(randomlist[i:i+chunk_size])          #putting it into groups of 6

newlist = chunked_list

print ("(a) create a 5 by 6 matrix, A, whose entries are random integers between 0 and 10.")
print("_"*75)
print("\nMATRIX 1")
print("_"*75)
print("\n(a) Create a 5x6 matrix")



A = newlist
print(*A, sep = "\n")

print("\n(b) Find the transpose of, B, of this matrix")
B = list(map(list,zip(*chunked_list)))                  #zip function makes it into the transpose
for row in B:
    print(row)

result = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]

print("\n(c)find the product AB.")
for i in range(len(A)):
     for j in range(len(B[0])):                 #multiplying A*B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
for r in result:
    print(r)



result1 = [[0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0]]
print("\n(d)find the product BA.")
for i in range(len(B)):
     for j in range(len(A[0])):             #multiplying B*A
        for k in range(len(A)):
            result1[i][j] += B[i][k] * A[k][j]
for r in result1:
    print(r)

print("_"*75)
print("\n(e) repeat the sequence of steps (a) through (d) two more times")
print("_"*75)

print("\nMATRIX 2")
print("_"*75)
print("\n")
print("\n(a) Create a 5x6 matrix")

randomlist1 = [random.randrange(10) for i in range (30)]
chunked_list = list()
chunk_size = 6

for i in range(0, len(randomlist), chunk_size):
    chunked_list.append(randomlist1[i:i+chunk_size])
newlist1 = chunked_list
A1 = newlist1
print(*A1, sep = "\n")

print("\n(b) Find the transpose of, B, of this matrix")
B1 = list(map(list,zip(*chunked_list)))
for row in B1:
    print(row)

print("\n(c)find the product AB.")
for i in range(len(A1)):
     for j in range(len(B1[0])):
        for k in range(len(B1)):
            result[i][j] += A1[i][k] * B1[k][j]
for r in result:
    print(r)

print("\n(d)find the product BA.")
for i in range(len(B1)):
     for j in range(len(A1[0])):
        for k in range(len(A1)):
            result1[i][j] += B1[i][k] * A1[k][j]
for r in result1:
    print(r)


#MATRIX 3
print("_"*75)
print("\nMATRIX 3")
print("_"*75)
print("\n(a) Create a 5x6 matrix")

randomlist2 = [random.randrange(10) for i in range (30)]
chunked_list = list()
chunk_size = 6

for i in range(0, len(randomlist), chunk_size):
    chunked_list.append(randomlist2[i:i+chunk_size])
newlist2 = chunked_list
A2 = newlist2
print(*A2, sep = "\n")

print("\n(b) Find the transpose of, B, of this matrix")
B2 = list(map(list,zip(*chunked_list)))
for row in B2:
    print(row)

print("\n(c)find the product AB.")
for i in range(len(A2)):
     for j in range(len(B2[0])):
        for k in range(len(B2)):
            result[i][j] += A2[i][k] * B2[k][j]
for r in result:
    print(r)

print("\n(d)find the product BA.")
for i in range(len(B2)):
     for j in range(len(A2[0])):
        for k in range(len(A2)):
            result1[i][j] += B2[i][k] * A2[k][j]
for r in result1:
    print(r)

print("_"*75)

negrandomlist = [-1*random.randrange(10) for i in range (30)]
chunked_list = list()
chunk_size = 6

for i in range(0, len(negrandomlist), chunk_size):
    chunked_list.append(negrandomlist[i:i+chunk_size])

negnewlist = chunked_list

print("\n(g) Create a negative 5x6 matrix")

negA = negnewlist
print(*negA, sep = "\n")
print("\n(REFERENCE (BELOW IS MATRIX A)")
print(*A, sep = "\n")

print("\n(h) Computer A+C")


resultAC = [[A[i][j] + negA[i][j]  for j in range(len(A[0]))] for i in range(len(A))]

for r in resultAC:
   print(r)

print("\n(i) Find the sum of all even numbers in A+C\n")
print("Even numbers in A + C below")
print("_"*75)
allrows = list(chain(resultAC[0], resultAC[1], resultAC[2], resultAC[3], resultAC[4]))          #combining the lists by using chain


mylist = []
for num1 in allrows:
    if num1 % 2 == 0:
        mylist.append(num1)
print(mylist)
total = sum(mylist)                     #making the even numbers into a list
print("_"*75)


print("\nTotal sum (even): ",total)
print("\n")

print("(j) Computer A-C")
print("\nREFERENCE (BELOW IS MATRIX A)")
print(*A, sep = "\n")
print("\nBELOW IS MATRIX C")
print(*negA, sep = "\n")
print("\nBELOW IS A-C")

subresultAC = [[A[i][j] - negA[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
for r in subresultAC:                                                                       #subtracting A-C
   print(r)


print("\nBelow are odd numbers in A-C")
allrows1 = list(chain(subresultAC[0], subresultAC[1], subresultAC[2], subresultAC[3], subresultAC[4]))

print("_"*75)

mylist = []
for num2 in allrows1:
    if num2 % 2 == 1:           #putting odd numbers into a list
        mylist.append(num2)
print(mylist)
total = sum(mylist)
print("_"*75)

print("\n(k)Find the sum of all odd numbers in A-C")
print("\nTotal sum (odd): ",total)
print("\n")
