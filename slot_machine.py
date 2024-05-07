
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
#check the results of the bet
def check_winnings(columns,lines,bet,values):
    winning_lines = []
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #creating a copy of the list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

#reverse the form of the slots
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row],end=" | ") #printing at the same line
            else:
                print(column[row],end="  ")#printing at the same line
        print() #jump to next line after printing the 3 spots
#deposit on the balance
def deposit():
    while True:
            amount = input("What would you like to deposit? $")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("Amount must be greater than 0")
            else:
                print("Please enter a number")
    return amount
#recive the number of the lines the user will bet
def get_numbers_of_lines():
    while True:
            lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Enter a valid number of lines")
            else:
                print("Please enter a number")
    return lines
#get the price of each bet
def get_bet():
    while True:
        bet = input("What would you like to bet on each bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET<= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return bet
#operates the game
def game(balance):
    lines = get_numbers_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount , your current amount is: ${balance}")
        else:
            break
    print(f"You're betting ${bet} on {lines} lines. Total be is equal to ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings} \n")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is: ${balance}")
        spin = input("Press enter to spin! (q to quit) ")
        if spin.lower() == "q":
            break
        else:
            balance +=  game(balance)
    print(f"You left with the balance of: {balance}")


main()