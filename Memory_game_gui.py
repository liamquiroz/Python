import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Memory Match Game")
root.resizable(False, False)

# Game settings
symbols = ["1","2","3","4","5","6","7","8"] * 2  # 16 cards (8 pairs)
random.shuffle(symbols)

buttons = []
flipped = []
matches = 0

# Handle card click
def on_click(i):
    global matches
    btn = buttons[i]
    if btn["text"] == "" and len(flipped) < 2:
        btn.config(text=symbols[i])
        flipped.append(i)

    if len(flipped) == 2:
        root.after(700, check_match)

# Check for match
def check_match():
    global matches, flipped
    i1, i2 = flipped
    if symbols[i1] == symbols[i2]:
        buttons[i1].config(state="disabled")
        buttons[i2].config(state="disabled")
        matches += 1
    else:
        buttons[i1].config(text="")
        buttons[i2].config(text="")
    flipped = []

    if matches == len(symbols) // 2:
        messagebox.showinfo("Game Over", "You matched all pairs!")
        reset_game()

# Reset game
def reset_game():
    global symbols, matches, flipped
    matches = 0
    flipped = []
    symbols = ["1","2","3","4","5","6","7","8"] * 2
    random.shuffle(symbols)
    for btn in buttons:
        btn.config(text="", state="normal")

# Create grid of buttons
for i in range(16):
    btn = tk.Button(root, text="", width=6, height=3, font=("Arial", 20, "bold"),
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    buttons.append(btn)

# Restart button
restart_btn = tk.Button(root, text="Restart Game", font=("Arial", 14), command=reset_game)
restart_btn.grid(row=4, column=0, columnspan=4, sticky="we", pady=10)

root.mainloop()