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
    unshuffled.append(item+"A")
    shuffled.append(item+"A")
    for i in range(2,11):
        unshuffled.append(item+str(i))
        shuffled.append(item+str(i))
    for face in ["J","Q","K"]:
        unshuffled.append(item+face)
        shuffled.append(item+face)
random.shuffle(shuffled)
print(unshuffled)
print(shuffled)
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
