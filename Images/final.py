from turtle import *
import random
import time
import sys
# Powerups 
#: Epipen - Used to heal yourself from any poisonous items you consume or touched. 
#: Weapon - Used to kill any killer that tends to strike you down and make you safe.
#: Automatic pass (Check) - Allows you to skip pass through 1 day without any form of elimination from the game.

""" Template ( Actual code BELOW )

if power_choice in powerups:
    claimed_power = powerups[power_choice]
else:
    exit()

# Show description
type_text(f"You have unlocked a {claimed_power}!")
add_to_inventory(claimed_power)

if power_choice == "1":
    type_text("This power heals your wounds.")
elif power_choice == "2":
    type_text("This power can kill or stun killers.")
elif power_choice == "3":
    type_text("This lets you skip a day of danger!")

""" 
inventory = []
def add_to_inventory(item):
    inventory.append(item)
    type_text(f"{item} added to your inventory.") # this function is storing any power up into a list.

def use_powerup(item):
    if item in inventory:
        inventory.remove(item) # removes the powerup out of the system.
        type_text(f"You've successfully used {item}!")
        return True # only if the statement is in inventory 
    else:
        return False # if not inventory.
powerups = { 
    "1" : "epipen",
    "2" : "weapon",
    "3": "skip",
}

def random_powerup():
    key = random.choice(list(powerups.values()))
    return key, powerups[key]
#Killers:
# A man who has a knife 
# A coworker who has illegal drugs 
# A person who brings in a bounty hounter

killers = {  
        "1" : "Knife Guy",
        "2" : "Illegal Drug/Chemical Dealer",
        "3" : "Bounty Hunter",
    }


def random_killer():
    return random.choice(list(killers.values()))

# turtle starts here:
# --- Screen setup ---
screen = Screen()
screen.setup(900, 700)
screen.title("Survival of the Unknown")

# --- Text turtle ---
pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the l4ft
start_y = screen.window_height() // 2 - 40 #40 pixels away from the top

pen.goto(start_x, start_y)

# --- Word Wrapping ---
def type_text(message, line_length=65, line_space=30, speed=0):
    words = message.split(" ") #spaces out the words 
    line = "" # refers to as a space between words

    for word in words:
        if len(line + word) > line_length: # length of line plus the word being greater than the line length, proceed to the next length, make a new line.
            for char in line:
                pen.write(char, font=("Chiller", 18, "normal"))
                pen.forward(12)
                time.sleep(speed) # speed controls the amount of delay time for text.

            # new line
            pen.goto(start_x, pen.ycor() - line_space)
            line = ""

        line += word + " " # text format in terminal or turtle 

    # last line
    for char in line:
        pen.write(char, font=("Chiller", 18, "normal"))
        pen.forward(12)
        time.sleep(speed)

    pen.goto(start_x, pen.ycor() - line_space)


# type text imports text into turtle as a print function.

# --- Game Start ---
type_text("Survival of the Unknown")
name = screen.textinput("Name", "Enter your name: ")

type_text(f"Welcome {name}.") #{ Are referrences when it comes to you given a parameter of a certain veriable or statement.}
type_text("You are now part of a simulation that will test your survival.")
type_text("You are in school for a science experiment.")
type_text("However, a purge has broken out—killers and poisonous traps are everywhere.")
type_text("These kinds of traps can be something you eat as well")
type_text(f"{name} becomes anxious and prepares for danger.")

# --- Proceed? ---
sequence = screen.textinput("Proceed?", "Do you wish to proceed? (Y/N)").lower()

if sequence in ("y", "yes"):
    type_text("You're ambitious! I like that! The goal is to survive 8 days.")
    type_text("Your choices will determine your fate.")
    type_text("Stay alert as danger approaches.")
else:
    type_text(f" As much I would want to let you get pass {name}, i'm sorry but you must continue.")
    type_text("Survival depends on your awareness and decisions.")
    type_text(f"If you think there's a way out, it is impossible for you {name}.")
    type_text("However, of you survive through these 8 days, you will be set free from this horror.")

# --- Day 1 ---
screen.reset() 

pen = Turtle(visible=False)
pen.hideturtle()
pen.penup()

start_x = -screen.window_width() // 2 + 20 #20 pixels up from the l4ft
start_y = screen.window_height() // 2 - 40 #40 pixels away from the top

pen.goto(start_x, start_y)

type_text("DAY 1")
type_text("You walk into school sensing something strange.")
type_text("It could be the feeling of frustartion of dealing with the unknown.")
type_text("You noticed that the crack is getting bigger and some type of light.")
type_text("The wall has a glowing crack. Do you want to inspect it?")

response = screen.textinput("Inspect?", "Yes or No?").lower()

if response in ("yes", "y"):
    type_text("You approach the crack.")
    type_text(f"Bats burst out and {name}, starts to scream!")
    type_text("A harmless scare… but danger grows.") # f refers to activating the variable function.
else:
    type_text("You ignore the crack and head to class.")
    type_text("A wise choice you had made... but things are getting worse.")

screen.reset() 
screen = Screen()
screen.setup(900, 700)

pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

type_text(" I have a special gift for you!")
type_text("Powerups for you to choose from!")
#powerup script starts here:
power_choice = screen.textinput(f"Powerup","Pick a number between 1 to 3 ")

if power_choice in powerups:
    claimed_power = powerups[power_choice] # captures the correct power
  #  inventory.append(claimed_power) # stores the power


if power_choice == "1": # variable in something is the same as if a variable is == to a response 
    type_text(f"You have unlocked a {claimed_power}!") #powerups[powerchoice] calls in the dictionary powerups to connect with the input of power choice
    type_text("This power up allows you to heal your wounds and damages you might encounter from a killer ")
    
    add_to_inventory(claimed_power)
elif power_choice == "2":
    type_text(f"You have unlocked a {claimed_power}")
    type_text("This power is only to be used to kill or knock out killers approaching you.")
    type_text("Use it wisely!")
    add_to_inventory(claimed_power)

elif power_choice == "3":
    type_text(f"You have unlocked a {claimed_power}!")
    type_text("This powerup allows you to be able to pass right through and day you encounter! ")
    type_text("A ticket of survival I would call it.")
    add_to_inventory(claimed_power)      
else:
    exit
#Screen Refresh 
screen.reset() 

pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

type_text( " As the night grows, you tend to feel scared that something is going to happen. ")
type_text( " You look around in your home for hours trying to see anything suspious. ")
type_text( " You became hungry for a bowl of cereal, but you're unsure if anything is infected. ")
sequence = screen.textinput("Proceed?", "Do you wish to proceed? (Y/N)").lower()
if sequence in ("y", "yes"):
    type_text(f"The cereal is infected! As {name}, continues to eat the cereal, you become dizzy. ")
    type_text(f"You have faced death from poison.")
    type_text("Game Over!")
    screen.bye() # excutes the screen to disappear after lost 
else:
    type_text("You grew hungry, but you passed through this day.")
    type_text("Good job on being aware, but it only gets worse.")


screen.reset() 

pen = Turtle(visible=False)
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

# Day 2 --

type_text("DAY 2")
type_text(" You start to feel cautious after what happened during the purge.")
type_text("Killers going around into peoples homes, stuff being contaminated with chemicals. ")
type_text("Anything you can imagine.")
type_text(" You go to lunch before you start heading home. ")
type_text(" You start eating then thought about grabbing a snack from the vending machine.")

response = screen.textinput("Inspect?", "Yes or No?").lower()

if response in ("yes", "y"):
    type_text(f"{name}, grabs a bag a chips and makes their way home. ")
        # f refers to activating the variable function.
elif response in ("no" , "n"):
    type_text(f"{name} , doesn't make the transaction to get a snack.")
    type_text(f"{name} feels that it is potentially affected.")
else:
    exit

type_text("You start to look outside as the sun drops down.")
type_text("You start to observe that something isn't right so you check outside. ")

type_text("A strange man picks up on the door after checking your windows" )
type_text("You still try to figure out who it is.")

person_choice = screen.textinput("Killer", "Choose an option between 1 to 3 : ")

if person_choice in killers:
    found_killer = killers[person_choice]

if person_choice in "1": # variable in something is the same as if a variable is == to a response 
    type_text(f"You have encountered a {killers[person_choice]}!") #killers[person_choice] calls in the dictionary powerups to connect with the input of power choice
    type_text("They have an impluse to try to stab you out of no where.")
    type_text("You tend to run in fear running out of your place, hoping they don't chase you. ")
    if use_powerup("weapon") or use_powerup("skip"):
        type_text("You took a chance and attack, the killer has fled the scene.")
    else:
        type_text(f"{name} had a chance of running, but the knife guy wasn't afar.")
        type_text("You wasn't able to survive the attack and was severely damaged.")
        screen.bye()
        
elif person_choice in "2":
    type_text(f"You entered across a {killers[person_choice]}")
    type_text("He gave you a potion trying to tell you that this potion will make you immue to poison")
    type_text(f"{name} is unsure if it's safe to consume a drug from a random")

    response = screen.textinput ( "Consume", "Are you going to consume the potion? (Y/N)").lower()
    
    if response in ("yes" , "y"):
     type_text(f"{name} grew more anxious and decides to take a risk and drink this potion.")
    if use_powerup("epipen"):
         type_text("You inject yourself and survive the toxins!")
         
    elif response ("no", "n"):
        type_text(f"{name} decides to throw away the potion and noticed a small gas coming out.")
        type_text("You are safe from danger. For now.....")
    else:
     type_text("The chemicals inside the potion overwhelm you…")
     type_text(f"{name} has died from these toxins taking over their body.")
     screen.bye()



elif person_choice in "3":
        type_text(f"You have encountered the mysterious {killers[person_choice]}!")
        type_text("They are looking to hunt you down and claim the money that was placed on you! ")
        type_text("RUN!!!!")
        if use_powerup("skip"):
            type_text("You've escaped from the bounty hunter!")
            type_text("It's probably safe to return back home now")
        elif use_powerup("weapon"):
            type_text("You go against a 1 on 1 with the bounty hunter.")
            type_text("You have shot down the hunter and realized that he died.")
        else:
            type_text("The bounty hunter tends to strike you down.")
            type_text(f"{name} faced fatal wounds")
            type_text("Game Over!")
            screen.bye()
else:
    type_text("Choice invalid")
    person_choice = screen.textinput("Killer", "Choose an option between 1 to 3 : ")

# Day 3 --

screen.reset() 
pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

type_text("Day 3")
type_text(f"Things are getting rough already.{name} starts to become overwhelmed and unsure with everything.")
type_text("Before you began another episode of horror, you need powerups.")

power_choice = screen.textinput(f"Powerup","Pick a number between 1 to 3 ")

if power_choice in powerups:
    claimed_power = powerups[power_choice] # captures the correct power
  #  inventory.append(claimed_power) # stores the power


if power_choice == "1": # variable in something is the same as if a variable is == to a response 
    type_text(f"You have unlocked a {claimed_power}!") #powerups[powerchoice] calls in the dictionary powerups to connect with the input of power choice
    type_text("This power up allows you to heal your wounds and damages you might encounter from a killer ")
    
    add_to_inventory(claimed_power)
elif power_choice == "2":
    type_text(f"You have unlocked a {claimed_power}")
    type_text("This power is only to be used to kill or knock out killers approaching you.")
    type_text("Use it wisely!")
    add_to_inventory(claimed_power)

elif power_choice == "3":
    type_text(f"You have unlocked a {claimed_power}!")
    type_text("This powerup allows you to be able to pass right through and day you encounter! ")
    type_text("A ticket of survival I would call it.")
    add_to_inventory(claimed_power)      
else:
    exit

type_text(f"{name} realizes that everything isn't normal and is scared that this purge is the new norm.")
type_text(f"As {name} begans an experiment making potions for class, they feared that the potion will cause them harm ")
type_text(f"{name} finishes up their custom potion for an assignment that they can keep.")
type_text("You think it's safe to keep the potion?")

decision = screen.textinput("Question","Do you keep this potion in your possession? (Y/N)").lower()
if decision in ("yes", "y"):
    type_text(f"{name}, decides to keep the potion. However, the potion is remained to be safe to consume. ")# variable in something is the same as if a variable is == to a response 
    type_text(f"You have unlocked a {claimed_power}!") #powerups[powerchoice] calls in the dictionary powerups to connect with the input of power choice
    type_text("This power up allows you to heal your wounds and damages you might encounter from a killer ")
    
    add_to_inventory(claimed_power)
        # f refers to activating the variable function.
else:
    type_text(f"{name} , doesn't keep the potion")
    type_text(f"{name} feels that it is potentially affected.")

# Day 4 -- 

screen.reset() 

pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

type_text("Day 4")
type_text(f" As {name} survives through out the days, they start to become more aware and less terrified about the purge.")
type_text("You got an email from your teacher that classes are cancelled today due to killers spreading.")
type_text(f"{name} wishes that all of it ends before they feel more cautious")
type_text("After a dark stormy night, you notices flashes of light outside and you thought about checking it out.")

# resetting the screen 
screen.reset() 
pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

type_text("As you got closer to the flashing lights, you noticed something suspious.")
type_text("You see toxin gas and you started coughing.")
type_text(f"{name} coughs started to become lethal.")
type_text(f"{name} isn't confident that they aren't going to make it out the toxin alive.")

if use_powerup("skip"):
            type_text(f"{name} escaped from the dangerous toxins from the field!")
            type_text("Try to avoid more of the toxins next time.")
elif use_powerup("epipen"):
            type_text(f"{name} started to use this medicine to remove the toxins out of their body.")
            type_text("You made it out of the toxins safely. Stay cautious from toxic gas.")
else:
     type_text(f"{name} was in danger from the toxin.")
     type_text("You've died from inhaling the toxic gas from the field.")
     type_text("Game Over!")
     screen.bye()

# Day 5 -- 

# resetting the screen 
screen.reset() 
pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

type_text("Day 5")
type_text ( "Things are becoming rough, but you are making it really far.")
type_text("As you start the day, you need a powerup to keep you alive.")
type_text(f"{name} looks around viciously for anything dangerous to them.")
type_text(f"{name} sees if they can find some pain killers around for their headache.")

power_choice = screen.textinput(f"Powerup","Pick a number between 1 to 3 ")

if power_choice in powerups:
    claimed_power = powerups[power_choice] # captures the correct power
  #  inventory.append(claimed_power) # stores the power

if power_choice == "1": # variable in something is the same as if a variable is == to a response 
    type_text(f"You have unlocked a {claimed_power}!") #powerups[powerchoice] calls in the dictionary powerups to connect with the input of power choice
    type_text("This power up allows you to heal your wounds and damages you might encounter from a killer ")
    
    add_to_inventory(claimed_power)
elif power_choice == "2":
    type_text(f"You have unlocked a {claimed_power}")
    type_text("This power is only to be used to kill or knock out killers approaching you.")
    type_text("Use it wisely!")
    add_to_inventory(claimed_power)

elif power_choice == "3":
    type_text(f"You have unlocked a {claimed_power}!")
    type_text("This powerup allows you to be able to pass right through and day you encounter! ")
    type_text("A ticket of survival I would call it.")
    add_to_inventory(claimed_power)      
else:
    exit

# resetting the screen 
screen.reset() 
pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

type_text("Now you should be geared up with a kit.")
type_text("You're almost there, but I wouldn't be too confident.")

#Day 6 -- 
screen.reset() 

pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 
pen.goto(start_x, start_y) 

type_text("Day 6")
type_text(f"{name} witness someone getting stabbed and was terrified.")
type_text("screamming and running at the same time. The killer chases after you.")


response = screen.textinput("Escape", "You believe that you'll escape the killer? (Y/N)").lower()

if response in ("yes" , "y"):
    type_text("The killer is on the run making it difficult to escape.")

elif response in ("no" , "n"):
    type_text(f"{name} was worried that they won't make it out alive.")

else:
    exit

if use_powerup("skip") or use_powerup("weapon"):
    type_text(f"{name} escaped from danger from the killer!")
    type_text(f"{name} made it back home safely")

else:
    type_text("Bummer, the killer was able to catch up to you.")
    type_text(f"{name} faced fatal blows and wounds that are impossible to heal.")
    type_text("Game Over!")
    screen.bye()

# Day 7 --
screen.reset() 
pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

type_text("On a bright sunny morning, you see an email from your school that the purge is ending in 2 days.")
type_text("However, the storm of killers are swarming much more.")
type_text(f"{name} was prepared to either fight or escape from killers all around.")

screen.reset()
pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

person_choice = screen.textinput("Killer", "Choose an option between 1 to 3 : ")

if person_choice in killers:
    found_killer = killers[person_choice]
    if person_choice in "1" or "3": # variable in something is the same as if a variable is == to a response 
     type_text(f"You have encountered a {killers[person_choice]}!") #killers[person_choice] calls in the dictionary powerups to connect with the input of power choice
    type_text("They are eager to hunt you down out of anger with no remorse.")
    type_text("You tend to run in fear running out of your place, hoping they don't chase you. ")
    if use_powerup("weapon") or use_powerup("skip"):
        type_text("You took a chance and attack, the killer has fled the scene.")
        type_text(f"{name} took a risk to fight off the killer and remained alive.")
    else:
        type_text(f"{name} had a chance of running, but the killer is close.")
        type_text("You wasn't able to survive the attack and was severely damaged.")
        type_text()
        screen.bye()

elif person_choice in "2":
    type_text(f"You entered across a {killers[person_choice]}")
    type_text("He's back with another potion telling you to not be scared or concerned about the dangers of the purge.")
    type_text(f"{name} felt that they can trust them so they took the potion")
    if use_powerup("skip") or use_powerup ("epipen"):
        type_text(f"{name} takes the potion.")
        type_text(f"{name} uses this potion and poured it on the killer. The Chemical Dealer dies.")
        type_text("You've passed the encounter.")
    else:
     type_text(f"{name} was in danger from the toxin.")
     type_text(f"The killer told {name} that the potion is prototype for healing wounds.")
     type_text("You started to become sick and ill.")
     type_text("The Chemical Dealer remained alive.")
     type_text("Game Over!")
     screen.bye()

else:
    type_text("Choice invalid")
    person_choice = screen.textinput("Killer", "Choose an option between 1 to 3 : ")

#  Day 8 --
screen.reset()
pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

type_text("Day 8")
type_text("The final day has arrived.")
type_text(f"{name} hopes never have to go through this again.")

screen.reset()
pen = Turtle()
pen.hideturtle()
pen.penup()

# Left-aligned top
start_x = -screen.window_width() // 2 + 20 #20 pixels up from the height
start_y = screen.window_height() // 2 - 40 #40 pixels away from the edge 

pen.goto(start_x, start_y)

type_text(f"{name} went outside to see that there are no more killers, but a ton of toxic gas")
type_text("These gasses are everywhere and it aims towards your home.")

type_text("The gasses are becoming lethal to a point where you want to run away, but you suspect that it's a fluke.")
response = screen.textinput ("Question", "Do you go out of your home? (Y/N)")

if response in("yes" , "y"): # look at if response in string == to if response == to yes or y
    type_text("You ended up running away hoping for some fresh air somewhere.")
    type_text("It gets to a point where you're slowly given up.")
    if use_powerup ("skip") or use_powerup ("epipen"):
        type_text(f"{name} tends to find some fresh air and was freed from the madness from these toxins.")
        type_text("Congratulations, you win!")
else:
    type_text("These gasses got stronger and stronger.")
    type_text("the toxins started to go all over your body and you started to faint.")
    type_text("You were so close of surviving this unknown terror.")
    type_text("You lose!")
    screen.bye()
done()   