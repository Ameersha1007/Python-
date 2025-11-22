text=input("enter a string:")
visit=""

for i in text:
    if i not in visit:
        count=0

        for j in text:
            if j==i:
                count=count+1

        print(i,"=",count)
        visit=visit+i
