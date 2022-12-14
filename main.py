from asyncio import run_coroutine_threadsafe
from email.mime import image
from logging import root
import tkinter
from tkinter import *
from tkinter import ttk

# importando o pillow
from PIL import Image, ImageTk

import random

# cores --------------------------------
co0 = "#FFFFFF" # white
co1 = "#333333" # branca
co2 = "#fcc058" # orange
co3 = "#38576b" # valor
co4 = "#3297a8" # blue
co5 = "#fff873" # yellow
co6 = "#fcc058" #orange
co7 = "#e85151" #vermelha
co8 = "#34eb3d" # + verde
fundo = "#3b3b3b"

# configurando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo) 


# dividindo a janela

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando o frame cima

app_1 = Label(frame_cima, text="voce", height=1, anchor='center', font=('ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=50, y=20)

app_= Label(frame_cima, text=":", height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=20)


app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=170, y=20)
app_2 = Label(frame_cima, text="PC", height=1, anchor='center', font=('ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=205, y=70)
app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

app_linha = Label(frame_cima, text="", width=255, anchor='center', font=('ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)


global voce 
global pc 
global rondas 
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rondas = 5 





#fun????o logica do jogo 
def jogar(i):
    global rondas 
    global pontos_voce
    global pontos_pc

    if rondas >0:
        print(rondas)
        op??oes =['Pedra','Papel','Tesoura']
        pc = random.choice(op??oes)
        voce = i 

     # caso for igual
    if voce== 'pedra' and pc == 'pedra':
        print('empate')
        app_1_linha['bg'] = co0
        app_2_linha['bg'] = co0
        app_linha['bg'] = co3

    elif voce== 'papel' and pc == 'papel':
         print('empate')
         app_1_linha['bg'] = co0
         app_2_linha['bg'] = co0
         app_linha['bg'] = co3

    elif voce== 'tesoura' and pc == 'tesoura':
         print('empate')
         app_1_linha['bg'] = co0
         app_2_linha['bg'] = co0
         app_linha['bg'] = co3

# para frente
    elif voce== 'Pedra' and pc == 'papel':
         print('voce ganhou')
         app_1_linha['bg'] = co4
         app_2_linha['bg'] = co8
         app_linha['bg'] = co8 


    else:
        fim_do_jogo()





#fun????o iniciar o jogo
def iniciar_jogo():
 global icon_1
 global icon_2
 global icon_3
 global b_icon_1
 global b_icon_2
 global b_icon_3


 icon_1 = Image.open('images/papel.png') 
 icon_1 = icon_1.resize((50,50), Image.ANTIALIAS) 
 icon_1 = ImageTk.PhotoImage(icon_1)
 b_icon_1 = Button(frame_baixo,comand=lambda: jogar('pedra'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0,font=('ivy 30 bold'), anchor=CENTER, relief=FLAT)
 b_icon_1.place(x=15, y=60)

 icon_2 = Image.open('images/pedra.png')
 icon_2 = icon_2.resize((50,50), Image.ANTIALIAS) 
 icon_2 = ImageTk.PhotoImage(icon_2)
 b_icon_2 = Button(frame_baixo,comand=lambda: jogar('papel'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0,font=('ivy 30 bold'), anchor=CENTER, relief=FLAT)
 b_icon_2.place(x=95, y=60)

 icon_3 = Image.open('images/tesoura.png')
 icon_3 = icon_3.resize((50,50), Image.ANTIALIAS) 
 icon_3 = ImageTk.PhotoImage(icon_3)
 b_icon_3 = Button(frame_baixo,comand=lambda: jogar('tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0,font=('ivy 30 bold'), anchor=CENTER, relief=FLAT)
 b_icon_3.place(x=170, y=60)



#fun????o terminar o jogo
def fim_do_jogo():
    pass

b_jogar = Button(frame_baixo,command=iniciar_jogo, width=30, text='jogar', bg=fundo, fg=co0, font=('ivy 10 bold'), anchor=CENTER, relief=FLAT  )
b_jogar.place(x=5, y=151)                                                                                                                           


def fim_do_jogo():
    pass





                                                                                                








janela.mainloop()
