"""
This is the main program where the flow of the game/story is
"""

from highSchoolPlayer import Player #be sure to have these files in the same folder to use their classes
from highSchoolEnemy import Enemy

from random import randrange
from random import random

       
def main():
    print("Hello, and welcome to Confidence High! Where your life is meaningless and the people are terrible.\nBut hey! That's life! Just get good grades and graduate!")
    input("'ENTER' to continue ▾") #python3 allows you to push enter without any input to move forward. 
    name = input("First off, what is your name? ")
    player = Player(name)
    print("Well {}, this is your inner voice speaking. You're kind of a wimp, this day better go well, or we'll just go home and cry to mommy".format(player.name))
    input("▾") #the triangles help player keep track of where they are reading
    print("BTW...if 'MENU' ever appears, you can type in 'p' for profile")
    input("▾")
    print("You can also type 'b' to check your backpack, and 'a' to use Affirmation Points to boost Confidence! (if you even get any HAH!)")
    input("▾")
    player.menu() #see class Player methods*
    print("*RIIIING!*\nOh, {}! Sounds like class is about to start! Better hurry off now!".format(player.name))
    input("▾")
    print("You find a calculator on the ground..wonder who's it is...")
    answer = input("Take item? y/n: ")
    
    if answer == 'y':
        player.takeItem("Calculator")
    input("▾")
    
    print("...moments later...\nmade it to class 5 minutes late...whatever...")
    input("▾")
    
    player.menu()
    
    print("Maria: 'Oh dear! I've lost my calculator...what will I ever do?? *sigh*")
    input("▾")
    CalcCount = 0 #makes sure calculator is in inventory
    for item in player.inventory:
        
        if item == 'Calculator':
            CalcCount += 1
            answer = input('Give calculator to Maria? y/n: ')
            if answer == 'y':
                print("Maria: 'Omygosh! Thank you so much {}! You're like, totally the best!".format(player.name))
                
                input("▾")
                player.receiveAffirmation(10) #affirmation is added to player class
                player.inventory.pop() #removes calculator from inventory since it was the last thing added. probably not scalable if we need to remove other specific items
            else:
                print("Maria: I can't believe I lost my calculator, I guess I'll just FAIL!")
                input("▾")
                print("Cool Guy Mike: 'You can borrow mine'")
                input("▾")
                print("Maria: 'Omygosh! Thank you so much Cool Guy Mike! You're like, totally the best!")
                input("▾")
                print("Geez {}, you didn't even try to help her...".format(player.name))
                player.changeConfidence(-10)
    if CalcCount == 0: #if calulator was never picked up
            print("Geez {}, you dummy, you saw the calculator and you didn't pick it up!".format(player.name))
            input("▾")
            print("You could've helped this poor girl...you're worthless")
            input("▾")
            player.changeConfidence(-10)
    player.menu() #player can check points and boost confidence with affirmation at this point       
    #####
    print("*RIIING!!!*")
    input("▾")
    print("Class is out, time to trek the halls and hope no one bothers me")
    input("▾")
    print("Uh oh! a bully appears!")
    input("▾")
    bullyA = Enemy("Tony Spagoni", "The slickest guy in school. He'll shake you down and take your lunch money", 50, 10, "Tony Spagoni: 'Agh! You'll pay someday!'")
    bullyB = Enemy("Keith McTeeth", "The heaviest dude in school. Legend says he'll eat ANYTHING, maybe even you.", 50, 10, "Keith McTeeth: 'You're lucky I'm slow!'")
    bullyList1 = [bullyA, bullyB] #two bullies added to have variation between playthroughs
    bully1 = bullyList1[randrange(0,len(bullyList1))]
    bully1.enemyIntro()
    input("▾")
    while bully1.confidencePct > 0 and player.confidencePct > 0: #this is the battle sequence
        bully1.insult(player) #bully will always insult randomly from insult list (see class methods)
        input("▾")
        if player.confidencePct > 0: #if player is still alive
            player.attack(bully1) #player has attack choices (see class methods)
            input("▾")
        
    player.gameOver() #ends game if player has 0 confidence after battle sequence.
    
    print(bully1.endingPhrase)
    input("▾")
    print("Glad that's over with, off to the next class...")
    input("▾")
    ###
    print("*RIIING!!!*")
    input("▾")
    print("(In class...) \nMr. Teacha: '{}, great job on yesterday's assignment, your use of metaphor was lightning to the soul!'".format(player.name))
    input("▾")
    print("Mr. Teacha: 'Here's a Gold Star!'")
    player.takeItem("Gold Star")
    input("▾")
    player.receiveAffirmation(10) 
    player.menu() #player can check points and boost confidence with affirmation at this point 
    
    print("*RIIING!!!*")
    input("▾")
    print("Break time, better get my textbook for the next class")
    input("▾")
    print("*checks locker*")
    input("▾")
    print("Theres a note left in here!")
    input("▾")
    print("Dear {}, I have a crush on you.\nLove,\nYour Secret Admirer".format(player.name))
    input("▾")
    print("P.S. - just kidding, you're ugly")
    input("▾")
    print("Uh oh! a bully appears!")
    input("▾")
    print("'Did you like the note we gave you?' *giggles*")
    input("▾")
    
    bullyC = Enemy("Nakamura Twins", "The most popular duo, and the most annoying.", 60, 20, "Nakamura Twins: '*Yawn* eh, you're not worth our time'")
    bullyD = Enemy("Cheer Squad", "They're pretty, but they think they're all that and a bag of avocado toast", 60, 20, "Cheer Squad: 'WAHH! We're calling daddy!'")
    bullyList2 = [bullyC, bullyD] #two bullies added to have variation between playthroughs
    bully2 = bullyList2[randrange(0,len(bullyList2))]
    bully2.enemyIntro()
    input("▾")
    while bully2.confidencePct > 0 and player.confidencePct > 0:
        bully2.insult(player)
        input("▾")
        if player.confidencePct > 0:
            player.attack(bully2)
            input("▾")
        
    player.gameOver()
    print(bully2.endingPhrase)
    input("▾")
    
    print("*RIIING!!!*")
    input("▾")
    print("Time for my least favorite class...")
    input("▾")
    print("In class..\nMrs. Sanwitch: 'Hello class, I am very disappointed in all of you...'")
    input("▾")
    print("'Especially in you, {}. You got a 0 on the assignment...You have no talent'".format(player.name))
    input("▾")
    bully3 = Enemy("Mrs. Sanwitch", "The meanest teacher in the world. How does she even have this job?", 80, 20, "Mrs. Sanwitch: 'Why you little....'")
    bully3.enemyIntro()
    input("▾")
    while bully3.confidencePct > 0 and player.confidencePct > 0:
        bully3.insult(player)
        input("▾")
        if player.confidencePct > 0:
            player.attack(bully3)
            input("▾")
        
    player.gameOver()
    print(bully3.endingPhrase)
    input("▾")
    
    print("*RIIING!!!*")
    input("▾")
    
    print("school's over...we made it...")
    input("▾")
    print("Cool Guy Mike: 'Yo {}, I saw what you did to Mrs. Sanwitch! Awesome!!'".format(player.name))
    input("▾")
    player.receiveAffirmation(10)
    input("▾")
    player.menu()
    input("▾")
    print("Maria: 'Yeah {}! no one's ever stood up to her! You're so brave!'".format(player.name))
    input("▾")
    player.receiveAffirmation(10)
    input("▾")
    player.menu()
    input("▾")
    print("Janitor: 'Go {}!'".format(player.name))
    input("▾")
    player.receiveAffirmation(10)
    input("▾")
    player.menu()
    input("▾")
    player.victory() #displays at end of game - displays points and inventory
    
main()