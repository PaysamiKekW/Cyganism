from tkinter import *
from PIL import ImageTk,Image
from threading import *

penize = 100
pzs = 800

pracovnik = [0,0,0,0,0,0,0,0,0,0]
pracovnik_nazvy = ["Cikáni", "Gadžové", "Cikánčata", "Varny", "Dealeři"]
koef = 1.5

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def update():
    global penize, pzs, root
    penize = penize + pzs
    penize_lbl = Label(frame_penezenka, text="Peníze: " + str(penize), anchor=W)
    penize_lbl.grid(row=0, column=1, sticky=W)
    root.after(500, update)

def budovaUppCena(urovenBudovy,typ):
	return str(int((100*typ) * (1.06)**urovenBudovy))

root = Tk()
root.title("Pica z krtka")
root.iconbitmap('c:/gui/something.ico')

frame_penezenka = LabelFrame(root, text="Bohatství", padx=25,pady=10)
frame_penezenka.pack(padx=10,pady=10)

penize_lbl = Label(frame_penezenka, text="Peníze: " + str(penize), anchor=W, width=40)
penize_lbl.grid(row=0, column=1, sticky=W)

frame = LabelFrame(root, text="Domov práce", padx=50,pady=50)
frame.pack(padx=10,pady=10)

def update_btn_text(which_one):
	global pracovnik
	if which_one == 1:
		pracovnik[0] += 1
		myButton1_text.set("Cena: " + budovaUppCena(pracovnik[0],2*koef))
		pracovnik_1_lbl_text.set("[OBR] " + pracovnik_nazvy[0] + ": " + str(pracovnik[0]) + "  [+" + str(pracovnik[1])+ "]  ")
	elif which_one == 2:
		pracovnik[2] += 1
		myButton2_text.set("Cena: " + budovaUppCena(pracovnik[2],8*koef))
		pracovnik_2_lbl_text.set("[OBR] " + pracovnik_nazvy[1] + ": " + str(pracovnik[2]) + "  [+" + str(pracovnik[3])+ "]  ")
	elif which_one == 3:
		pracovnik[4] += 1
		myButton3_text.set("Cena: " + budovaUppCena(pracovnik[4],32*koef))
		pracovnik_3_lbl_text.set("[OBR] " + pracovnik_nazvy[2] + ": " + str(pracovnik[4]) + "  [+" + str(pracovnik[5])+ "]  ")
	elif which_one == 4:
		pracovnik[6] += 1
		myButton4_text.set("Cena: " + budovaUppCena(pracovnik[6],64*koef))
		pracovnik_4_lbl_text.set("[OBR] " + pracovnik_nazvy[3] + ": " + str(pracovnik[6]) + "  [+" + str(pracovnik[7])+ "]  ")
	elif which_one == 5:
		pracovnik[8] += 1
		myButton5_text.set("Cena: " + budovaUppCena(pracovnik[8],128*koef))
		pracovnik_5_lbl_text.set("[OBR] " + pracovnik_nazvy[4] + ": " + str(pracovnik[8]) + "  [+" + str(pracovnik[9])+ "]  ")
	else:
		pass
    


pracovnik_1_lbl_text = StringVar()
pracovnik_1_lbl = Label(frame, textvariable=pracovnik_1_lbl_text)
pracovnik_1_lbl_text.set("[OBR] " + pracovnik_nazvy[0] + ": " + str(pracovnik[0]) + "  [+" + str(pracovnik[1])+ "]  ")
pracovnik_1_lbl.grid(row=0, column=1, sticky=W)

pracovnik_2_lbl_text = StringVar()
pracovnik_2_lbl = Label(frame, textvariable=pracovnik_2_lbl_text)
pracovnik_2_lbl_text.set("[OBR] " + pracovnik_nazvy[1] + ": " + str(pracovnik[2]) + "  [+" + str(pracovnik[3])+ "]  ")
pracovnik_2_lbl.grid(row=1, column=1, sticky=W)

pracovnik_3_lbl_text = StringVar()
pracovnik_3_lbl = Label(frame, textvariable=pracovnik_3_lbl_text)
pracovnik_3_lbl_text.set("[OBR] " + pracovnik_nazvy[2] + ": " +str(pracovnik[4]) + "  [+" + str(pracovnik[5])+ "]  ")
pracovnik_3_lbl.grid(row=2, column=1, sticky=W)

pracovnik_4_lbl_text = StringVar()
pracovnik_4_lbl = Label(frame, textvariable=pracovnik_4_lbl_text)
pracovnik_4_lbl_text.set("[OBR] " + pracovnik_nazvy[3] + ": " + str(pracovnik[6]) + "  [+" + str(pracovnik[7])+ "]  ")
pracovnik_4_lbl.grid(row=3, column=1, sticky=W)

pracovnik_5_lbl_text = StringVar()
pracovnik_5_lbl = Label(frame, textvariable=pracovnik_5_lbl_text)
pracovnik_5_lbl_text.set("[OBR] " + pracovnik_nazvy[4] + ": " + str(pracovnik[8]) + "  [+" + str(pracovnik[9])+ "]  ")
pracovnik_5_lbl.grid(row=4, column=1, sticky=W)



myButton1_text = StringVar()
myButton1 = Button(frame, textvariable=myButton1_text, width=18, command=lambda:update_btn_text(1))
myButton1_text.set("Cena: " + budovaUppCena(pracovnik[0],2*koef))
myButton1.grid(row=0, column=2, sticky=W)

myButton2_text = StringVar()
myButton2 = Button(frame, textvariable=myButton2_text, width=18, command=lambda:update_btn_text(2))
myButton2_text.set("Cena: " + budovaUppCena(pracovnik[1],8*koef))
myButton2.grid(row=1, column=2, sticky=W)

myButton3_text = StringVar()
myButton3 = Button(frame, textvariable=myButton3_text, width=18, command=lambda:update_btn_text(3))
myButton3_text.set("Cena: " + budovaUppCena(pracovnik[2],32*koef))
myButton3.grid(row=2, column=2, sticky=W)

myButton4_text = StringVar()
myButton4 = Button(frame, textvariable=myButton4_text, width=18, command=lambda:update_btn_text(4))
myButton4_text.set("Cena: " + budovaUppCena(pracovnik[3],64*koef))
myButton4.grid(row=3, column=2, sticky=W)

myButton5_text = StringVar()
myButton5 = Button(frame, textvariable=myButton5_text, width=18, command=lambda:update_btn_text(5))
myButton5_text.set("Cena: " + budovaUppCena(pracovnik[4],128*koef))
myButton5.grid(row=4, column=2, sticky=W)

root.after(1000,update)
root.mainloop()
