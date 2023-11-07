card_number=input('Enter the card number')

number=list(card_number)

remove_last_digit = number[0:-1]

reverse_num = remove_last_digit[::-1]

size_of_number = len(reverse_num)

new_list=[]

for i in reverse_num:
    int_num=int(i)
    new_list.append(int_num)
    
for s in range(size_of_number):
    if s%2==0:
        new_list[s]=new_list[s]*2
        
for j in range (size_of_number):
    if new_list [j]>9:
        new_list[j]= new_list [j]-9
                
last_digit =  int(number[-1])
        
total_sum_card_number= sum(new_list,last_digit)

if total_sum_card_number % 10 == 0:
    print("card number is valid")
else:
      print("card number is invalid please check the card number")