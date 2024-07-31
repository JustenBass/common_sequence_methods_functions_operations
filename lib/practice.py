##common sequence operations
my_list = [1, 2, 3, 4 , 5]

#x in my_list returns True if x is equal to at least one element of my_list.
print(2 in my_list)

#my_list + my_list2 returns a single sequence of the elements of my_list followed by the elements of my_list2.
print(my_list + my_list)

#my_list * n returns a single sequence of my_list repeated n times.
print(my_list * 4)

#my_list[i]returns the ith element of my_list (starting at 0).
print(my_list[0])

#my_list[i:j] returns a slice of my_list from index i up to (but not including!) index j.
print(my_list[1:3])

#my_list[i:j:k] returns a slice of my_list from i to j with steps of k in between
print(my_list[0:4:2])

#len(my_list) returns the number of elements in my_list
print(len(my_list))

#min(my_list) and max(my_list) return the minimum and maximum values in my_list, respectively. >
# NOTE: this requires the elements of my_list to be of the same data type, either str or numerical.
print(min(my_list))
print(max(my_list))

#min(my_list) and max(my_list) on list where we use the key attribute to tell our max and min functions to find the string with the min/max
#characters with the len function
names = ['Kate', 'Q', 'Tasha', 'Elizabeth', 'Wonder']
print(max(names, key = len))
print(min(names, key = len))

#names.index(x) returns the index of the first x in names.
print(names.index('Kate'))

#names.count(x) returns the number of instances of x in names
print(names.count('Kate'))

#########################################################################

##Lists

#.sort() rearranges the elements of the list so that they are in order
nums = [7,1,5,4,3,2]
fruits = ['Orange', 'Apple', 'Cranberry', 'Beats', 'Bananas']

nums.sort()
print(nums)

fruits.sort()
print(fruits)

#.sort() with a list of sentances including the key attribute to tell our sort function to sort with the len function
strings = ['This message is so long', 'How are you', 'ok']


strings.sort(key = len)
print(strings)
strings.sort(key = len, reverse = True)
print(strings)


#.sort() a list of tuples we can define a function for the list to sort by any chosen key/index in the tuple
my_list_of_tuples = [('John', 4), ('Jason', 2), ('Jared', 3)]

def sort_tuple(tuple_value):
    return tuple_value[0]

my_list_of_tuples.sort(key = sort_tuple)
print(my_list_of_tuples)


my_list_of_tuples_2 = [('Kate', 4, 5, 5), ('Mickie', 6, 7, 8), ('Carmen', 1, 3, 1)]

def sort_tuple_2(tuple_value):
    return tuple_value[3]

my_list_of_tuples_2.sort(key = sort_tuple_2)
print(my_list_of_tuples_2)

my_list_of_tuples_2.sort(key = sort_tuple_2, reverse = True)
print(my_list_of_tuples_2)


#sorted() function should only be used when you want to preserve your originial list, but you need a sorted version for a sepertate task
my_list_2 = [3, 4, 2, 6, 5]

sorted_list = sorted(my_list_2)
print(my_list_2)
print(sorted_list)

##.sorted() with a list of sentances including the key attribute to tell our sort function to sort with the len function
strings_2 = ['You are a going to ace this!', 'Common', 'j']

sorted_list_2 = sorted(strings_2, key=len)
print(strings_2)
print(sorted_list_2)

sorted_list_2 = sorted(strings_2, key=len, reverse=True)
print(sorted_list_2)