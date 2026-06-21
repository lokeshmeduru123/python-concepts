# this is all about list use cases 
# list is an hetrogeneous type it means it can have multiple datatypes in it 
fruits = ["apple", "banana","pineapple","orange", 1, 2, 3, True]

print(fruits[0]) # prints first variable 

print(fruits[-1]) # prints last variable 

print(fruits[-2]) # prints n-1 variable 

print(fruits[0:2]) # prints frisr 2 variables 



print(dir(fruits)) #display all the valid attributes, properties, and methods belonging to a specific object. 

"""
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

# append: adding elements to a list at the end 

fruits.append(5) # in place operation, basiclly adding the number at the end without displaying/stroting in variable 

print(fruits)


# append vs extend
# append operation adds the entire element as -1
# extend operation itrates over the itratable and appends the element to the original list 
fruits.append(["goa","straberry","avacado"])

print(fruits)


fruits.extend(["goa","straberry","avacado"])

print(fruits)


vegetables = ["tomoto","onion","carrot","beetrote"]

print(vegetables.count("tomoto")) # count helps to print the num of variables in it 

print(vegetables.index("carrot")) # it wwill shows the indeex of the variable 


# converting the sting to individual list, basically converting one dat type to another data type 
sports_string = "i love playing cricket"
list_string = list(sports_string)
print(list_string)

# join 
join_str = "".join(list(sports_string))
print(join_str)


# sort, its an in place operation

trial_numbers = [6, 2, 3, 4, 5]
trial_numbers.sort()
print(trial_numbers)
# sorted  returns the sorted list 
trial_numberts_sorted = sorted(trial_numbers)
print(trial_numbers, trial_numberts_sorted)
