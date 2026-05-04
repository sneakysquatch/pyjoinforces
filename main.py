#import, pygame is unused for now but will be used to add graphics later
import random
import pygame
#declare variables ahead of time for cleanness
dealerbet = 0
tatsuyabet = 0
eikichibet = 0
ginkobet = 0
mayabet = 0
yukkibet = 0
unshuffled = []
shuffled = []
dealerhand = []
tatsuyahand = []
eikichihand = []
ginkohand = []
mayahand = []
yukkihand = []
cardvalues = {"1":10,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
players = ["Dealer", "Tatsuya", "Eikichi", "Ginko", "Maya", "Yukki"]
playerhands = {"Dealer":dealerhand, "Tatsuya": tatsuyahand, "Eikichi": eikichihand, "Ginko": ginkohand, "Maya": mayahand, "Yukki": yukkihand}
playerbets = {"Dealer":dealerbet, "Tatsuya": tatsuyabet, "Eikichi": eikichibet, "Ginko": ginkobet, "Maya": mayabet, "Yukki": yukkibet}
suits = ["♠","♥","♣","♦"]
#add cards to deck
for item in ["♠","♥","♣","♦"]:
    unshuffled.append("A"+item)
    shuffled.append("A"+item)
    for i in range(2,11):
        unshuffled.append(str(i)+item)
        shuffled.append(str(i)+item)
    for face in ["J","Q","K"]:
        unshuffled.append(face+item)
        shuffled.append(face+item)
random.shuffle(shuffled)
def validbet(bet):
    return bet > -1 and bet < 11
while True:
    try:
        tatsuyabet = int(input("Input Tatsuya's bet "))
        eikichibet = int(input("Input Eikichi's bet "))
        ginkobet   = int(input("Input Ginko's bet "))
        mayabet    = int(input("Input Maya's bet "))
        yukkibet   = int(input("Input Yukki's bet "))
    except:
        print("Erroneous bet value. Ensure bet is an integer.")
        continue
    if validbet(tatsuyabet) and validbet(eikichibet) and validbet(ginkobet) and validbet(mayabet) and validbet(yukkibet) and (tatsuyabet>0 or eikichibet>0 or ginkobet>0 or mayabet>0 or yukkibet>0):
        break
    print("One or more invalid bets. Please input all bets as a valid number and bet on at least one player.")
for hand in playerhands.values():
    hand.append(shuffled[0])
    shuffled.pop(0)
    hand.append(shuffled[0])
    shuffled.pop(0)
for player in players:
    print(f"{player}'s Hand: {str((playerhands[player]))}")
#functions for checking hands
def checkAJ(hand):
    if ((hand[0][0]=="A" or hand[1][0]=="A") and (hand[0][0]=="J" or hand[1][0]=="J")) and (hand[0][1] == hand[1][1]):
        if hand[0][1] == "♠":
            return "SPAJ"
        else:
            return "AJ"
    else:
        return "NoAJ"
def checkBJ(hand):
    if (checkAJ(hand)=="NoAJ") and (hand[0][0]=="A" or hand[1][0]=="A") and ((hand[0][0]=="1" or hand[1][0]=="1")or(hand[0][0]=="J" or hand[1][0]=="J")or(hand[0][0]=="Q" or hand[1][0]=="Q")or(hand[0][0]=="K" or hand[1][0]=="K")):
        return "BJ"
    else:
        return "NoBJ"
#test for checking hands
for player in players:
    print(f"{player} has: {checkAJ(playerhands[player])} {checkBJ(playerhands[player])}")
#figure out the numerical value of a given hand idk
def checkvalue(hand):
    for card in hand:
        if(card[0]=="A"):
            hand.append(card)
            hand.remove(card)
    value = 0
    for card in hand:
        if not card[0] == "A":
            value += cardvalues[card[0]]
        else:
            if value + 11 <= 21:
                value += 11
            else:
                value +=1
    return value
#print statuses
print("The dealer has:")
if(checkAJ(dealerhand)!="NoAJ") or (checkBJ(dealerhand)=="BJ"):
    print("A BLACKJACK!")
else:
    print(checkvalue(dealerhand))
for player in players[1:]:
    print(f"{player} has:")
    if(checkBJ(playerhands[player])=="BJ"):
        print("A BLACKJACK!")
    elif checkAJ(playerhands[player])=="SPAJ":
        print("A SPADE ACE-JACK!")
    elif checkAJ(playerhands[player])=="AJ":
        print("AN ACE-JACK!")
    else:
        if(playerhands[player][0][0]==playerhands[player][1][0]):
            print(str(checkvalue(playerhands[player])) + " (Splittable)")
        else:
            print(checkvalue(playerhands[player]))

dealerstatus = "active"
tatsuyastatus = "active"
eikichistatus = "active"
ginkostatus = "active"
mayastatus = "active"
yukkistatus = "active"
#game start
