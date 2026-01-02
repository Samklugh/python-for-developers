men= int(input("How many men are there? "))
women= int(input("How many women are there? "))
total= men + women

#boolean expressions / boolean variables are expressions that evaluate to true or false
has_enough_players= total >=7
has_enough_women= women >=4

#both conditions must be true for and operator to return true

# if total >=7 and women >4:  
    # print("You can play.")
# else:
    # print("You cannot legal play.")

    # or

if has_enough_players and has_enough_women:
    print("You can play.")      
else:
    print("You cannot legal play.")


#negation operator is not. and it negates the boolean value
# NOTES: that there is order in boolean expressions. NOT is evaluated first before AND operation and then the OR operation

if not has_enough_players:
    print("You do not have enough players to play.")