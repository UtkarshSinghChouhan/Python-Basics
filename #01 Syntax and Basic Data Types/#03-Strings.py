# =============== Quotes Inside Quotes ================

print("It's alright")
print("His name is 'Utkarsh'")
print('His name is "Utkarsh"')


# =================== Multiline Strings ===============
x = """Utkarsh
Singh 
Chouhan"""

print(x)


# =================== Strings are Arrays ===============
b = "Hello, World!"
print(b[1])


 
# =================== Check String ===============
txt = "This is Utkarsh Singh Chouhan"
print("Utkarsh" in txt)





# =================== SLICING ===============
a = "UtkarshSinghChouhan"
print(a[2:5])

# =================== Slice from the Start ===============
c = "Hello, World!"
print(c[:4])


# =================== Slice to the end ===============
d = "Mayank Singh Chouhan"
print(b[2:])





# =================== Common String Methods ===============
e = "utkarsh"
print(a.upper())


f = "UTKARSH"
print(f.lower())


h = "        Utkarsh         Singh           "
print(h.strip())            #removes whitespace from the begining and the end


i = "Utkarsh Singh Chouhan"
print(i.replace("Utkarsh", "Mayank"))


j = "Utkarsh"
print(j.split('a'))



# =================== String Concatenation ===============
a = "Utkarsh"
b = "Singh"
c = "Chouhan"
d = a + " " + b + " " + c
print(d)



# =================== STRING FORMAT [ f-String and format() ] ===============
val = 55
txt = f"The price is ${val}"
print(txt)


txt = "My name is {name}"
print(txt.format(name = "Utkarsh Singh Chouhan"))