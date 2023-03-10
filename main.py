from tkinter import *
from tkinter import ttk
import random
bot = random.randint(1,3)
player = int(input("Виберіть щось одне(1-папір,2-камінь,3-ножниці):"))
n1 = 0
n2 = 0
n3 = 0
#бота
n4 = 0
#гравця
n5 = 0
n6 = "У гравця балів:"
n7 = "У бота балів:"

root = Tk()
root.title("Камін,ножниці,папір")
root.geometry("250x200")

def Close():
    root.destroy()

exit_button = Button(root, text="Нажміть щоб побачити результат", command=Close)
exit_button.pack(pady=20)
root.mainloop()





if bot == 1:
    print("У бота папір")
    n1 = "У бота папір"
elif bot == 2:
    print("У бота камінь")
    n1 = "У бота камінь"
else:
    print("У бота ножниці")
    n1 = "У бота ножниці"

#press F


if player == 1:
    print("У вас папір")
    n3 = "У вас папір"
elif player == 2:
    print("У вас камінь")
    n3 = "У вас камінь"
else:
    print("У вас ножниці")
    n3 = "У вас ножниці"



if bot == player:
    print("Нічия")
    n2 = "Нічия"
elif 1 < player < bot:
    print("Ви виграли")
    n2 = "Ви виграли"
    n5 = +1
elif bot < player < 3:
    print("Ви програли")
    n2 = "Ви програли"
    n4 = +1
elif player < bot < 3:
    print("Ви виграли")
    n2 = "Ви виграли"
    n5 = +1
elif player < 2 < bot:
    print("Ви програли")
    n2 = "Ви програли"
    n4 = +1
elif 1 < bot < player:
    print("Ви програл")
    n2 = "Ви програли"
    n4 = +1
elif bot < 2 < player:
    print("Ви виграли")
    n2 = "Ви виграли"
    n5 = +1







root = Tk()
root.title("Камін,ножниці,папір")
root.geometry("250x200")


def click():
    window = Tk()
    window.title("Новое окно")
    window.geometry("250x200")



label = ttk.Label(text=(n1),foreground="red")
label.pack(anchor=W, expand=10)

label = ttk.Label(text=(n2))
label.pack(anchor=S, expand=8)

label = ttk.Label(text=(n3),foreground="blue")
label.pack(anchor=E, expand=10)

label = ttk.Label(text=(n6 + str(n4)),foreground="blue")
label.pack(anchor=NW, expand=10)

label = ttk.Label(text=(n7 + str(n5)),foreground="red")
label.pack(anchor=SE, expand=10)

root.mainloop()



#Камінь,ножниці,бумага





