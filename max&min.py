arr=[10,5,7,8,2]

maxno=arr[0]
minno=arr[0]

for num in arr:
    if num > maxno:
        maxno= num
    if num < minno:
        minno=num

print(maxno)
print(minno)
