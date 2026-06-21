# string starts with 0 index 
# types of functions used in this python script
# len function
#
sample_string = "this is an python programe"

print(sample_string)

first_string = sample_string[0]
print(first_string)


last_string = sample_string[-1]
print(last_string)

length_of_string = len(sample_string)   # len function
print(length_of_string)

words = sample_string.split(sep= " ")
print(words)
print(type(words))
#print(dir(words))


"""
this is the comment lines in pytho
multiples lines comments we can use this mentiod
"""
print(sample_string.strip())


# how to extract first 2 character in new string 
# To do this we use ':'
# ussage : start:end:step, all three are optonal
# important: end index is not included , hence used end+1

new_string = "welocme to python class"

first_two = new_string[0:10] # here the step size value is 1 (defalut)
print(first_two)

alternate_char = new_string[::2] # start with 0 end: len(str)
print(alternate_char)

reverse_string = new_string[::-1] # here step size is -1
print(reverse_string)

reverse_string = new_string[::-2] # here step size is -2
print("the reverse string is :", reverse_string)