from tkinter import *
from utils import *
from PIL import ImageTk, Image


def update_window():
    json_pokemon = get_answer_from_api()
    img = Image.open(find_pokemon(json_pokemon))
    lbl['text'] = json_pokemon['name']
    next_photo = ImageTk.PhotoImage(img.resize((400, 400)),master= root)
    pok_img.configure(image=next_photo)
    pok_img.image = next_photo

root = Tk()
root.title("Your pokemon")
root.geometry('600x400')
root.resizable(width=False, height=False)
frm = Frame(root)
frm.grid(column=1, row=0)

json_pokemon = get_answer_from_api()
img = Image.open(find_pokemon(json_pokemon))
photo = ImageTk.PhotoImage(img.resize((400, 400)))
pok_img = Label(frm, image=photo)
pok_img.grid(column=0, row=0)
lbl = Label(frm, text=json_pokemon['name'], font=50)
lbl.grid(column=1, row=0)
Button(frm, text="OK", command=root.destroy, height=2, width=5).grid(column=4, row=0)
Button(frm, text="Next", command=update_window, height=2, width=5).grid(column=5, row=0)

root.mainloop()
