#Mam before you check the code i want you to know that i got the idea of this code from internet as it was new for me.I hope it is fine.

import random
print('Number guessing game')
number=random.randint(1,9)
chances=0
print('Guess a number (between 1 and 9)')
while chances <5:
    guess=int(input('enter your guess:-'))
    if guess==number:
        print('Congratulation YOU WON!!!')
        break
    elif guess<number:
        print('Your guess was too low: Guess a number higher than',guess)
    else:
        print('Your guess was too high,Guess a number lower than',guess)
    chances+=1

if not chances<5:
    print('You lose!! the number is ',number)