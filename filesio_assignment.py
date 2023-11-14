passage = open("passage.txt","r")
str_pass = passage.read()

lower_case = str_pass.lower()
#print(lower_case)

lis = list(str_pass.split())
#print(lis)

total_words = len(lis)
print("Total number of words:-",total_words)


count = 0
diction = {}

for char in lower_case:
    for j in range(97,123):
        aii_value = chr(j)
        if char == aii_value:
            count += 1
        diction[aii_value]=count
print(diction)

ratio_diction = {}

for ke,val in diction.items():
    value ="{:.2f}".format(val/total_words) 
    ratio_diction[ke]=value
print(ratio_diction)