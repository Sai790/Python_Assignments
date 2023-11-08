str_in = input("Enter num")
lis = list(str_in)
length = len(lis)

like_array = []

for i in range(length):
    b = int(lis[i])
    like_array.append(b)
    
for j in range(length):
    for s in range (length):
        if like_array[j] < like_array[s]:
            like_array[j],like_array[s]=like_array[s],like_array[j]
            
print(like_array)