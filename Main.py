import random


randomlist = [random.randrange(10) for i in range (30)]
chunked_list = list()
chunk_size = 6

for i in range(0, len(randomlist), chunk_size):
    chunked_list.append(randomlist[i:i+chunk_size])

newlist = chunked_list

print ("(a) create a 5 by 6 matrix, A, whose entries are random integers between 0 and 10.")
A = newlist
print(*A, sep = "\n")



print("\n(b) Find the transpose of, B, of this matrix")
B = list(map(list,zip(*chunked_list)))
for row in B:
    print(row)




result = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]


print("\n(c)find the product AB.")

for i in range(len(A)):
 
    # iterating by column by B
    for j in range(len(B[0])):
 
        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)





# print("\n(d) find the product BA.")

# for i in range (len(A)):
#     for j in range (len(B)):
#         result[i][j] = B[i][j] * A[i][j]
# for r in result:
#     print(r)
