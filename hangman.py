# hangman game

import sys
# a random word is generated by the program
words = ["random", "word", "generator","tool","help", "create","list","blue", "one","interested","likely", "because", "default","five", "input",
"number","type","verbs","adjective", "simply", "press" ,"button", "appear","scan","scrawl","change","goldfish","religion","disastrous","animate",
"ring","defeated","parched","ornament","star","mouth","basketball","bulb","zipper","box","hands","donkey","yellow","home","operation","station",
"building","calendar","chairs","disturbed","chunky","clever","thoughtful","undesirable","abnormal","fat","sabotage","counsel","oblige","purify",
"contradict","chicken","pink","blanket", "keyboard","lemon","brown","bear"]

#print(len(words))

# generating a random number to choose a number from the words list
import random

chosen_number = (random.randint(0,len(words)))
#print(chosen_number)
chosen_word = words[chosen_number]
print("Chosen Word:", chosen_word)
length = len(chosen_word)
print("length:", length)

# displaying the dashes for the word
dashes = []

for i in range(0,length):
    dashes.append("_")
dashes_string = " ".join(dashes)
print(dashes_string) # displays the contents of the dashes list
print("\nNow is time to guess the letters!!\nGoooooood Luuuuuuck!\n :) :) :)")

# rules
# if a letter is not a digit,
# 11 wrong guesses
guessed_letters =[]
incorrect = []
correct = []
counter = 0 #when this reaches 11 the game is over


# while loop to continue game
while True:
    if counter < 11:
        letter = input("\nEnter your guess? \nEnter a hash (#) key if you would like to end the game.\n")
        letter = letter.lower()
    #while counter < 11:
        if letter == "#":
            print("The game has now ended.\nThank you for playing!")
            break
        elif letter.isalpha() == False:
            print("This is not a valid entry")
        else:
            for i in range(0,length):
                if chosen_word[i] == letter:
                    dashes[i] = letter



                else:

                    counter += 1
            print("counter", counter)
        print(dashes)
    elif counter == 10:
        print("This is your last chance! Guess incorrectly and the game is over!")
        for i in range(0,length):
            if chosen_word[i] == letter:
                dashes[i] = letter
                print(dashes)

            else:
                print(dashes)

        counter += 1
        print("counter", counter)
    else:
        print("You have guessed incorrectly too many times :( \nThe game is now over!")
        sys.exit()

        # if letter in chosen_word == True:
        #     print("This guess was correct")
        # else:
        #     print("This letter is not present in the word")

        # check to see if the
        # if correct replace the hyphens
        # if incorrect display it also the
        #guessed_letters.append(letter.lower())
        #print("These are the letters you have guessed: ", guessed_letters)
