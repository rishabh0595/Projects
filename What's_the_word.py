import random
import string
import os

def whatstheword(num_guesses,score):
    letters = string.ascii_lowercase
    c = [random.choice(letters) for i in range(10)]
    d = c[random.randint(0, len(c) - 1)]
    final(num_guesses,score,d)

# To check the input
def charCheck(input_char):

    # CHECKING FOR ALPHABET
    if ((int(ord(input_char)) >= 65 and int(ord(input_char)) <= 90) or
            (int(ord(input_char)) >= 97 and int(ord(input_char)) <= 122)):
        return 0

    # CHECKING FOR DIGITS
    elif (int(ord(input_char)) >= 48 and int(ord(input_char)) <= 57):
        return 1

    # SPECIAL CHARACTER
    else:
        return 1



def final(num_guesses,score,d):

    #print("num is ",num_guesses)

    if num_guesses>5:
        print("Your Score is ", score)
        return
    print((d))

    """
    ASCII VALUE
    For capital alphabets 65 – 90
    For small alphabets 97 – 122
    For digits 48 – 57
    else- Special Characters
    """
    user_input = input("Enter valid input")
    charCheck(user_input)

    if charCheck(user_input)==0:
        pass
    else:
        print("Please enter valid character")
        score -= 20
        num_guesses += 1
        final(num_guesses, score, d)

    if user_input==d:
        print("Congratulations! your guess is correct")
        print("Your Score is ", score)
        return

    else:
        print("Please Try Again")
        score -= 20
        num_guesses += 1
        final(num_guesses,score,d)



num_guesses=1
score=100
print("Welcome to \'What's the word\' ")

print(whatstheword(num_guesses,score))

print(" Thanks for playing")