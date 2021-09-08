
import random
import string
import sys

file = open('C:\_dev\GitHub\Hangman\words.txt', 'r')
words = file.read().split('\n')
file.close()

random = random.randint(1, 200)+1
word = list(words[random])      #randomly generated word
tempword = list(word)
available = string.ascii_lowercase
guess = []     #the word the player is building'
tries = 10
for i in range(len(word)):
    guess.append("_")
print('\n' + words[random] + '\n')

""" #uncomment to enable user difficulty setting
diff = ''
while True:
    break
    if diff == 'e':
        tries = 15
        break
    elif diff == 'm':
        tries = 10
        break
    elif diff == 'h':
        tries = 5
        break
    else:
        diff = str(input("\nHow difficult would you like this to be? (e/m/h) "))
"""

while True:
    print("Length: " + str(len(word)))
    print("Available: " + available)
    print("Tries Left: " + str(tries))
    tempguess = ""
    for letter in guess:
        tempguess = tempguess + letter
    print(tempguess)
    letter = input("Choose a letter: ")
    available = available.replace(letter, '')

    indicies = []
    ind = 0
    for i in range(len(word)):
        if word[i] == letter:
            indicies.append(i)

    if letter in word:
        for item in word:
            if letter == item:
                index = word.index(letter)               
                if not indicies:
                    guess[index] = letter
                else:
                    guess[indicies[ind]] = letter
                    ind = ind+1
                for i in guess:
                    i.replace(' ', '')
                    
                    if guess == word:
                        print("You win!")
                        sys.exit()
    else:
        tries = tries-1
        if tries == 0:
            print("Game Over!")
            break
    print("----------------------------------------------\n\n\n")
