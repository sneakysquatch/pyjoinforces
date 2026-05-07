#import
import random
#declare variables ahead of time for cleanness
juckport = 10000
dealerbet = 5
tatsuyabet = 0
eikichibet = 0
ginkobet = 0
mayabet = 0
yukkibet = 0
dealerpayout = 0
tatsuyapayout = 0
eikichipayout = 0
ginkopayout = 0
mayapayout = 0
yukkipayout = 0
dealerstatus = "active"
tatsuyastatus = "active"
eikichistatus = "active"
ginkostatus = "active"
mayastatus = "active"
yukkistatus = "active"
unshuffled = []
shuffled = []
dealerhand = []
tatsuyahand = []
eikichihand = []
ginkohand = []
mayahand = []
yukkihand = []
dealermove = None
tatsuyamove = None
eikichimove = None
ginkomove = None
mayamove = None
yukkimove = None
cardvalues = {"1":10,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
players = ["Dealer", "Tatsuya", "Eikichi", "Ginko", "Maya", "Yukki"]
playerhands = {"Dealer":dealerhand, "Tatsuya": tatsuyahand, "Eikichi": eikichihand, "Ginko": ginkohand, "Maya": mayahand, "Yukki": yukkihand}
playerstatus = {"Dealer":dealerstatus, "Tatsuya": tatsuyastatus, "Eikichi": eikichistatus, "Ginko": ginkostatus, "Maya": mayastatus, "Yukki": yukkistatus}
playermove = {"Dealer":dealermove, "Tatsuya": tatsuyamove, "Eikichi": eikichimove, "Ginko": ginkomove, "Maya": mayamove, "Yukki": yukkimove}
playerpayouts = {"Dealer":dealerpayout, "Tatsuya": tatsuyapayout, "Eikichi": eikichipayout, "Ginko": ginkopayout, "Maya": mayapayout, "Yukki": yukkipayout}
suits = ["♠","♥","♣","♦"]
dealersoft = "Hard"
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
playerbets = {"Dealer":dealerbet, "Tatsuya": tatsuyabet, "Eikichi": eikichibet, "Ginko": ginkobet, "Maya": mayabet, "Yukki": yukkibet}
for player in players:
    if playerbets[player]!=0:
        playerhands[player].append(shuffled[0])
        shuffled.pop(0)
        playerhands[player].append(shuffled[0])
        shuffled.pop(0)
print(f"Dealer's first card is: {dealerhand[0]}")
for player in players[1:]:
    if playerbets[player]!=0:
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
#for player in players:
#    print(f"{player} has: {checkAJ(playerhands[player])} {checkBJ(playerhands[player])}")
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
                if(hand == dealerhand):
                    dealersoft = "soft"
            else:
                value +=1
    return value
#print statuses
for player in players[1:]:
    if playerbets[player]!=0:
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
#define special hand checkers
def issixcards(hand):
    return len(hand)==6
def issevencards(hand):
    return len(hand)==7
def istripleseven(hand):
    if len(hand)==3:
        return all([hand[0][0]==7, hand[1][0]==7, hand[2][0]==7])
def isjuckport(hand):
    if len(hand)==6:
        return ((any([hand[0][0]=="A",hand[1][0]=="A",hand[2][0]=="A",hand[3][0]=="A",hand[4][0]=="A",hand[5][0]=="A"])) and (any([hand[0][0]=="2",hand[1][0]=="2",hand[2][0]=="2",hand[3][0]=="2",hand[4][0]=="2",hand[5][0]=="2"])) and (any([hand[0][0]=="3",hand[1][0]=="3",hand[2][0]=="3",hand[3][0]=="3",hand[4][0]=="3",hand[5][0]=="3"])) and (any([hand[0][0]=="4",hand[1][0]=="4",hand[2][0]=="4",hand[3][0]=="4",hand[4][0]=="4",hand[5][0]=="4"])) and (any([hand[0][0]=="5",hand[1][0]=="5",hand[2][0]=="5",hand[3][0]=="5",hand[4][0]=="5",hand[5][0]=="5"])) and (any([hand[0][0]=="6",hand[1][0]=="6",hand[2][0]=="6",hand[3][0]=="6",hand[4][0]=="6",hand[5][0]=="6"])))
#game start
playerstatus.pop("Dealer")
while "active" in playerstatus.values():
    for player in players[1:]:
        if playerbets[player] == 0:
            playerstatus[player] = "inactive"
        while playerstatus[player] == "active":
            if checkvalue(playerhands[player])>21:
                print(f"{player} busted")
                playerstatus[player] = "bust"
            elif checkAJ(playerhands[player]) == "SPAJ":
                print(f"{player} has a spade ace-jack. Standing")
                playerstatus[player] = "SPAJ"
            elif checkAJ(playerhands[player]) == "AJ":
                print(f"{player} has an ace-jack. Standing.")
                playerstatus[player] = "AJ"
            elif checkBJ(playerhands[player]) == "BJ":
                print(f"{player} has a blackjack. Standing.")
                playerstatus[player] = "BJ"
            elif issevencards(playerhands[player]):
                print(f"{player} has seven cards. Standing.")
                playerstatus[player] = "tripleseven"
            elif len(playerhands[player]) == 2:
                if playerstatus[player] == "active" and not (playerhands[player][0][0]==playerhands[player][1][0]):
                    print(f"{player} has {playerhands[player]} with value {checkvalue(playerhands[player])}. Choose X to hit, O to stand, or T to double down.")
                    while True:
                        playermove[player] = input()
                        if playermove[player].upper() in ("X","O","T"):
                            break
                        print("Please input a single letter corresponding to a valid command.")
                    if playermove[player].upper() == "X":
                        playerhands[player].append(shuffled[0])
                        shuffled.pop(0)
                        print(f"{player} now has {playerhands[player]} with value {checkvalue(playerhands[player])}.")
                    if playermove[player].upper() == "O":
                        playerstatus[player]= "stand"
                    if playermove[player].upper() == "T":
                        playerbets[player]*=2
                        playerhands[player].append(shuffled[0])
                        shuffled.pop(0)
                        if checkvalue(playerhands[player])>21:
                            print(f"{player} busted")
                            playerstatus[player] = "bust"
                        else:
                            playerstatus[player] = "stand"
                elif playerstatus[player] == "active" and (playerhands[player][0][0]==playerhands[player][1][0]):
                    print(f"{player} has {playerhands[player]} with value {checkvalue(playerhands[player])}. Choose X to hit, O to stand, S to split, or T to double down.")
                    while True:
                        playermove[player] = input()
                        if playermove[player].upper() in ("X","O","T","S"):
                            break
                        print("Please input a single letter corresponding to a valid command.")
                    if playermove[player].upper() == "X":
                        playerhands[player].append(shuffled[0])
                        shuffled.pop(0)
                        print(f"{player} now has {playerhands[player]} with value {checkvalue(playerhands[player])}.")
                    if playermove[player].upper() == "O":
                        playerstatus[player]= "stand"
                    if playermove[player].upper() == "T":
                        playerbets[player]*=2
                        playerhands[player].append(shuffled[0])
                        shuffled.pop(0)
                    if playermove[player].upper() == "S":
                        #split is a wip
                        pass
            elif playerstatus[player] == "active":
                print(f"{player} has {playerhands[player]} with value {checkvalue(playerhands[player])}. Choose X to hit or O to stand.")
                while True:
                    playermove[player] = input()
                    if playermove[player].upper() in ("X","O"):
                        break
                    print("Please input a single letter corresponding to a valid command.")
                if playermove[player].upper() == "X":
                        playerhands[player].append(shuffled[0])
                        shuffled.pop(0)
                        print(f"{player} now has {playerhands[player]} with value {checkvalue(playerhands[player])}.")
                if playermove[player].upper() == "O":
                        playerstatus[player]= "stand"
playerstatus.update({"Dealer":dealerstatus})
while(dealerstatus == "active"):
    if(checkvalue(dealerhand))>21:
        dealerstatus = "bust"
        print(f"Dealer busted with {checkvalue(dealerhand)} and cards {dealerhand}.")
    elif(checkvalue(dealerhand))<17:
        dealerhand.append(shuffled[0])
        shuffled.pop(0)
    elif checkvalue(dealerhand)==17 and dealersoft == "Soft":
            dealerhand.append(shuffled[0])
            shuffled.pop(0)
    elif any([checkBJ(dealerhand)=="BJ",checkAJ(dealerhand)=="AJ",checkAJ(dealerhand)=="SPAJ"]):
        dealerstatus = "BJ"
        print("Dealer has blackjack.")
    else:
        dealerstatus = "stand"
        print(f"Dealer stands on {checkvalue(dealerhand)} with cards {dealerhand}.")
#scoring?
for player in players[1:]:
    if isjuckport(playerhands[player]):
        if playerbets[player] > 9:
            playerpayouts[player] = juckport
        else:
            playerpayouts[player] = playerbets[player] * 1 #replace 1 with juckport mult please
    elif istripleseven(playerhands[player]) or checkAJ(playerhands[player]) == "SPAJ":
        playerpayouts[player] = playerbets[player]*100
    elif issevencards(playerhands[player]) or checkAJ(playerhands[player])=="AJ":
        playerpayouts[player] = playerbets[player]*50
    elif issixcards(playerhands[player]):
        playerpayouts[player] = playerbets[player]*20
    elif checkBJ(playerhands[player]) == "BJ":
        if dealerstatus != "BJ":
            playerpayouts[player] = playerbets[player]*3
        else:
            playerpayouts[player] = playerbets[player]
    elif dealerstatus == "BJ":
        playerpayouts[player] = 0
    elif playerstatus[player] == "bust":
        playerpayouts[player] = 0
    elif dealerstatus == "bust":
        playerpayouts[player] = playerbets[player]*2
    elif checkvalue(playerhands[player]) > checkvalue(dealerhand):
        playerpayouts[player] = playerbets[player]*2
    elif checkvalue(playerhands[player]) == checkvalue(dealerhand):
        playerpayouts[player] = playerbets[player]
    else:
        playerpayouts[player] = 0
    #test payouts
for player in players[1:]:
    print(f"{player} wins {playerpayouts[player]} chips.")
