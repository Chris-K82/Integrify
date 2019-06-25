# Numpy Tutorial Peer Review

Authors: Peter Le and Chris Kraus

Location: Integrify, Helsinki, FI

Description: This is a brief peer review of another team's assignment execution.

line 70. "int_array = np.arange(5) # an array of 5 index is created"
    - this is incorrect. "np.arange(5)" creates an array of len == 5 '[0, 1, 2, 3, 4]'
    as you can see from this example, the highest index is "4".

line 85. "print(array2.ndim)  # print the no. of dimension"
    - this is incorrect, this statement returns the number of rows

line 170 - 173. When the assignment statement "arr_flt[0] = 33" is compiled, it changes
    the values in both the original array and the new array which is not a new array but
    rather a copy of the reference to the original array. Essentially, you can change the
    values by either calling arr[some_index] = some_val or by arr_flt[some_index] = some_val.
    This phenomena occurs because the original array wasn't copied, only its reference.

line 238. "arry = np.arange(10, dtype = float).reshape((2, 5)) #matrix of 2 rows 5 colomns having float data type and 10 index"
    - This is again, incorrect. This statement creates an array which is actually a 2 x 5 matrix in range(10). Because
    python is a zero-index based array system, the highest index is 9. The new array has len == 10.

line 238 - 256. Again, the point of this exercise was to realize that this method made an actual copy of the values
    stored in the original array which means that when the assignment statement on line 253 occurs, only the value
    in the new array is changed.

line 433. "print(number_1.std())             # standard division of array"
    - This comment is incorrect. ".std" computes standard deviation.

line 528 - 534. This explanation of the diagram is incorrect. When numpy recognizes a dimensional mismatch, it will
    - still execute the operation so long as one of the dimensions of the smaller matrix can match one of the dimensions of the
    larger matrix.
