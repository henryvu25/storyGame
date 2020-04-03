"""
This is the enemy class. It will instantiate an enemy object that has a name,
introduction description, confidence Pct that acts as hit points (resource/health),
damage that they can deal and an ending phrase when they run out of resource points (die)
"""
from random import randrange
from random import random

class Enemy():
    def __init__(self, name, intro, confidencePct, damage, endingPhrase): #can be programmed in when instantiating object
        self.name = name
        self.intro = intro
        self.confidencePct = confidencePct
        self.damage = damage
        self.endingPhrase = endingPhrase
        
    def insult(self, player): #takes in player object to affect its confidencePct
        insultList = ["You smell like old gym socks!","You're dumber than a doorknob","You look like a mop!","Your family is poor!","You're an uncultured swine!"]
        print("{}: 'Hey {}! {}'".format(self.name,player.name,insultList[randrange(0,len(insultList))])) #randomly selects from insult list. it is different from player's insult list
        player.confidencePct = player.confidencePct - self.damage
        if player.confidencePct < 0:
                player.confidencePct = 0 ##will avoid player from displaying negative confidence
        print("Your confidence is now at {}%".format(player.confidencePct)) #displays to the player their own confidence
    
    def enemyIntro(self):
        print ("==========\nIt's {}: {}\nConfidence: {}%\n==========".format(self.name,self.intro,self.confidencePct))