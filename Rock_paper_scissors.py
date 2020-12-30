import random

# List of possible user inputs and the inputs 'opposite'
popp = {"rock":"paper","paper":"scissors","scissors":"rock"}
poss = ["rock","paper","scissors"]

#a list of all the previous users and their scores
rating_list = []

#opens the file with the users and their scores and appends them to rating_list
rating = open('rating.txt', 'r')
for line in rating:
    rating_list.append(line)

#checks if the enetered name exists in the file and imports the score
new_user = ['placeholder']
name = input('Enter your name: ')
score = 0
x = 0
for i in rating_list:
    if i.startswith(name) == True:
        iname = int(x)
        new_user[0] = name
        i_split = i.split()
        score = int(i_split[1])
        break
    x = x + 1
rating.close()

while True:
    comp = random.choice(["rock","paper","scissors"]) #what the computer picks
    
    uin = input('Please type your action (rock,paper,scissors) or !rating for your score or !exit to exit: ') #what the user picks
    
    if uin in poss: #checks if the user input is valid
        if comp == popp[uin]: #the computer won
            print("Sorry, but computer chose",comp)
            score = score + 0
        elif comp == uin: #the computer and the hman chose the same action
            print("There is a draw ("+comp+")")
            score = score + 50
        else: #the user won
            print("Well done. Computer chose",comp,"and failed")
            score = score + 100
    
    elif uin == "!exit":
        print("Bye!")
        
        rating = open('rating.txt', 'w')
        
        #first checks if the user is old or new, if old, it just updates the score otherwise it creates a new entry
        if new_user[0] == name:
            rating_list[int(iname)] = name+' '+str(score)+'\n'
            rating.writelines(rating_list)
        
        else:
            rating_list.append(name+' '+str(score)+'\n')
            rating.writelines(rating_list)
        rating.close()
        break
    
    elif uin == "!rating": #shows the user his/her current rating
        print('Your rating:',str(score))
    
    else:
        print("Invalid input")
        pass
    
