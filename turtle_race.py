# creating a graphical aplication for turtle race
import turtle 
import time
import random
import tkinter as tk

WIDTH,HEIGHT = 500,500
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "dark gray"]
FINAL_LINE_Y = HEIGHT // 2 - 20

def get_number_of_racers():
     while True:
        racers = tk.simpledialog.askinteger("Number of Racers", "Enter the number of racers (2 - 10): ")
        if racers is None:
            return  # If user cancels, return None
        if 2 <= racers <= 10:
            return racers
        else:
            tk.messagebox.showerror("Invalid Number", "Please enter a number between 2 to 10.")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing!")

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            x,y = racer.pos()
            #checking if the turtle has reached the finish line
            if y >= FINAL_LINE_Y:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    x,y = WIDTH//(len(colors)+1),-HEIGHT//2+20
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.speed(3)
        racer.shape("turtle")
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * x,y)#set the position of the turtle
        racer.pendown()
        turtles.append(racer)
    return turtles
   
def select_bet(colors):
    root = tk.Tk()
    root.title("Select Your Bet")
    bet_color = tk.StringVar(root)
    bet_color.set("Select a color")
    drop = tk.OptionMenu(root, bet_color, *colors)
    drop.pack()
    confirm_button = tk.Button(root, text="Confirm Bet", command=root.quit)
    confirm_button.pack()
    root.mainloop()
    root.destroy()  # Destroying the window after selection
    return bet_color.get()

def draw_final_line(y):
    final_line = turtle.Turtle()
    final_line.speed(0)
    final_line.penup()
    final_line.goto(-WIDTH // 2, y)
    final_line.pendown()
    final_line.setheading(0)  # Ensure the turtle is facing right
    # Draw the line
    final_line.forward(WIDTH)
    # Draw squares along the line
    square_size = 20
    num_squares = WIDTH // (2 * square_size)  # Adjust for the distance between squares
    # Desenha a linha de chegada
    for _ in range(16):  # Desenha 16 traços para a linha de chegada
        final_line.forward(30)  # Comprimento de cada traço
        final_line.penup()
        final_line.forward(10)  # Espaçamento entre os traços
        final_line.pendown()
     

    final_line.hideturtle()


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
draw_final_line(FINAL_LINE_Y)

colors = COLORS[:racers] #slide te list acording with the quantity of racers
bet = select_bet(colors)
winner = race(colors)

if winner == bet:
    tk.messagebox.showinfo("Result", f"Congratulations! Your bet was the {winner}. You won!")
else:
    tk.messagebox.showinfo("Result", f"Unfortunately, your bet {bet} didn't win. Better luck next time!")

time.sleep(5)
