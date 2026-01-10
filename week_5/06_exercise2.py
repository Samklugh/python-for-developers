number_list=[]
your_number=int(input("Enter a number: "))

while your_number != 0:
    your_number=int(input("Enter a number: "))
    number_list.append(your_number)
    
print(f"The numbers your entered are: {number_list}")

sum_of_numbers=0
for number in number_list:
    sum_of_numbers += number
print(f"The sum of the numbers is: {sum_of_numbers}")

average=sum_of_numbers/len(number_list)
print(f"The average of the numbers is: {average}")

#maximum number
largest_number=0
for number in number_list:
    if number > largest_number:
        largest_number = number
print(f"The largest number is: {largest_number}")

#minimum  positive number
smallest_number=9999999
for number in number_list:
    if number < smallest_number and number > 0:
        smallest_number = number

print(f"The smallest positive number is: {smallest_number}")
