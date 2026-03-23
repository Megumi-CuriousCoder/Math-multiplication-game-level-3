import random
import time

print('~Math multiplication game~  level 3')
name = input("Your name: ")

score = 0
for number in range(1, 6):
    number1 = random.randint(5, 13)
    number2 = random.randint(5, 13)
    right_answer = number1 * number2
   
    print(f'Operation Number {number}: How many {number1} * {number2}?')
   
   
    start_time = time.time()
   


    answer = 0
    while answer != right_answer:
        try:
            answer = int(input('Your answer:'))
           
            end_time = time.time()
            duration = end_time - start_time
           
            if answer == right_answer:
                if duration <= 5:
                    print('You right!')
                    score = score + 20
                elif duration <= 10:
                    print('Correct! But try faster!')
                    score = score + 15
                else:
                    print('Correct! But try faster!')
                    score = score + 10
            else:
                print('You lose!   -try again-')
                score = score - 20
        except ValueError:
            print('Please use number')
           
print('~Hurraay...  you finished all the operations!')

print(f"Your score is {score}!")



print('Thanks for learning!')
print(f'Hope you be smarter, {name}!')
