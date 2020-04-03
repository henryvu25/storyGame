"""
This is the Player class. It will allow you to instantiate your player object with a name, set inventory
that you can add or remove from (random trickets to collect), confidence pct that acts as
hit points (resource/health), affirmation points
that act as confidence boosters when you receive them (like a health potion/a useful trinket)
"""
from random import randrange
from random import random

class Player():
    def __init__(self, name):
        self.name = name
        self.inventory = ['Pencil', 'Notebook']
        self.confidencePct = 50
        self.affirmationPoints = 0
        
    def takeItem(self,item):
        self.inventory.append(item)
        print("You added {} to your backpack".format(item))
    
    def receiveAffirmation(self, affirmationPoints):
        self.affirmationPoints += affirmationPoints
        print("You received {} Affirmation Points! You can use these to remind yourself how not-so-worthless you are and build some self-confidence!".format(affirmationPoints))
        
    def changeConfidence(self, adjust):
        self.confidencePct = self.confidencePct + adjust
        print("Your confidence is now at {}%".format(self.confidencePct))
        
    def menu(self):
        option = input('MENU (p)rofile, (b)ackpack, (a)ffirmation, (q)uit: ')
        while True: #continues to display menu until input is 'q'
            if option == 'q':
                break
            if option == 'p':
                print("==========\nName: {}\nConfidence: {}%\nAffirmation Points: {}\n==========".format(self.name,self.confidencePct,self.affirmationPoints))
                option = input('MENU (p)rofile, (b)ackpack, (a)ffirmation, (q)uit: ')
            elif option == 'b':
                print("==========\nYour backpack contains: ")
                for item in self.inventory:
                    print(item)
                print("==========")
                option = input('MENU (p)rofile, (b)ackpack, (a)ffirmation, (q)uit: ')
            elif option == 'a':
                useAff = input("You have {} affirmation points. Use it to boost confidence? y/n: ".format(self.affirmationPoints))
                if useAff == 'y':
                    self.confidencePct = self.confidencePct + self.affirmationPoints
                    self.affirmationPoints = self.affirmationPoints - self.affirmationPoints
                    option = input('MENU (p)rofile, (b)ackpack, (a)ffirmation, (q)uit: ')
                else:
                    option = input('MENU (p)rofile, (b)ackpack, (a)ffirmation, (q)uit: ')
            else:
                option = input('MENU (p)rofile, (b)ackpack, (a)ffirmation, (q)uit: ')
    
    def attack(self,enemy):
        atkChoice = input("What will you do?\n(a) Punch 'em in the face! \n(b) Insult them \n(c) Say something nice \n(d) Run away \nType your choice: ")
        if atkChoice == 'a':
            punchAccuracy = random()
            if punchAccuracy > .20: #one in five chance to make contact
                print("You attempted to throw a punch..and missed!")
            else:
                enemy.confidencePct = enemy.confidencePct - 10
                self.confidencePct = self.confidencePct + 20 #will give confidence if hit lands
                if enemy.confidencePct < 0:
                    enemy.confidencePct = 0 #will avoid enemy from displaying negative confidence
                print("Wow! You punched {}! The bully's Confidence is now at {}%".format(enemy.name,enemy.confidencePct))
                input("▾")
                print("Your confidence is now at {}%".format(self.confidencePct))
        elif atkChoice == 'b':
            insultList = ["You smell like rotten cheese!","Your nickname should be dumbo","You look like a overused toothbrush!","Your family is a band of chimps!","You can't even spell 'The Louvre!'"]
            print("{}: 'Hey {}! {}'".format(self.name,enemy.name,insultList[randrange(0,len(insultList))])) #randomly selects from insult list. It is different from enemy insult list
            enemy.confidencePct = enemy.confidencePct - 10
            if enemy.confidencePct < 0:
                enemy.confidencePct = 0 #will avoid enemy from displaying negative confidence
            print("The bully's Confidence is now at {}%".format(enemy.confidencePct))     
        elif atkChoice == 'c':
            niceList = ["You smell like flowers!","You're smarter than a college student!","You look like a movie star!","Your family loves you!","You're a modern day DaVinci!"]
            print("{}: 'Hey {}! {}'".format(self.name,enemy.name,niceList[randrange(0,len(niceList))])) #randomly chooses from compliments
            enemy.confidencePct = enemy.confidencePct - 30 #strongest attack so far
            if enemy.confidencePct < 0:
                enemy.confidencePct = 0 #will avoid enemy from displaying negative confidence
            print("The bully is super confused, their Confidence is now at {}%".format(enemy.confidencePct))
            self.confidencePct = self.confidencePct + 10
            input("▾")
            print("Your confidence is now at {}%".format(self.confidencePct))
        elif atkChoice == 'd':
            print("You ran away like the whimp that you are")
            self.confidencePct = self.confidencePct - 20 #ends fight but hurts confidence
            enemy.confidencePct = 0 #ends the fight
            if self.confidencePct < 0:
                self.confidencePct = 0
            print("Your confidence is now at {}%".format(self.confidencePct))
            
    def gameOver(self): 
        if self.confidencePct <= 0:
            print("You've lost all confidence, and ran home to mommy.")
            input("▾")
            print("==========\nName: {}\nConfidence: {}%\nAffirmation Points: {}\n==========".format(self.name,self.confidencePct,self.affirmationPoints))
            print("Your backpack contains: ") #displays remaining points and inventory
            for item in self.inventory:
                print(item)
            print("==========")
            raise SystemExit #ends program immediately if confidence goes to 0
        
    def victory(self):
        print("You completed the school day, hopefully tomorrow will be better...")
        print("==========\nName: {}\nConfidence: {}%\nAffirmation Points: {}\n==========".format(self.name,self.confidencePct,self.affirmationPoints))
        print("Your backpack contains: ") #displays remaining points and inventory
        for item in self.inventory:
            print(item)
        print("==========")
                
    def __repr__(self): #used for testing and displaying object's values
        return "Name: {}\nBackpack: {}\nSelf-confidence: {}%\nAffirmation: {}".format(self.name,self.inventory,self.confidencePct*100,self.affirmationPoints)