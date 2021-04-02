import arrays


cir_array = arrays.Array(5)
first = 2
last = 4

# show code for append
last = ( last + 1) % len(cir_array)
# how to know array is full
if last == first:
    raise IndexError("Array is full")