a="Cisco Switch"
print("Find,Count,lower,upper,capitalize,startswith,endswith----------------------")
print(a.find("Sw"))
# 6 - It"s case sensitive
print(a.count("Sw"))
# 1
print(a.lower())
# cisco switch -similar for upper()
print("capitalize----------------------")
a="ding dong"
print(a.capitalize())
# Ding dong
# capitalizes first letter of string
a="Cisco Switch"
print(a.startswith("c"))
# False -as case sensitive,note w in with is not caps 
# similar for endswith()
print("Strip----------------------")
b="  Cisco Switch "
print("Remove white space in the begining and end.Strip>>",b.strip())
c="$$@Cisco Switch$#"
print("Striping all given characters>>",c.strip("$,#,@"))
# Cisco Switch
print("Replace----------------------")
d="$Cisco Switch"
print(d.replace(" ", "") and d.replace("$",""))
# Cisco Switch
print("Split----------------------")
a ="Cisco,Juniper,HP,Avaya,Nortel"#the delimiter is a comma
b=a.split(",")
print(a.split(","),"\n",a)
# ["Cisco", "Juniper", "HP", "Avaya", "Nortel"] returns an array after splitting
print("Join----------------------")
# join the string with a given character
print("_".join(a))


print("lstrip--------------------")
a="   Disco Cap"
print(a.lstrip())
# Disco Cap
# rstrip removes trailing whitespaces
print("swapcase--------------------")
a="Dinosaur ComingA?"
print(a.swapcase())
# dINOSAUR cOMINGa?
print("title--------------------")
a="hello man. how are you?"
print(a.title())
# Hello Man. How Are You?
a="A quick Brown Fox has mobile no #123341"
print(a.isalnum())#Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
print(a.isalpha())#Returns  true  if  string  has  at  least  1  character  and  all  characters  are  alphabetic  and  false otherwise.
print(a.isdigit())#Returns true if string contains only digits and false otherwise.
print(a.islower())#Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
print(a.isnumeric())#Returns true if a unicode string contains only numeric characters and false otherwise.
print(a.isspace())#Returns true if string contains only whitespace characters and false otherwise.
print(a.istitle())#Returns true if string is properly "titlecased" and false otherwise.
print(a.isupper())#Returns  true  if  string  has  at  least  one  cased  character  and  all  cased  characters  are  in uppercase and false otherwise.
#source: https://www.tutorialspoint.com/python3/python_strings.htm

print("Concatenate---------------")
#Strings -concatenating two or more strings
a ="Cisco"
b ="2691"
print(a +b)

print("in not in-----------------")
#Strings -checking if a character is or is not part of a string
a ="Cisco"
print("o"in a)
print("b"not in a)

print("Formatting with %s,%d,%f C like syntax-----------------")
print("Cisco model:%s" %("Hula10x"))

print("Cisco model: %s, %d WAN slots, IOS %f"%("2600XM",2,12.4))
print("Cisco model: %s, %d WAN slots, IOS %.f"%("2600XM",2,12.4))
print("Cisco model: %s, %d WAN slots, IOS %.1f"%("2600XM",2,12.4))
print("Cisco model: %s, %d WAN slots, IOS %.2f"%("2600XM",2,12.4))

print('Strings -formatting v2 with .format------------------')
print("Cisco model: {}, {} WAN slots, IOS {}".format("2600XM",2,12.4))
print("Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM",2,12.4))

print('Strings -formatting v3 (f-strings)-------------------')
model ="2950M"
wan =4
ios ="12.2"
print(f"Ciscomodel: {model}, {wan} WAN slots, IOS {ios}")

print('slicing-------------index starts at 0')
string1 ="O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
print('dingss>>>>>>>>',string1.index('O'))
print(string1[5:15])#slice  starting  at  index  5  up  to,  but  NOT  including,  index  15;  so  index  14 represents the last element in the slice

print(string1[5:])#slice starting at index 5 up to the end of the string

print(string1[:10])#slice starting at the beginning of the string up to, but NOT including, index 10

print(string1[:])#returns the entire string

print(string1[-1])#returns the last character in the string

print(string1[-2])#returns the second to last character in the string

print(string1[-9:-1])#extracts a certain substring using negative indexes

print('last Five',string1[-5:])#returns the last 5 characters in the string
# last Five rnet2
print('Excluding last Five ',string1[:-5])#returns the string minus its last 5 characters
# Excluding last Five  O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethe
print('Two steps>>',string1[::2])#adds a third element called step; skips every second character of the string
# Two steps>> OE 01089[6/]va1.1.5.,00:0 tent
print('Reverse string>>',string1[::-1])#returns string1's elements in reverse order
# Reverse string>> 2tenrehtE ,00:10:0 ,6.452.911.01 aiv ]5/061[ 9.8.011.01 2E O

print('Type and other functions------------')
num1=10
print(type(num1))

print(int(1.5))
print(float(1.5))
print(abs(-5))
print(max(1,5))
# similar to min
print(pow(3,2))
print(not(1==1))
print(bool(None))
print(bool('router'))

print('List-----------------------')
list1 =["Cisco","Juniper","Avaya","HP",10,10.5,-11]
list2 =[-11,2,12]
print(len(list1))
list1.pop(0)#removing an elementfrom the list by index
list1.remove("HP")#removing an element from the list by value
list1.insert(2,"Nortel")#inserting an element at a particular index
list1.extend(list2)#appending a list to another list
list1.index(-11)#returns the index of element -11
list1.count(10)#returns the number of times element 10 is in the list

list2 =[9,99,999,1,25,500]
list2.sort()#sorts the list elements in ascending order; modifies the list in place
print('after sorting',list2)
list2.reverse()#sorts the list elements in descending order; modifies the list in place
sorted(list2)#sorts the elements of a list in ascending order and creates a new list at the same time
sorted(list2,reverse =True)#sorts the elements of a list in descending order and creates a new list at the same time
list1 +list2 #concatenating two lists
list1 *3#repetition of a list
print('list slicing---------')
#'Lists -slicing  works  the  same  as  string  slicing,  but  with  list  elements  instead  of  string characters'
a_list=[1,2,3,4,6,67,57,87,45,99,64,678,577,874,454]
print(a_list[5:15])#slice  starting  at index  5  up  to,  but  NOT  including,  index  15;  so  index  14 represents the last element in the slice
# [67, 57, 87, 45, 99, 64, 678, 577, 874, 454]
print(a_list[5:])#slice starting at index 5 up to the end of the list
# [67, 57, 87, 45, 99, 64, 678, 577, 874, 454]
print(a_list[:10])#slice starting at the beginning of the list up to, but NOT including, index 10
# [1,2,3,4,6,67,57,87,45,99]
print(a_list[:])#returns the entire list
# [1, 2, 3, 4, 6, 67, 57, 87, 45, 99, 64, 678, 577, 874, 454]
print(a_list[-1])#returns the last element in the list
# 454
print(a_list[-2])#returns the second to last element in the list
# 874
print(a_list[-9:-1])#extracts a certain sublist using negative indexes excluding -1
# [57,87,45,99,64,678,577,874]
print(a_list[-5:])#returns the last 5 elements inthe list
# [64,678,577,874,454]
print(a_list[:-5])#returns the list minus its last 5 elements
# [1,2,3,4,6,67,57,87,45,99]
print('original\n',a_list,a_list[::2])#adds a third element called step; skips every second element of the list

print(a_list[::-1])#returns a_list'selements in reverse order

print('Sets---------------------------------')
#Sets -unordered collections of unique elements
set1 ={"1.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4"}#creating a set
list1 =[11,12,13,14,15,15,15,11]
string1 ="aaabcdeeefgg"
set1 =set(list1)#creating a set from a list; removing duplicate elements; 
# returns {11, 12, 13, 14, 15}
set2 =set(string1)#creating a set from a string; removing duplicate characters; 
# returns {'b', 'a', 'g', 'f', 'c', 'd', 'e'}; 
# remember that sets are UNORDERED collections of elements
print(len(set1))#returns the number of elements in the set
print(11 in set1) #returns True; checking if a value is an element of a set
print(10 not in set1)#returns True; checking if a value is an element of a set
print(set1.add(16))#adding an element to a set
print(set1.remove(16))#removing an element from a set
print('Frozensets -immutable sets------------------')
#The elements of a frozenset remain the same after creation.
fs1 =frozenset(list1)#defining a frozenset 
print(fs1)
# frozenset({11,12,13,14,15})#the result
# fs1.add(12)
# AttributeError:'frozenset'object has no attribute 'add
# no operation or method works

print('Set methods---------------------------')
setX=set1.intersection(set2)#returns the common elements of the two sets
print(set1,set2,setX)
set1.difference(set2)#returns the elements that set1 has and set2 doesn't
set1.union(set2)#unifying two sets; the result is also a set, so there are no duplicate elements; not to be confused with concatenation
set1.pop()#removes  a  random  element  from  the  set;  
# important :set  elements  cannot  be  removed  by index because sets are UNORDERED collections of elements, so there are no indexes to use
set1.clear()#clearing a set; the result is an empty set

print('Tuples-------------------------------')
#Tuples -immutable lists (their contents cannot be changed by adding, removing or replacing elements)
my_tuple =()#creating an empty tuple
my_tuple =(9,)#creating a tuple with a single element; DO NOT forget the comma
print(my_tuple)
my_tuple =(1,2,3,4)#Tuples -the same indexing & slicing rules apply as for lists
len(my_tuple)#returns the number of elements in the tuple
my_tuple[0]#returns the first element in the tuple (index 0)
my_tuple[-1]#returns the last element in the tuple (index -1)
my_tuple[0:2]#returns (1, 2)
my_tuple[:2]#returns (1, 2)
my_tuple[1:]#returns (2, 3, 4)
my_tuple[:]#returns (1, 2, 3, 4)
my_tuple[-2:]#returns (3, 4)
my_tuple[:-2]#returns (1, 2)
my_tuple[::-1]#returns (4, 3, 2, 1) reverse the tuple
my_tuple[::2]#returns (1, 3)

print('Tuples -tuple assignment / packing and unpacking-------')
tuple1 =("Cisco","2600","12.4")
(vendor,model,ios)=tuple1 #vendor will be mapped to "Cisco" and so are the rest of the elements  with  their  corresponding  values;  
# both  tuples  should  have  the  same  number  of elements
(a,b,c)=(1,2,3)#assigning values in a tuple to variables in another tuple
min(tuple1)#returns "12.4"
max(tuple1)#returns "Cisco"
tuple1 +(5,6,7)#tuple concatenation
tuple1 *20#tuple multiplication
"2600"in tuple1 #returns True
784 not in tuple1 #returns True
del tuple1 #deleting a tuple