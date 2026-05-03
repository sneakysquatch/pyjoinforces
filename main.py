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
    if bet > -1 and bet < 11:
        return True
    else:
        return False
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