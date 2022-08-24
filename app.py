import os 
import Randow
from Colorama import fore, back, style 

jogarnovamente="s"
jogadas=0
quemjoga=2
maxjogadas=9
vit="n"
velha=[
[" "," "," ",],
[" "," "," ",],
[" "," "," ",]
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("   -----------")
    print("jogadas: " + fore.green + str (jogadas) + fore.reset)

while True:
    tela()
    #jog
    #cpu
    #vv
