animal= input("Enter your favorite animal: ").lower()

sound= ""

if animal=="dog":
    sound= "bark"

elif animal=="cat":
    sound= "meow"

elif animal=="cow":
    sound= "moo"

else:
    sound= "unknown sound"

print("A {} goes {}".format(animal, sound))