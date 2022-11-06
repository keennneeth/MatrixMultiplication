import random


randomlist = [random.randrange(10) for i in range (30)]
chunked_list = list()
chunk_size = 6

for i in range(0, len(randomlist), chunk_size):
    chunked_list.append(randomlist[i:i+chunk_size])

newlist = '\n'.join(map(str, chunked_list))

print ("(a) create a 5 by 6 matrix, A, whose entries are random integers between 0 and 10.")
A = newlist
print(A)



print("\n(b) Find the transpose of, B, of this matrix")
B = map(list,zip(*chunked_list))
for row in B:
    print(row)


result = [[0,0,0],
           [0,0,0],
           [0,0,0]]


print("\n(c)find the product AB.")





# print("\n(d) find the product BA.")

# for i in range (len(A)):
#     for j in range (len(B)):
#         result[i][j] = B[i][j] * A[i][j]
# for r in result:
#     print(r)
