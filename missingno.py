n=5

actualsum=0
for i in arr:
    actualsum=actualsum+i

expectedsum=0
for j in range(1,n+1):
    expectedsum=expectedsum+j
    
missingno=expectedsum - actualsum
print(missingno)
