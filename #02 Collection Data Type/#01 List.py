myList = ["Apple", "Banana", "Mango"]
print(myList)


newList = [True, 10, "utkarsh"]
print(newList)


# ================Type=========
print(type(newList), type(myList))





#  ================list() Constructor=========
myList = list(("apple", "mango", "grapes"))
print(myList)



#  ================Accessing List Items=========

l = [1, 2, 3, 4, 5]

print(l[1])         
print(l[-1])        #Negative Index -> -1 referes the last element
print(l[1: 4])      #Range of Indexes
print(l[: 4])      #Range of Indexes Stating from start
print(l[1:])      #Range of Indexes till end
print(l[-4:-1])      #Range of Negative Indexes(not including -1)




#  ================ Check if Item Exists(Mmebership Operator) ================
a = [1, 2, 3, 4, 5]
print(5 in a)



#  ================Change List Items=========
b =  ["Utkarsh", "Sigh", "Chouhan"]

b[0] = "Mayank"
print(b)

b[0 : 2] = ["Sunder", "Pal"]
print(b)

# ========================== ADD LIST ITEMS =======================

#  ================Append Items at the end=========
d = ["one", "two", "three"]
d.append("four")
print(d)
 


#  ================Insert Items=========
c = ["Utkarsh", "Mayank", "Sandhya", "Sunder"]
c.insert(1, "Sunny")
print(c)


#  ================Extend Items=========
e = ["a", "b", "c", "d"]
f = ["e" , "f", "g"]
g = ("h", "i", "j")


e.extend(f)
e.extend(g)         #The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).


print(e)



# ========================== REMOVE LIST ITEMS =======================


# ================= remove() method =============
a = ["apple", "banana", "banana", "mango"]
a.remove("banana")   #remove only the first occurence of the value
print(a)    


#====================== pop() method ========================
a = ["apple", "banana", "banana", "mango"]
a.pop(1)
print(a)

a.pop()
print(a)


#====================== Using the del keyword ========================
a = ["apple", "banana", "grapes", "mango"]
del a[1]
print(a)


#====================== clear() method ========================
b = ["apple", "banana", "grapes", "mango"]
b.clear()
print(b)


# ======================== LOOPING OVER A LIST ====================


# =============== for loop =================
a = ["apple", "banana", "grapes", "mango"]
for x in a:
    print(x)


for i in range(len(a)):
    print(a[i])

# =================== while loop ============
i = 0
while i in range(len(a)):
    print(a[i])
    i += 1

i = 0
while i < len(a):
    print(a[i])
    i += 1



# ================================== LIST COMPREHENSION ===========================
# List comprehensions offers a shorter syntax for when you want to create a newList based on the values of the existing list

a = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []


# newList contains all the values from the list "a", which has character "a" in them
for x in a:
    if 'a' in x:
        newList.append(x)

print(newList)


newList = [x for x in a if 'a' in x]
print(newList)