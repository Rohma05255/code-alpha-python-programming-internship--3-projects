#hangman game
#use random module to choose a word
import random
secret_words=["genome","protien","enzyme","plasmid","bacteria"]
secret_word=random.choice(secret_words)
guessed_letters=[]

#then to display the guessed letter use for loop
display_word=""
for letter in secret_word:
    if letter in guessed_letters:
        display_word+=letter
    else:
        display_word+="_"
#another loop to check attempts
wrong_attempts=0
max_attempts=6
while wrong_attempts<max_attempts and "_" in display_word:
    print(display_word)
    print("Wrong attempts:",wrong_attempts,"/",max_attempts)
    letter=input("Guess the letter:")
    if letter in guessed_letters:
        print("You alredy tried this letter!")
    elif letter in secret_word:
        guessed_letters.append(letter)
        print("Correct guess!")
    else:
        guessed_letters.append(letter)
        wrong_attempts+=1
        print("Wrong guess!")
    display_word=""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word+=letter
        else:
            display_word+="_"
if"_" not in display_word:
    print("Congragulations! You won! The word was:",secret_word)
else:
    print("Game over! You lost! The word was:",secret_word)