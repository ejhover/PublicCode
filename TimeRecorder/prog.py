from tkinter import *
root = Tk()

root.title('Emmet TA Time Manager')
root.geometry("400x400")
with open("time.txt", "r") as time:
    txt = time.read()
    hours,mins = map(int, txt.split())
def upClick():
    global hours
    global mins
    if mins+5>59:
        hours+=1
        mins=5-(60-mins)
    else:
        mins+=5
    displayed_time["text"] = f'{hours : 03d}:{mins: 03d} hrs:min'
    with open("time.txt", "w") as time:
        time.write(f'{hours} {mins}')
def downClick():
    global hours
    global mins
    if mins-5<0:
        hours-=1
        mins=60-(5-mins)
    else:
        mins-=5
    displayed_time["text"] = f'{hours : 03d}:{mins: 03d} hrs:min'
    with open("time.txt", "w") as time:
        time.write(f'{hours} {mins}')
def enter():
    l = Label(root, text=e.get())
    with open("activities.txt", "a") as f:
        f.write(f'{e.get()} ')
    e.delete(0, 'end')
    l.pack(pady=1)
displayed_time = Label(root, text=f'{hours : 03d}:{mins: 03d} hrs:min', font=("Times", 30))
displayed_time.pack(padx=10, pady=10)
upButton = Button(root, text="Up", command=upClick)
upButton.pack(padx=5, pady=5)
downButton = Button(root, text="Down", padx=5, pady=5, command=downClick)
downButton.pack(padx=5, pady=5)
e = Entry(root, width=40, font=("Times", 20))
e.pack(padx=15, pady=10)
enterButton = Button(root, text="Enter", command=enter)
enterButton.pack(padx=5, pady=5)
with open("activities.txt", "r") as f:
    txt = f.read()
    activities = txt.split("  ")
    for pos, i in enumerate(activities):
        if pos == len(activities):
            l = Label(root, text=i)
            l.pack(pady=1)
            break
        l = Label(root, text=f'{i}, ')
        l.pack(pady=1)
root.mainloop()
