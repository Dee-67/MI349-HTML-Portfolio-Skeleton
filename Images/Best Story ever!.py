print("Hello")
print("")
print("Welcome to the world of Marvel!")


Leader = "Thor"
print("")
print(" Welcome everyone! I am" , Leader, "and I want to recruit someone who is worthy to fight by my side.")
print(" Doing this, I am going to give you some challenges of training to test your skills on how you are capable of fighting" "\n" "against crime.")
print(" Who ever is ready, come up to me and show me how worthy are you.")
print("")
print(Leader , "was looking around and started picking people one by one")
print(" You there, what is your name?")
player = input("Enter player name: ")
print("Welcome," , player , " it's nice to see you here.")
print("Now tell me, what is your superpower?")
power = input("Pick a number between 1 to 4: ")

if power == "1":
    print(" You have Agility!")
    
elif power == "2": 
    print("You are Stealthy!")
elif power == "3":
    print("You have Teleportation!")
elif power == "4":
    print("You have super speed!")

else:
    power = input("Pick a number between 1 to 4: ")
    "Please try again!"

print ("")
print(Leader , "starts to pick out", player, "superpower and is giving them a challenge")
print("Now" , player, "We are going to test out your powers before we start training!")
print("I hope you are worthy for crime fighting.") 

print("") 

print("Now you have your superpower" , player, "we are going to start training!")
print("We are going to start by picking a number between 1 to 3")
print("What would that number be?")

num = input("Choose a number : ")

if num == "1":
    print("You're going to fight against robbers and take them to the police.")

elif num == "2": 
    print("Ah.. very easy. you are going to go through a maze and save someone from a tall building while enemies tries to chase after them.")

elif num == "3": 
    print("My favorite number. You are going to fight along side me against crime, but its not going to be easy, so be prepared!")
    
else: 
    num = input("Choose a number : ")
    print("please pick again.")

    print ("")
    print("Now you have done your training for" ,Leader, "The next number you pick determines if you succeed your training or you had failed the simulation.")
    num2 = input("pick the final number : ")

    if num2 == "1" or "3": 
        print("You have passed the training")

    else: 
        print("I'm sorry, you had failed the simulation!")