# =========== str(Text Type) =================
name = "Utkarsh Singh Chouhan"
print(name)


# =========== int(Numeric type) =================
x = 50
print(type(x))


# =========== float =================
y = 50.25
print(y)


# =========== bool =================
z = True
print(z)


# =========== LIST =================
a = ["apple", "banana", "mango"]
print(a)


# =========== TUPPLES =================
b = ("apple", "banana", "mango")
print(b)


# =========== RANGE =================
c = range(6)
print(c)


# =========== DICT =================
d = {
    "name" : "Utkarsh",
    "profession" : "SDE"
}
print(d)


# =========== SET(Allows only unique values) =================
e = {"apple", "banana", "banana", "apple"}
print(e)



# =========== RANDOM NUMBER =================
#Python does not a random() funtion but Python has a built-in module random that can be used to make random numbers

import random
print(random.randrange(1, 10))