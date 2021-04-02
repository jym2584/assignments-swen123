import arrays

array_a = arrays.Array(10)
print(array_a)
print(array_a[3])

length = len(array_a)
for index in range(length):
    array_a[index] = index * 5
print("Number of arrays:",index+1)

counter = 0
while counter < length:
    array_a[counter] = counter * 2
    counter+= 1
    

array_b = arrays.Array(5, "abc")