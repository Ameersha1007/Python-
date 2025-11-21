arr=[3,5,7,10,11]

largest=arr[0]
secondlargest=arr[0]

for num in arr:
    if num > largest:
        largest = num

secondlargest = -99

for num in arr:
    if num != largest and num > secondlargest:
        secondlargest = num
print(secondlargest)
