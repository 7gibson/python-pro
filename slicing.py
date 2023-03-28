my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing from index 2 to index 5 (exclusive)
slice1 = my_list[2:5]  

print(slice1)
print("\n")
# Slicing from index 0 to index 7 (exclusive), skipping every second element
slice2 = my_list[0:7:2]  

print(slice2)
print("\n")
# Slicing from index 5 to the end of the list
slice3 = my_list[5:]

print(slice3)
print("\n")
# Slicing from the beginning of the list to index 3 (exclusive)
slice4 = my_list[:3]  

print(slice4)

print("\n")
players=['rashford','bruno','shaw','verane','bissaka','sancho']

best_scorers=players[0:5:2]
averange_players=players[2:]

print(averange_players)
print("\n")
print(best_scorers)
print("\n")
my_list = [3, 7, 1, 9, 2, 6]
my_list.sort()  # Sort the list in ascending order
print(my_list)  
print("\n")
my_list.sort(reverse=True)  # Sort the list in descending order
print(my_list)  
print("\n")
my_list = [1, 2, 3]
my_list[1] = 4
print(my_list)  

print("\n")

my_list1 = [1, 2, 3]
my_list2 = my_list1
my_list2[1] = 4
print(my_list1)

print("\n")

print(my_list2) #my_list1 and my_list2 are the same
print("\n")
#to avoid my_list1 and my_list2 being the same we use slicing notation

my_list1 = [1, 2, 3]
my_list2 = my_list1[:]
my_list2[1] = 4
print(my_list1)  

print("\n")

print(my_list2)  




