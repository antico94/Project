import random
import time
import sys
def play(word, lives):

    print("_"*len(word))
    list=[]
    list2=[]
    list3=[]
    numar=0

    for letter in word:
        list.append(letter.lower())
        list2.append("_")

    print("You got " +str(lives)+ " lives left!")
    guess=input("Please enter your first guess: ").lower()
    while lives>0:
        if guess in list:
            if guess in list2:
                print("You have already inserted the letter " + str(guess) + " before.")
                guess = input("Please enter another guess: ").lower()

            elif list.count(guess.lower())>=1:
                for numar in range(len(word)):
                    if list[numar]==guess.lower():
                        list2.pop(numar)
                        list2.insert(numar,guess.lower())
                        numar+=1

                if "_" not in list2:
                    print("Congrulations! The word was " + word + "!")
                    break
                print("".join(list2))
                guess = input("Please enter another guess: ").lower()


        else:
            if guess == "quit":
                print("Good Bye!")
                break
            print("The letter "+str(guess)+ " is not the word.")
            if guess.lower()  not in list3:
                lives-=1
                print(pics(lives))
                print("You got "+ str(lives) + " lives left.")
                if lives==0:
                    print(("    Game Over!"))
                    print("The word was "+word+" .")
                    break

                list3.append(guess.lower())
                print("The list with all the wrong letters inserted is bellow:")
                print(",".join(list3))
                guess = input("Please enter another guess: ").lower()
            else:
                print("You have already inserted the letter "+ str(guess)+ " before.")
                print("The list with all the wrong letters inserted is bellow:")
                print(",".join(list3))
                guess = input("Please enter another guess: ").lower()

def pics(parameter):
    pics = ['''

      +---+
      |   |
          |
          |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    return pics[(6-parameter)]

def random_words(x):
    text = open("/home/user/PycharmProjects/Hangman/countries-and-capitals.txt", "r")
    country = []
    capital = []
    for el in text.readlines():
        country_and_capitals = el.split("|")
        country.append(country_and_capitals[0].strip())
        capital.append(country_and_capitals[1].strip())
    word = random.choice(country+capital)
    while len(word)>5*(int(x)):
        word = random.choice(country + capital)
    return word

def dificulty(number):
    if number == "1":
        print("The topic of the word is Countries and Capitals.")
        return play(random_words(number),7)
    if number == "2":
        print("The topic of the word is Countries and Capitals.")
        return play(random_words(number),3)
    if number == "3":
        print("The topic of the word is Countries and Capitals.")
        return play(random_words(number),2)
    if number == "4":
        print("¯\_(ツ)_/¯")
        return play(random_words(number),1)

def mode():
    print("Please select the mode:")
    print("1. Player vs Player (Player 1 sets the word and the amount of lifes for Player 2)")
    print("2. AI vs Player (AI sets the word and the player will choose the difficulty)")
    choice=""
    choice=input("Your choice: ")
    if choice=="1":
        try:
            print("You have chosen Player vs Player.")
            play(input("Enter the secret word: "),int(input("\nChoose the amount of lives: ")))
        except ValueError as err:
            print("The game will now restart!")
            print("Please enter a valid number for lives this time!")
            for i in range(3):
                print("The game will restart in " + str(3-i) + ".")
                time.sleep(1)
            mode()
    elif choice=="2":
        print("You have chosen AI vs Player")
        dificulty(input("Please select the dificulty:\n1.Easy\n2.Normal\n3.Hard\n4.Hardcore\nYour choice: "))



    elif choice== "quit":
        for i in range(3):
            print("The game will exit in " + str(3 - i) + ".")
            time.sleep(1)
        print("Good Bye!")
        sys.exit()

    else:
        print("Please enter a valid number this time!")
        for i in range(3):
            print("The game will restart in " + str(3 - i) + ".")
            time.sleep(1)
        mode()





mode()











