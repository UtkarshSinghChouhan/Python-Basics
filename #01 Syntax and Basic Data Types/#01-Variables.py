a = "Utkarsh"
b = "Singh"
c = "Chouhan"


print(a + b + c)



x = "Mayank"
x = 4   #This will overrride the above declared variable

print(x)



# ============= CASTING ==================

x = str(3)      
print(x)

y = int(3)
print(y)

z = float(3)
print(z)



# ============= ASSIGNING MULTIPLE VALUES ==================

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# ============= ONE VALUE TO MULTIPLE VARIABLES ==================

a = b = c = "Orange"

print(a)
print(b)
print(c)


# ============= UNPACK COLLECTION (LIST or TUPLES) ==================

fruits = ["apple", "banana", "mango"]

one, two, three = fruits

print(one)
print(two)
print(three)