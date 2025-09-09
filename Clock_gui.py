import tkinter as tk
import time

# Function to update the clock every second
def update_time():
    current_time = time.strftime("%H:%M:%S")  # 24-hour format
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1 second

# Create window
root = tk.Tk()
root.title("Digital Clock")

# Create label
label = tk.Label(root, font=("Arial", 48), background="black", foreground="cyan")
label.pack(anchor="center")

# Start clock
update_time()

# Run application
root.mainloop()