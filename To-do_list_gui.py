import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30, font="Arial 14")
entry.pack(side="left", padx=5)

add_btn = tk.Button(frame, text="Add", command=add_task)
add_btn.pack(side="left")

listbox = tk.Listbox(root, width=40, height=10, font="Arial 14")
listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete", command=delete_task)
delete_btn.pack()

root.mainloop()