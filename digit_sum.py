two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
sum = 0
two_digit_number = int(two_digit_number)
while(two_digit_number !=0):
   rem = two_digit_number%10
   sum = sum +rem
   two_digit_number = int (two_digit_number /10)
print(sum)
  
