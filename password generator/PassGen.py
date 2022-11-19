from random import randint, choice
import string
import pyperclip
from tkinter import *

def generate_password():
    password_min = 12
    password_max = 25
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join (choice(all_chars) for y in range (randint (password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
     

# créer la fenêtre
window = Tk()
window.title("PassGen")
window.geometry("1080x720")
window.config(background='#4065A4')

# créer la frame principale
frame = Frame(window, bg='#4065A4')

# création d'image
width = 512
height = 512
image = PhotoImage(file="padlock.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# créer une sous boite
right_frame = Frame(frame, bg='#4065A4')

# créer un titre
label_title = Label(right_frame, text="Mot de passe", font= ("Helvetica", 35), bg='#4065A4', fg="white")
label_title.pack()

# créer un champs de texte
password_entry = Entry(right_frame, font= ("Helvetica", 35), bg='#4065A4', fg="white")
password_entry.pack()

# créer un bouton
generate_password_button = Button(right_frame, text="Générer", font= ("Helvetica", 40), bg="#4065A4", fg="#47DC0F", command=generate_password)
generate_password_button.pack(fill=X)

# sous boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

# barre de menu
menu_bar = Menu(window)
# créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer la fenêtre pour ajouter la menubar
window.config(menu=menu_bar)

# copier les mots de passe
pyperclip.copy('je t aime maman ❤️')

# afficher la frame
frame.pack(expand=YES)

# afficher la fenêtre
window.mainloop()