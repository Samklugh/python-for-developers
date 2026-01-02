#triple-quoted strings for multi-line text

# introduction and instructions

print("""Hello, Welcome to Bible Adventure Game!
In this game, you will be going on an adventure through the Bible.
You will be making choices that will affect the outcome of your adventure.
if each choice you make is correct, you will move on to the next part of the adventure.
the expected respkonse for each question is in ALL CAPS.
Good luck and have fun!
      
""")

# solutions with nested if statements

# .upper string method is used to standardize user input to uppercase for easier comparison

question1= input ("""You're given the choice to be one of the following Bible characters: MOSES, OR JOSEPH.
     Which do you choose? 
                 
                 """).upper()

if question1=="MOSES":

    question2= input("""You found out that you are not the son of Pharaoh's daughter, but a Hebrew.
    God has called you to lead the Israelites out of Egypt and rebel against the family that raised you.
    do you OBEY or DISOBEY  
                     
                     """).upper()

    if question2=="OBEY":

        question3= input("""You will be kicked out of Pharoah's palace, and you will lose all the comfort and privileges of being a prince.
        LOSE, KEEP or IGNORE  privileges? 
                         
                         """).upper()

        if question3=="LOSE":

            print("""Congratulations! You will part the Red Sea and lead the Israelites to freedom.
            You have successfully completed the Bible Adventure Game as MOSES!
                  
                  """)

        elif question3=="KEEP":
            print("""you will live the rest of your life in luxury but never as a King, and you will live outside Gos's will for your life.
                  
                  """)

        elif question3=="IGNORE":
            print("""you have ignored the call of God.""")

        else:
            print("Invalid choice. Please restart the game and choose either LOSE, KEEP or IGNORE.")

    elif question2=="DISOBEY":
        question3= input("""You will be prince for a while, and your peope will remain as slaves.
            do you AGREE or DISAGREE? 
                         
                         """).upper()
        
        if question3=="AGREE":
            print("""you have agreed to live outside God's will for your life.""")

        elif question3=="DISAGREE":
            print("""you have disagreed with God's plan for your life.""")

        else: print("Invalid choice. Please restart the game and choose either AGREE or DISAGREE.")


    else:
            print("Invalid choice. Please restart the game and choose either OBEY or DISOBEY.")

elif question1=="JOSEPH":

    question2= input("""You had a a dream that your brothers were bowing down to you
    would you share with them? SHARE or MUTE
                     
                     """).upper()

    if question2=="SHARE":

        question3= input("""Your brothers are very jealous of you and your dreams, and you were sold as a slave in Egypt. POtiphar's wife tried seducing you..
        do you AGREE or FLEE? 
                         
                         """).upper()

        if question3=="AGREE":

            print("""You will sin against God and go to prison.
            You have successfully completed the Bible Adventure Game as JOSEPH!""")

        elif question3=="FLEE":
            print("""you will live a life of integrity and honor God.
                  You will eventually become second in command in Egypt.
                  You have successfully completed the Bible Adventure Game as JOSEPH!""")
            
        else:
            print("Invalid choice. Please restart the game and choose either AGREE or FLEE.")
    
    elif question2=="MUTE":
        question3= input("""Your brothers are very confused about your dreams, and you were sold as a slave in Egypt.
            do you AGREE or DISAGREE? 
                         
                         """).upper()
        
        if question3=="AGREE":
            print("""you have agreed to live a life of silence.""")

        elif question3=="DISAGREE":
            print("""you have disagreed with God's plan for your life.""")

        else: print("Invalid choice. Please restart the game and choose either AGREE or DISAGREE.")

    else: print("Invalid choice. Please restart the game and choose either SHARE or MUTE.")

else:
    print("Invalid choice. Please restart the game and choose either MOSES or JOSEPH.")
