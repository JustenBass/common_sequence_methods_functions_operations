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

#min(my_list) and max(my_list) on strings have to include the argument key and equal to length
names = ['Kate', 'Q', 'Tasha', 'Elizabeth', 'Wonder']
print(max(names, key = len))
print(min(names, key = len))

#names.index(x) returns the index of the first x in names.
print(names.index('Kate'))

#names.count(x) returns the number of instances of x in names
print(names.count('Kate'))