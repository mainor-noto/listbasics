#SECTION #1
color_list = ["red", "green", "blue", "yellow"]
#TODO: use notes to print first element
print(color_list[0])
#TODO: use notes to print last element
print(color_list[3])

#SECTION #2
# TODO: create num_list
num_list = [4, 6, 4, 2, 9, 4,1]
#TODO: use append to add 5 to num_list and print
num_list.append(5)
print(num_list)
#TODO: use remove to remove the
# first occurence of 4 and then print
num_list.remove(4)
print(num_list)
#TODO: use count to count how many times 4 appears in num_list
print(num_list.count(4))
#TODO: use the index method to find where the 9 is and print the index
print(num_list.index(9))
#SECTION #3
#TODO: first part of section 3
fruit_list = ["apple", "banana", "cherry"]
#TODO: use index operator [] to alter index 1 to orange.  Use notes
print(fruit_list.index('banana'))
fruit_list[1] = "orange"
print(fruit_list)
fruit_list.pop(2)
print(fruit_list)