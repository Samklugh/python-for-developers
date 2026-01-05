# to use range in a for loop, we can use the range() function which generates a sequence of numbers. The range() function can take one, two, or three arguments: start, stop, and step.

number= [1, 2, 3, 4, 5] 

for num in range(0, 10, 1): 
    print(num)
    #range(start, stop, step)... the loop will start at 0, stop before 10, and increment by 1 each time

    #its common to use the iterator variable name "i" when using range in a for loop
    # example:
# for i in range(5):
    # print(i)
    #this will print numbers from 0 to 4 (5 is excluded)

#note that the stop and step arguments are optional. if only one argument is provided, it is treated as the stop value, with start defaulting to 0 and step defaulting to 1. if two arguments are provided, they are treated as start and stop, with step defaulting to 1.