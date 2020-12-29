import random

print('H A N G M A N')

glet = [] # stores guessed letters
guess = random.choice(['engineering','software']) #the word which is chosen for guessing
hyphen_word = list("-"*len(guess)) # the ciphered word
list_word = list(guess) #the word to be guessed in list form

while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    
    if menu == "play": #start the game
        x= 9
        
        while x>1: #run until the user runs out of tries
            if "".join(hyphen_word) == guess: #the user has guessed all of the letters
                print('You guessed the word '+"".join(hyphen_word)+'!')
                print("You survived!")
                break
            print("")
            print("".join(hyphen_word))
            
            let = input("Input a letter: ") #asks the user to input a letter to be guessed
            lower_let = let.lower()
            
            if len(let) == 1: #checks if the user inputted one letter    
                if let.isalpha() and let == lower_let: #checks if the user inputted an alhpabet
                    if lower_let in glet: #checks if the user has laready guessed the character
                            print("You already typed this letter")
                    else:
                        if guess.find(lower_let) == -1: #removes a life if the user guesses wrong
                            print("No such letter in the word")
                            glet.append(lower_let)
                            x=x-1
                        else: #finds which hyphens from the string to replace with a letter if the user guesses right
                            glet.append(lower_let)
                            for i in range(len(list_word)):
                                if list_word[i] == lower_let:
                                    hyphen_word[i] = lower_let
                else:
                    print("It is not an ASCII lowercase letter")
                if x == 1: #the user has run out of lives
                    print("You are hanged!")
                    break
            else:
                print("You should input a single letter")
    elif menu == "exit":
        break
        
