# -*- coding: utf-8 -*-

# Proyecto desarrollado por Adrián Álvarez @chapitro

"""
Filmpy es un proyecto que busca tener una plataforma
para el almacenamiento de información de películas,
en este se puede registrar una película y serán almacenados sus datos.
Por su parte cuando se registre una película se indica
el titulo, el valor de ranking y un comentario. Si el
usuario desea ingresa un link de www.filmaffinity.com
y cuando el usuario vea la información de la pelicula
se puede mostrar cierta información consultada de dicha
página. Entre lo principal se consulta: la foto, el país,
el año, el director, el director de fotografía,
el encargado de música y la respectiva sipnosis de la película.
"""

# LIBRERÍAS NECESARIAS

from Tkinter import *
from tkMessageBox import showinfo
import tkMessageBox
from PIL import Image, ImageTk
import os
from textblob import TextBlob
from register import registro
from register import edit
from ScrolledText import *

# --- GUI

root = Tk()
root.geometry("1320x690+15+10")
root.title("Filmpy @chapitro")
root.configure(background='#6E6E6E')
root.resizable(0,0)

# Colores:
"Fondo claro: #6E6E6E, Fondo oscuro: #424242, fondo más oscuro: #1C1C1C"


    # --- Frames

headF = Frame(root)
headF.place(x=575, y=10)
headF.configure(background='#6E6E6E')

dBF = LabelFrame(root, text="Data base", padx=5, pady=5, background='#6E6E6E',fg='#ffffff')
dBF.place(x=40,y=110)

searcher = LabelFrame(root, text="Searcher", padx=5, pady=5, background='#6E6E6E',fg='#ffffff')
searcher.place(x=40,y=395)

separator1 = Frame(height=500, width=2, bd=1, bg="#1C1C1C", relief=SUNKEN)
separator1.place(x=418, y= 100)

backInfo = Frame(relief=SUNKEN,  background='#6E6E6E')
backInfo.place(x=450, y= 120)

footerF1 = Frame(root)
footerF1.place(x=0,y=610,height=170,width=1320)
footerF1.configure(background='#424242')

footerF2 = Frame(root)
footerF2.place(x=0,y=610,height=15,width=1320)
footerF2.configure(background='#1C1C1C')

footerF3 = Frame(root)
footerF3.place(x=0,y=0,height=10,width=1320)
footerF3.configure(background='#585858')


    # --- Frames <//END//>

    # --- Logo 

img_logo = Image.open("config/logo.jpg") # Abrir logo
photo_logo = ImageTk.PhotoImage(img_logo) # Características de imagen
boton_logo = Button(headF, image=photo_logo, borderwidth=0,highlightcolor='#6E6E6E', highlightthickness=0,relief=FLAT,activebackground='#6E6E6E') # Config de botón/imagen 
boton_logo.photo_logo = photo_logo # Config
boton_logo.grid(row=0, column=0, rowspan=2) # Ubicación

def vacio():
    img_cinta = Image.open("config/cinta.jpg") # Abrir logo
    photo_cinta = ImageTk.PhotoImage(img_cinta) # Características de imagen
    boton_cinta = Button(root, image=photo_cinta, borderwidth=0,highlightcolor='#6E6E6E', highlightthickness=0,relief=FLAT,activebackground='#6E6E6E') # Config de botón/imagen 
    boton_cinta.photo_cinta = photo_cinta # Config
    boton_cinta.place(x=780,y=220)

    try:
        if os.listdir(r'movies/') == [] :
            Label(root, text='You can add a movie!',font=("bold", 13,"bold"),fg='#A4A4A4',bg='#6E6E6E').place(x=760,y=340)
        else:
            Label(root, text='You can watch movie info!',font=("bold", 13,"bold"),fg='#A4A4A4',bg='#6E6E6E').place(x=740,y=340)
    except:
        Label(root, text='You can add a movie!',font=("bold", 13,"bold"),fg='#A4A4A4',bg='#6E6E6E').place(x=760,y=340)

vacio()

    # --- Logo <//END//>


def registrar():
    registro()

Button(root, text="Movie!", command=registrar, background='#1C1C1C',relief=RIDGE,font=("bold", 11,"bold"),fg='#ffffff',activeforeground='#ffffff', activebackground='#424242').place(x=610,y=640)

def onselectdBA(evento): 
    try:
        wid = evento.widget
        index = int(wid.curselection()[0])
        onselectdB(index, dBlistaMovies)
        #Label(backInfoD, text='Info: ',font=("bold", 13,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=800,y=90)
    except:
        pass

def onselectdBB(evento):
    wid = evento.widget
    index = int(wid.curselection()[0])
    try:
        onselectdB(index, listRutas)
    except:
        pass

def onselectdB(index, listaX):

    global backInfo
    backInfo.destroy()

    backInfoD = Frame(height=10, width=775, bd=1, bg="#1C1C1C", relief=SUNKEN)
    backInfoD.place(x=450, y= 121)
    
    backInfoF = Frame(height=10, width=775, bd=1, bg="#1C1C1C", relief=SUNKEN)
    backInfoF.place(x=450, y=580)
    
    backInfo = Frame(height=450, width=775, bd=1, bg="#ffffff", relief=SUNKEN)
    backInfo.place(x=450, y= 130)
    global botonesF
    botonesF = Frame(root)
    botonesF.place(x=1245, y= 130)
    botonesF.configure(bg='#6E6E6E')

    infoMovieRead =  open("movies/%s"%listaX[index], 'r').read()
    splitInfo = infoMovieRead.split('-,-')

    def deleteMovie():
        os.remove("movies/%s.txt"%splitInfo[0])
        try:
            os.remove("covers/%s.jpg"%splitInfo[0])
        except:
            pass
        base()

        global backInfo
        backInfo.destroy()

        backInfoD = Frame(height=10, width=775, bg="#6E6E6E", relief=SUNKEN)
        backInfoD.place(x=450, y= 121)
        
        backInfoF = Frame(height=10, width=775, bg="#6E6E6E", relief=SUNKEN)
        backInfoF.place(x=450, y=580)
        
        backInfo = Frame(height=450, width=775, bg="#6E6E6E", relief=SUNKEN)
        backInfo.place(x=450, y= 130)
        
        global botonesF
        botonesF.destroy()

        botonesF = Frame(root)
        botonesF.place(x=1245, y= 130)
        botonesF.configure(bg='#6E6E6E')
        
        vacio()
        
    img_delete = Image.open("config/delete.jpg") # Abrir logo
    photo_delete = ImageTk.PhotoImage(img_delete) # Características de imagen
    boton_delete = Button(botonesF, image=photo_delete, borderwidth=0,highlightcolor='#6E6E6E', highlightthickness=0,relief=FLAT,activebackground='#6E6E6E', command= deleteMovie) # Config de botón/imagen 
    boton_delete.photo_delete = photo_delete # Config
    boton_delete.grid(row=0, column=0, pady=20)

    def editMovie():
        edit(splitInfo)
        
    img_edit = Image.open("config/edit.jpg") # Abrir logo
    photo_edit = ImageTk.PhotoImage(img_edit) # Características de imagen
    boton_edit = Button(botonesF, image=photo_edit, borderwidth=0,highlightcolor='#6E6E6E', highlightthickness=0,relief=FLAT,activebackground='#6E6E6E', command= editMovie) # Config de botón/imagen 
    boton_edit.photo_edit = photo_edit # Config
    boton_edit.grid(row=1, column=0)

    showF = Frame(root)
    showF.place(x=460, y= 140)
    showF.configure(bg='#ffffff')

    Label(showF, text="Title:",font=("bold", 11, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=0, column=0,sticky=W)
    Label(showF, text="\t" + splitInfo[0],font=("bold", 11),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=1, column=0,sticky=W)
    Label(showF, text="Ranking:",font=("bold", 11, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=2, column=0,sticky=W)
    Label(showF, text="\t" + splitInfo[2] + " pts  of  10 pts",font=("bold", 11),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=3, column=0,sticky=W)
    
    textpad = ScrolledText(showF, width=35, height=16, bg='#E6E6E6',font=("bold", 11))
    textpad.grid(row=4,column=0,pady=30,padx=5)
    textpad.insert(INSERT,splitInfo[1])
    textpad.config(state='disabled')

    separator2 = Frame(height=400, width=2, bd=1, bg="#ffffff", relief=SUNKEN)
    separator2.place(x=780, y= 150)

    showFB = Frame(root)
    showFB.place(x=790, y= 135)
    showFB.configure(bg='#ffffff')
    
    try: 
        img_img = Image.open("covers/%s.jpg"%splitInfo[0]) # Abrir logo
        photo_img = ImageTk.PhotoImage(img_img)
        boton_img = Button(showFB, image=photo_img, borderwidth=0,highlightcolor='#6E6E6E', highlightthickness=0,relief=FLAT,activebackground='#6E6E6E') 
        boton_img.photo_img = photo_img # Config
        boton_img.grid(row=0, column=0, rowspan=14, padx=7)
        Label(showFB, text="By FilmAffinity",font=("bold", 7, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=14, column=0)

        if len(splitInfo[4]) > 34:
            varTitle = (splitInfo[4])[:35] + '...'
        else:
            varTitle = splitInfo[4]
            
        Label(showFB, text="Title:",font=("bold", 8, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=1, column=1,sticky=W)
        Label(showFB, text="\t" + varTitle,font=("bold", 8),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=2, column=1,sticky=W)

        Label(showFB, text="Year:",font=("bold", 8, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=3, column=1,sticky=W)
        Label(showFB, text="\t" + splitInfo[5],font=("bold", 8),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=4, column=1,sticky=W)

        Label(showFB, text="Country:",font=("bold", 8, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=5, column=1,sticky=W)
        Label(showFB, text="\t" + splitInfo[6],font=("bold", 8),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=6, column=1,sticky=W)

        if len(splitInfo[7]) > 34:
            varDirector = (splitInfo[7])[:35] + '...'
        else:
            varDirector = splitInfo[7]
            
        Label(showFB, text="Director:",font=("bold", 8, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=7, column=1,sticky=W)
        Label(showFB, text="\t" + varDirector,font=("bold", 8),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=8, column=1,sticky=W)

        if len(splitInfo[8]) > 34:
            varScreenwriter = (splitInfo[8])[:35] + '...'
        else:
            varScreenwriter =splitInfo[8]
            
        Label(showFB, text="Screenwriter:",font=("bold", 8, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=9, column=1,sticky=W)
        Label(showFB, text="\t" + varScreenwriter,font=("bold", 8),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=10, column=1,sticky=W)

        if len(splitInfo[9]) > 34:
            varMusic = (splitInfo[9])[:35] + '...'
        else:
            varMusic =splitInfo[9]
            
        Label(showFB, text="Music:",font=("bold", 8, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=11, column=1,sticky=W)
        Label(showFB, text="\t" + varMusic,font=("bold", 8),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=12, column=1,sticky=W)

        if len(splitInfo[10]) > 34:
            varCine = (splitInfo[10])[:35] + '...'
        else:
            varCine =splitInfo[10]
            
        Label(showFB, text="Cinematography:",font=("bold", 8, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=13, column=1,sticky=W)
        Label(showFB, text="\t" + varCine,font=("bold", 8),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=14, column=1,sticky=W)

        Label(showFB, text="Synopsis:",font=("bold", 8, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=15, column=0,columnspan=2, sticky=W)
        
        textpad2 = ScrolledText(showFB, width=50, height=6, bg='#E6E6E6',font=("bold", 11))
        textpad2.grid(row=16,column=0, columnspan=2, pady=5,padx=5)
        textpad2.insert(INSERT,splitInfo[11])
        textpad2.config(state='disabled')
        
    except:
        Label(showFB, text="\n\n\n\n\n\n\n\n\n\n\nNo information.\nYou can edit link of movie and\nreceive technical info about movie.",font=("bold", 10, "bold"),fg='#000000',bg='#ffffff', justify=LEFT).grid(row=0, column=0)
    
def base():
    global dBF
    dBF.destroy()
    
    dBF = LabelFrame(root, text="Data base", padx=5, pady=5, background='#6E6E6E',fg='#ffffff')
    dBF.place(x=40,y=110)
    scrollbary = Scrollbar(dBF)
    scrollbary.pack(side = RIGHT, fill=Y)

    scrollbarx = Scrollbar(dBF,orient=HORIZONTAL)
    scrollbarx.pack(side = BOTTOM, fill=X )

    file_storage =  Listbox(dBF, height=10, width=45, activestyle='none', selectbackground='#F0F0F0', selectforeground='#007ee5', 
        yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set, font=("bold", 9, "bold"), background='#F0F0F0')

    try:
        for files in os.listdir(r'movies/'):
            file_storage.insert(END, "%s"%files[:-4])
    except:
        os.mkdir('movies/')
        
    global dBlistaMovies
    dBlistaMovies = os.listdir(r'movies/')
    
    file_storage.pack(side=LEFT, fill=BOTH)
    scrollbary.config(command = file_storage.yview) 
    scrollbarx.config(command = file_storage.xview)

    file_storage.bind('<<ListboxSelect>>', onselectdBA)

base()

Label(root, text='Movies',font=("bold", 13,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=175,y=85)

img_logo = Image.open("config/reload.jpg") # Abrir logo
photo_logo = ImageTk.PhotoImage(img_logo) # Características de imagen
boton_logo = Button(root, image=photo_logo, borderwidth=0,highlightcolor='#6E6E6E', highlightthickness=0,relief=FLAT,activebackground='#6E6E6E', command=base) # Config de botón/imagen 
boton_logo.photo_logo = photo_logo # Config
boton_logo.place(x=240,y=87)

Label(root, text='Search', font=("bold", 13,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=175,y=335)

search = Entry(root)
search.config(width=40,background='#ffffff',font=("bold", 10,"bold"), fg='#1C1C1C')
search.place(x=70,y=365)

def enter(event):    
    global searcher
    searcher.destroy()
    
    searcher = LabelFrame(root, text="Searcher", padx=5, pady=5, background='#6E6E6E',fg='#ffffff')
    searcher.place(x=40,y=395)

    texto = event.widget.get()

    listTexto = TextBlob(texto.lower()).words

    listPalabrasR = [] 
    for i in os.listdir(r'movies/'):
        listPalabrasR += [ [i, TextBlob(i[:-4].lower()).words] ]


    for h,  i in enumerate(listPalabrasR):
        count = 0
        for j in i[1]:
            if j in listTexto:
                count += 1
        listPalabrasR[h] += [count]

    listPalabras = []
    
    for i in listPalabrasR:
        if i[-1] > 0:
            listPalabras += [i]

    # Ordenamiento:
    valores = []
    count = 0
    listSORT = []
    while listPalabras != []:
        for i in listPalabras:
            valores += [i[-1]]
        if max (valores) == listPalabras [count] [-1]:
            listSORT += [listPalabras [count]]
            listPalabras = listPalabras[:count]+ listPalabras[count+1:]
            count = 0
            valores = []
        else:
            count +=1
    global listRutas
    listRutas = []
    for i in listSORT:
        listRutas += [i[0]]
    
    scrollbary = Scrollbar(searcher)
    scrollbary.pack(side = RIGHT, fill=Y)

    scrollbarx = Scrollbar(searcher,orient=HORIZONTAL)
    scrollbarx.pack(side = BOTTOM, fill=X )

    file_storageB =  Listbox(searcher, height=10, width=45, activestyle='none', selectbackground='#F0F0F0', selectforeground='#007ee5', 
        yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set, font=("bold", 9, "bold"), background='#F0F0F0')

    for files in listRutas:
        file_storageB.insert(END, "%s"%files[:-4])

    file_storageB.pack(side=LEFT, fill=BOTH)
    scrollbary.config(command = file_storageB.yview) 
    scrollbarx.config(command = file_storageB.xview)
        
    file_storageB.bind('<<ListboxSelect>>', onselectdBB)

search.bind('<Return>', enter)

Label(root, text="By @chapitro 2015 v0.2",font=("Helvetica 16 bold italic", 10),fg='#ffffff', background='#424242').place(x=1175,y=668)

root.mainloop()
