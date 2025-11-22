arr=[2,3,5,7,2,3,5]
arr2=[]

for i in arr:
    found=0

    for j in arr2:
        if j==i:
            found=1

    if found==0:
         arr2.append(i)
print(arr2)         
        



