#Matthew Wood
#Woodmatthewj522@aol.com
#This is one of my first python programs, thank you for playing!

import random
import time

#Define "rules" function
#Print statement to display rules to user

def rules():
    rule = print("""          You will be given two cards to start, and the total of your cards
          will be displayed to you. Your goal is to get as close to 21 as you
          can without going over 21. You will be pressing "1" to stay, at which point your
          turn is finished, and your opponent will have their turn to go. You will press "2" 
          if you would like to "hit", at which point you will be given another card to add to
          your total. If at any point you or your opponents total goes above 21, referred to as 
          a "bust", this is considered an automatic loss. If neither players total is above 21,
          and you both have chosen to "stay", the player with the highest total wins! If you win
          the game, the payout for your bet will be double the amount you put in!""")
    time.sleep(1)
    return rule

#Define "bet" function
#Prompt user for input (amount they want to "bet")

def bet():
    time.sleep(1)
    print("\nYou may bet between $50 - $10,000\n")
    time.sleep(1)

    #Indefinite iteration 
    #loop ends when user input is > 50 and <= 10000

    while True:
        usr_bet = input("How much would you like to bet?\n")
        if usr_bet.isdigit():
            usr_bet = int(usr_bet)
            if usr_bet >= 50 and usr_bet <= 10000:
                break
            else:
                print("\nPlease enter an amount between $50 - $10,000\n")
        else:
            print("Please enter a valid number between $50 - $10,000\n")

    return usr_bet

#Game function

def game():

    #List of "cards" in deck

    deck = [2, 2, 2, 2, 3, 3, 3, 3,
            4, 4, 4, 4, 5, 5, 5, 5,
            6, 6, 6, 6, 7, 7, 7, 7,
            8, 8, 8, 8, 9, 9, 9, 9,
            10, 10, 10, 10, 11, 11, 11, 11]

    print("Shuffling")
    time.sleep(.5)
    print("...")
    time.sleep(.5)
    print("...")
    time.sleep(.5)
    print("...")
    time.sleep(.5)

    # pulls 2 random elements from list "deck" for dealer
    # removes chosen elements from list "deck"

    dealer1 = random.choice(deck)
    deck.remove(dealer1)
    dealer2 = random.choice(deck)
    deck.remove(dealer2)
    dealer_total = dealer1 + dealer2

    #pulls 2 random elements from list "deck" for user
    #removes chosen elements from list "deck"
    #Assigns elements pulled from list to user "total"

    time.sleep(.5)
    x = random.choice(deck)
    print("Your first card is: ", x)
    deck.remove(x)
    time.sleep(1)
    y = random.choice(deck)
    print("Your second card is: ", y)
    deck.remove(y)
    time.sleep(1)
    total = (x + y)
    print("Your total is: ", total)
    time.sleep(2)

    #User indefinite iteration
    #Loop will continue until user inputs "1" to "stay" or if total > 21

    while True:

        #Establish parameters for user input - input must be numerical - "1" or "2"
        
        answer = input("\nWould you like to stay (1) or hit (2)? \n")
        if answer.isdigit():
            answer = int(answer)
            
            #User input conditions
            #If user input == 1 - begin while loop for automated opponent turn

            if answer == 1:
                time.sleep(1)
                
                #Indefinite iteration for automated opponent
                #Loop will continue until dealer_total is > 16 and < 21
                #Assigns elements pulled from list to "dealer_total"

                while True:
                    if dealer_total < 16:
                        print("dealer has chosen to hit!")
                        dealer_draw = random.choice(deck)
                        deck.remove(dealer_draw)
                        dealer_total = dealer_total + dealer_draw
                        time.sleep(1)
                    elif dealer_total > 21:
                        print("Dealer busted! You win!!")
                        time.sleep(1)
                        break
                    else:
                        print("Dealer has chosen to stay")
                        break
                print("\nThe dealers total was: ", dealer_total, "\nYour total was: ", total)
                
                #Establish winner - total/dealer_total comparison
                #If user wins - continue main function - otherwise terminate application

                if total > dealer_total:
                    time.sleep(1)
                    print("You win!\n")
                    time.sleep(1)
                    break
                elif total < dealer_total:
                    print("You lost! Better luck next time!\n")
                    time.sleep(1)
                    exit()
                elif total == dealer_total:
                    print("It's a tie! There are no winners this round.\n")
                    exit()
                else:
                    print("Error")
                    exit()

            #User input conditions
            #If user input == 2 - pull element from list - remove chosen element from list
            #assign element to user "total"

            elif answer == 2:
                hit1 = random.choice(deck)
                deck.remove(hit1)
                total = hit1 + total
                time.sleep(1)
                print("\nYour next card is: ", hit1)
                time.sleep(1)
                print("Your new total is: ", total)
                if total > 21:
                    print("\nBust! Better luck next time! ")
                    exit()
            else:
                print("\nPlease enter (1) to hold, or (2) to hit")

#Define main function

def main():

    #Display welcome message

    print("\nWelcome to BlackJack and thank you for playing!\n")
    time.sleep(2)

    #Indefinite iteration prompting for user input
    #Loop ends when user input == 1 to display rules, or == 2 to skip rules and play

    while True:
        usr_prompt = input("""Before we begin, would you like to read the rules (1)?
Or skip (2) and play?\n""")
        if usr_prompt.isdigit():
            usr_prompt = int(usr_prompt)
            if usr_prompt == 1:
                rule = rules()
                time.sleep(6)
                break
            elif usr_prompt == 2:
                break
            else:
                print("Please enter (1) to read the rules, or (2) to skip and play!\n")
                time.sleep(1)
        else:
            print("\nPlease enter (1) to read the rules, or (2) to skip and play!\n")
            time.sleep(1)

    #call functions

    usr_bet = bet()
    time.sleep(1)
    game()

    #If user "wins", multiply "bet" * 2
    
    usr_win = int(usr_bet * 2)
    
    #Display users "winnings"

    time.sleep(1)
    print("Your total winnings: ", usr_win)
    print("\nCongratulations!")
    time.sleep(3)
    
    #If user wins, display funny message!

    print("\nPlease insert 25 cents to play again!")
    time.sleep(2)
    print("\nJust joking of course! Thanks again for playing!\n")

main()