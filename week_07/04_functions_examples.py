#whenever we want to achieve same task multiple times in a program, we can define a function once and call it whenever needed. This promotes code reusability and modularity.
# 
def get_positive_values(prompt_text):
    """"This function prompts the user to enter a positive value, and re-prompt if the value entered is negative. """    

    #prompt for the value
    value= float(input(prompt_text)) #prompt_text is added  because we want to customize the prompt message when calling the function. Thsi is because prompt_text is a parameter.
    print(f"You entered: {value}")


    #check if the value is positive and reprompt if needed 
    if value < 0:
        print("The value must be positive. Please try again.")
        value= float(input(prompt_text))  #reprompting the user to enter a positive value.

    #return value
    return value

length= get_positive_values("Please enter the length of the rectangle: ")  #customizing the prompt message when calling the function.   
width= get_positive_values("Please enter the width of the rectangle: ")  

area= length * width
print(f"The area of the rectangle is: {area}.")