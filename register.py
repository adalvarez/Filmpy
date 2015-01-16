# -*- coding: utf-8 -*-

# Proyecto desarrollado por Adrián Álvarez Calderón @chapitro

from Tkinter import *
from tkMessageBox import showinfo
import tkMessageBox
from PIL import Image, ImageTk
from ScrolledText import *
import os
from lxml import html
import requests
import urllib2

def llamarWEB (url, name):
     page = requests.get(url)
     tree = html.fromstring(page.text)

     infoA = tree.xpath('//dd/text()')
     infoB = tree.xpath('//a/text()')

     mTitle = infoA[0]
     mYear = infoA[1]

     mCountry = ''
     if infoA[2][-4:] == "min.":
          mCountry = infoA[3]
          count = 4
     else:
          mCountry = infoA[2]
          count = 3

     countB = 0
     while infoB[countB] != "Tweet":
          countB += 1

     mDirector = infoB [ countB +1]

     while infoA[count][0] == ',':
          count += 1

     mScreenwriter = infoA[count]

     mMusic = infoA[count+1]

     mCinematography = infoA[count+2]

     count = -1
     while infoA[count][0] == '\n' or infoA[count][0] == '\r':
          count += -1
          
     mSynopsis = infoA[count]

     infoC= tree.xpath('//img/@src')

     count = -1
     while infoC[count][-8:] != 'main.jpg':
          count += -1

     imgLink = infoC[count]
     
     try:
          furl = urllib2.urlopen(imgLink)
          f = file("covers/%s.jpg"%name,'wb')
          f.write(furl.read())
          f.close()
     except:
          print 'Unable to download file'
           
     infoMovie = ('-,-' +mTitle + '-,-' + mYear + '-,-' + mCountry + '-,-' + mDirector + '-,-' + mScreenwriter + '-,-' + mMusic + '-,-' + mCinematography + '-,-' + mSynopsis).encode('utf-8')
     return infoMovie


def edit(lista):
     root = Toplevel()
     root.geometry("420x630+420+35")
     root.title("Register")
     root.configure(background='#6E6E6E')

     footer = Frame(root)
     footer.place(x=0, y=0,height=15,width=1320)
     footer.configure(background='#1C1C1C')

     Label(root, text='Edit a movie in Filmpy!',font=("bold", 14,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=85,y=20)

     Label(root, text='Title *',font=("bold", 12,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=20,y=80)

     title = Entry(root)
     title.config(width=30,background='#ffffff',font=("Times New Roman", 12), fg='#1C1C1C')
     title.place(x=25, y= 110)
     title.insert(INSERT,lista[0])

     Label(root, text='Ranking *',font=("bold", 11,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=295,y=80)
     
     def calificacion(*argumentos):
          if format(opcion_defaultA.get())=="1":
               global option
               option = 1
          elif format(opcion_defaultA.get())=="2":
               option = 2
          elif format(opcion_defaultA.get())=="3":
               option = 3
          elif format(opcion_defaultA.get())=="4":
               option = 4
          elif format(opcion_defaultA.get())=="5":
               option = 5
          elif format(opcion_defaultA.get())=="6":
               option = 6
          elif format(opcion_defaultA.get())=="7":
               option = 7
          elif format(opcion_defaultA.get())=="8":
               option = 8
          elif format(opcion_defaultA.get())=="9":
               option = 9
          elif format(opcion_defaultA.get())=="10":
               option = 10
          else:
               option = lista[2]
               
     opcion_defaultA = StringVar(root)
     opcion_defaultA.trace("w", calificacion)
     opcion_defaultA.set(lista[2])
     
     elige_frameA = OptionMenu(root, opcion_defaultA, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
     elige_frameA.config(bg = "#ffffff", borderwidth=0)
     elige_frameA["menu"].config(bg = "#ffffff",font=('calibri',(10)))
     elige_frameA.place(x=300, y=110)
     
     Label(root, text='Commentary *',font=("bold", 12,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=20,y=150)

     
     textpad = ScrolledText(root, width=40, height=15, bg='#ffffff',font=("Bookman Old Style", 11))
     textpad.place(x=25, y=180)
     textpad.insert(INSERT,lista[1])

     Label(root, text='Link FilmAffinity',font=("bold", 12,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=20,y=485)

     url = Entry(root)
     url.config(width=43,background='#ffffff',font=("Times New Roman", 12), fg='#1C1C1C')
     url.place(x=25, y= 512)
     url.insert(INSERT,lista[3])

     def info():
          showinfo(title="Information", message="Allowed only links FilmAffinity.\nIn the next format: 'http://www.filmaffinity.com/en/--'.")

     img_logo = Image.open("config/icoInfo.jpg") # Abrir logo
     photo_logo = ImageTk.PhotoImage(img_logo) # Características de imagen
     boton_logo = Button(root, image=photo_logo, borderwidth=0,highlightcolor='#6E6E6E', highlightthickness=0,relief=FLAT,activebackground='#6E6E6E', command= info) # Config de botón/imagen 
     boton_logo.photo_logo = photo_logo # Config
     boton_logo.place(x=380, y=513) # Ubicación

     Label(root, text="* Required information",font=("Helvetica 16 bold italic", 8),fg='#ffffff', background='#6E6E6E').place(x=20,y=545)

     def save():
          try:
               os.remove("movies/%s.txt"%lista[0])
               os.remove("covers/%s.jpg"%lista[0])
          except:
               pass
          
          if title.get() != '' and textpad.get('1.0', END+'-1c') != '' and option != 0 and title.get() not in os.listdir(r'movies/'):
               if url.get() != '' and url.get()[:31] == 'http://www.filmaffinity.com/en/':
                    movieDatos = llamarWEB(url.get(), title.get())
                    guardarPelicula = open('movies/%s.txt'%title.get(),'w')
                    datos = title.get() + '-,-' + textpad.get('1.0', END+'-1c') + '-,-' + str(option) + '-,-' + url.get() + movieDatos.decode('utf-8')
                    guardarPelicula.write(datos.encode('utf-8'))
                    guardarPelicula.close()
                    showinfo(title="Warning", message="Please reload the panel of movies.")
                    root.destroy()
               elif url.get() == '':
                    guardarPelicula = open('movies/%s.txt'%title.get(),'w')
                    datos = title.get() + '-,-' + textpad.get('1.0', END+'-1c') + '-,-' + str(option) + '-,-' + ' ' + '-,-' + ' ' + '-,-' + '' + '-,-' + ' ' + '-,-' + ' ' + '-,-' + ' ' + '-,-'  + ' ' + '-,-' + ' ' + '-,-' + ' ' + '-,-' 
                    guardarPelicula.write(datos.encode('utf-8'))
                    guardarPelicula.close()
                    showinfo(title="Warning", message="Please reload the panel of movies.")
                    root.destroy()
               else:
                    tkMessageBox.showerror(title="Warning", message="Link not allowed. You can check the format in in the information button.")
          else:
               tkMessageBox.showerror(title="Warning", message="Problem with the required values. Please check:\n• Already entered the film.\n• Enter the title of the film.\n• Enter the commentary of the film.\n• Select a value ranking.")

     Button(root, text="Save", command=save, background='#1C1C1C',relief=RIDGE,font=("bold", 11,"bold"),fg='#ffffff',activeforeground='#ffffff', activebackground='#424242').place(x=170, y=580)

     root.mainloop()


def registro():
     root = Toplevel()
     root.geometry("420x630+420+35")
     root.title("Register")
     root.configure(background='#6E6E6E')

     footer = Frame(root)
     footer.place(x=0, y=0,height=15,width=1320)
     footer.configure(background='#1C1C1C')

     Label(root, text='Register a movie in Filmpy!',font=("bold", 14,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=85,y=20)

     Label(root, text='Title *',font=("bold", 12,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=20,y=80)

     title = Entry(root)
     title.config(width=30,background='#ffffff',font=("Times New Roman", 12), fg='#1C1C1C')
     title.place(x=25, y= 110)

     Label(root, text='Ranking *',font=("bold", 11,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=295,y=80)
     
     def calificacion(*argumentos):
          if format(opcion_defaultA.get())=="1":
               global option
               option = 1
          elif format(opcion_defaultA.get())=="2":
               option = 2
          elif format(opcion_defaultA.get())=="3":
               option = 3
          elif format(opcion_defaultA.get())=="4":
               option = 4
          elif format(opcion_defaultA.get())=="5":
               option = 5
          elif format(opcion_defaultA.get())=="6":
               option = 6
          elif format(opcion_defaultA.get())=="7":
               option = 7
          elif format(opcion_defaultA.get())=="8":
               option = 8
          elif format(opcion_defaultA.get())=="9":
               option = 9
          elif format(opcion_defaultA.get())=="10":
               option = 10
          else:
               option = 0
               
     opcion_defaultA = StringVar(root)
     opcion_defaultA.trace("w", calificacion)
     opcion_defaultA.set(">>")
     
     elige_frameA = OptionMenu(root, opcion_defaultA, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
     elige_frameA.config(bg = "#ffffff", borderwidth=0)
     elige_frameA["menu"].config(bg = "#ffffff",font=('calibri',(10)))
     elige_frameA.place(x=300, y=110)
     
     Label(root, text='Commentary *',font=("bold", 12,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=20,y=150)

     
     textpad = ScrolledText(root, width=40, height=15, bg='#ffffff',font=("Bookman Old Style", 11))
     textpad.place(x=25, y=180)

     Label(root, text='Link FilmAffinity',font=("bold", 12,"bold"),fg='#ffffff',bg='#6E6E6E').place(x=20,y=485)

     url = Entry(root)
     url.config(width=43,background='#ffffff',font=("Times New Roman", 12), fg='#1C1C1C')
     url.place(x=25, y= 512)

     def info():
          showinfo(title="Information", message="Allowed only links FilmAffinity.\nIn the next format: 'http://www.filmaffinity.com/en/--'.")

     img_logo = Image.open("config/icoInfo.jpg") # Abrir logo
     photo_logo = ImageTk.PhotoImage(img_logo) # Características de imagen
     boton_logo = Button(root, image=photo_logo, borderwidth=0,highlightcolor='#6E6E6E', highlightthickness=0,relief=FLAT,activebackground='#6E6E6E', command= info) # Config de botón/imagen 
     boton_logo.photo_logo = photo_logo # Config
     boton_logo.place(x=380, y=513) # Ubicación

     Label(root, text="* Required information",font=("Helvetica 16 bold italic", 8),fg='#ffffff', background='#6E6E6E').place(x=20,y=545)
     
     def ejecutar():
          if title.get() != '' and textpad.get('1.0', END+'-1c') != '' and option != 0 and title.get() not in os.listdir(r'movies/'):
               if url.get() != '' and url.get()[:31] == 'http://www.filmaffinity.com/en/':
                    movieDatos = llamarWEB(url.get(), title.get())
                    guardarPelicula = open('movies/%s.txt'%title.get(),'w')
                    datos = title.get() + '-,-' + textpad.get('1.0', END+'-1c') + '-,-' + str(option) + '-,-' + url.get() + movieDatos.decode('utf-8')
                    guardarPelicula.write(datos.encode('utf-8'))
                    guardarPelicula.close()
                    root.destroy()
               elif url.get() == '':
                    guardarPelicula = open('movies/%s.txt'%title.get(),'w')
                    datos = title.get() + '-,-' + textpad.get('1.0', END+'-1c') + '-,-' + str(option) + '-,-' + ' ' + '-,-' + ' ' + '-,-' + '' + '-,-' + ' ' + '-,-' + ' ' + '-,-' + ' ' + '-,-'  + ' ' + '-,-' + ' ' + '-,-' + ' ' + '-,-' 
                    guardarPelicula.write(datos.encode('utf-8'))
                    guardarPelicula.close()
                    root.destroy()
               else:
                    tkMessageBox.showerror(title="Warning", message="Link not allowed. You can check the format in in the information button.")
          else:
               tkMessageBox.showerror(title="Warning", message="Problem with the required values. Please check:\n• Already entered the film.\n• Enter the title of the film.\n• Enter the commentary of the film.\n• Select a value ranking.")

     
     Button(root, text="Register!", command=ejecutar, background='#1C1C1C',relief=RIDGE,font=("bold", 11,"bold"),fg='#ffffff',activeforeground='#ffffff', activebackground='#424242').place(x=170, y=580)
     
     root.mainloop()
