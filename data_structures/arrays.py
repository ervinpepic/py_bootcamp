# in most cases python use lists instead of arrays
# but if you need to deal with large datasets you need to use arrays
# to start working with array
# you have to import array class from array module like this

from array import array

numbers = array("i", [1, 2, 3, 4])
numbers.append(4)
numbers.insert(0, 20)
print(numbers)

#the typecode in the initialization of the array, specifies the
# type of data that array must use. 
#If we try to put floating point number we will encounter an error

numbers[1] = 1.2