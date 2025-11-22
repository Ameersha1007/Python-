text=input("enter a string:")
vowels="aeiou"

vcount=0
cocount=0

for i in text:
    if i.isalpha():
        if i in vowels:
            vcount=vcount+1
        else :
            cocount=cocount+1
print(vcount)
print(cocount)
