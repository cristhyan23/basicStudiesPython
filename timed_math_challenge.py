""""
Generate a banch of random math questions ask them to the user and do not close the app until they answer it correctly
and take the time user's takes to answering
"""

import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generat_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = str(left) +" "+ operator +" "+str(right)
    answer = eval(expr) #calculates math based on strings
    return expr, answer

wrong = 0

input("Press Enter to start!")
print("------------------------------")
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr,answer = generat_problem()
    right_answer = False
    while not right_answer:
        try:
            user_reply = int(input(f"Problem #{i+1}: {expr} answer =  "))
        except ValueError:
            print("Please only type numbers!")
        if user_reply == answer:
            print("Congrats , you're right!")
            right_answer = True
        else:
            print("Oh no! you've missed it!")
            wrong+=1

end_time = time.time()
total_time = end_time - start_time

print("------------------------------")
print("Nice Work!")
print(f"It took you {total_time:.2f} secs to solve it")
print(f"Accuracy: {((TOTAL_PROBLEMS-wrong)/TOTAL_PROBLEMS)*100:.2f}%")
