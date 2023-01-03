# -*- coding: utf-8 -*-
"""
Stein
Saks
Papir

Sander Kaupang
"""

import random as rm 
import colorama
import sys
print ("Hei og velkommen til Stein, Saks, Papir. Vi spiller for best av 5!")

game = True 

# Holder oversikt over poeng
computerScore = 0
userScore = 0


#coloer green om bruker vinner
userWon = colorama.Fore.GREEN + "User won"
#color red om computer vinner
computerWon = colorama.Fore.RED + "Computer won"
#color yellow om det er uavgjort
tie = colorama.Fore.BLUE + "Uavgjort"
#reset color
resetColor = colorama.Fore.WHITE + "\n play again ? (y/n) :"
# Bruker gir ugyldig verdi 
error = "feil verdi, vil du prøve på nytt ? (y/n) : "

i = 0


while game:

#liste med muligheter av valg.
    guessList = ["saks", "papir" , "stein"]
    computerGuess = rm.choice(guessList)
    
#bruker's gjett 
    userGuess = input("\nstein, saks, papir :")
    
#sjekker for ugyldige verdier
    while userGuess not in guessList: # om gjettet ikke er i listen vil denne slå inn
        print("ERROR, ugyldig verdi")
        
        play_again = input(error) # spørr om spiller vil prøve å gjette på nytt
        
        if play_again.lower() != "y":
            sys.exit()  # avslutter spillet
        else:
            break # hopper ut av while løkka for og fortsette spillet
        
        
#uavgjort
    if (computerGuess == userGuess):
        print (tie)
        print (colorama.Fore.WHITE + "\ncomputer guess:", computerGuess)
        print ("user guess:", userGuess)
        

#computer vinner
    elif (computerGuess == "saks" and userGuess == "papir"):
        print (computerWon)
        print (colorama.Fore.WHITE + "\ncomputer guess:", computerGuess)
        print ("user guess:", userGuess)
        
    
    elif (computerGuess == "papir" and userGuess == "stein"):
        print (computerWon)
        print (colorama.Fore.WHITE + "\ncomputer guess:", computerGuess)
        print ("user guess:", userGuess)
        
    
    elif (computerGuess == "stein" and userGuess == "saks"):
        print (computerWon)
        print (colorama.Fore.WHITE + "\ncomputer guess:", computerGuess)
        print ("user guess:", userGuess)
        
    
# bruker vinner
    elif (userGuess in guessList):
        print (userWon);
        print (colorama.Fore.WHITE + "computer guess:", computerGuess)
        print ("user guess:", userGuess)
   
    else: 
        continue
    '''
    om bruker har skrevet en ugyldig verdi og vil forstett og spille 
    vil else starte koden på nytt. 
    om ikke vil sys.exit() avslutte koden
    '''
        
    
# ser om bruker vil spille mer. 
    play_again = input(resetColor) 
    if play_again.lower() != "y":
        break



