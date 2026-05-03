#import, pygame is unused for now but will be used to add graphics later
import random
import pygame
#declare variables ahead of time for cleanness
unshuffled = []
shuffled = []
dealerhand = []
tatsuyahand = []
eikichihand = []
ginkohand = []
mayahand = []
yukkihand = []
cardvalues = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"J":10,"Q":10,"K":10}
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
for hand in [dealerhand, tatsuyahand, eikichihand, ginkohand, mayahand, yukkihand]:
    hand.append(shuffled[0])
    shuffled.pop(0)
    hand.append(shuffled[0])
    shuffled.pop(0)
print("Dealer's Hand: "+str(dealerhand))
print("Tatsuya's Hand: "+str(tatsuyahand))
print("Eikichi's Hand: "+str(eikichihand))
print("Ginko's Hand: "+str(ginkohand))
print("Maya's Hand: "+str(mayahand))
print("Yukki's Hand: "+str(yukkihand))
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
    if (checkAJ(hand)=="NoAJ") and (hand[0][0]=="A" or hand[1][0]=="A") and ((hand[0][0]==10 or hand[1][0]==10)or(hand[0][0]=="J" or hand[1][0]=="J")or(hand[0][0]=="Q" or hand[1][0]=="Q")or(hand[0][0]=="K" or hand[1][0]=="K")):
        return "BJ"
    else:
        return "NoBJ"
#test for checking hands
print("Dealer has: " +checkAJ(dealerhand)+" "+checkBJ(dealerhand))
print("Tatsuya has: "+checkAJ(tatsuyahand)+" "+checkBJ(tatsuyahand))
print("Eikichi has: "+checkAJ(eikichihand)+" "+checkBJ(eikichihand))
print("Ginko has: "  +checkAJ(ginkohand)+" "+checkBJ(ginkohand))
print("Maya has: "   +checkAJ(mayahand)+" "+checkBJ(mayahand))
print("Yukki has: "  +checkAJ(yukkihand)+" "+checkBJ(yukkihand))
#figure out the numerical value of a given hand idk
def checkvalue(hand):
    pass
#print dealer status
print("The dealer has:")
if(checkAJ(dealerhand)!="NoAJ") or (checkBJ(dealerhand)=="BJ"):
    print("A BLACKJACK!")
else:
    print(checkvalue(dealerhand))