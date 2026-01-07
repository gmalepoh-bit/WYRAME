#importation du module kinter
from tkinter import *


# fonction permettant de changer de joueur
def cp_player():
    global current_player
    if current_player=="x":
        current_player="0"
    else:
        current_player="x"



#definition de la victoire
def check_win(click_row, click_column):
    compt=0
    #victoire hrizontale 
    for i in range(3):
        check_btn=stockage[i][click_row]
        #compteur
       
        if check_btn ['text'] ==current_player:
            compt+=1
    if compt==3:
        print("c'est gagner h")
    #gagner v
    compt=0
    for i in range(3):
        check_btn=stockage[click_column][i]
        #compteur
        if check_btn ['text'] ==current_player:
            compt+=1
    if compt==3:
        print("c'est gagner v")
    #gagner d
    compt=0
    for i in range(3):
        check_btn=stockage[i][i]
        #compteur
        if check_btn ['text'] ==current_player:
            compt+=1
    if compt==3:
        print("c'est gagner d")
    # gagner di
    # 
    compt=0
    for i in range(3):
        check_btn=stockage[2-i][i]
        #compteur
        if check_btn ['text'] ==current_player:  
            compt+=1
    if compt==3:
        print("c'est gagner di")
#definition de la grille du jeu
def grille():   
# definir la fonction de declanchement
# il est possible de faiore sa mais nous allons uiliser une boucle 
    for column in range(3):
        # créee une liste qui vas contenir les donnée
        btn_r=[]
        for row in range(3):
            btn=Button(
                root,text="",font=("Arial", 50),
                width=5, height=2,command=lambda r=row, t=column:action(r, t)
                )
            btn.grid(row=row, column=column)
            btn ['background']="yellow"
            btn_r.append(btn)
        stockage.append(btn_r)
#
def action(row ,column):
    print("click", row, column)
        #
    botton_click=stockage[column][row]
    botton_click.config(text=current_player)
    
    check_win(row, column)
    cp_player()

#création 'une variable de stockage des information
stockage=[]
#
current_player="x"

#création de la fenettre de jeu
root = Tk()
#root.geometry("500x500")
root.minsize(600, 600)
root.title("morpion")
root ['background'] = "black"
#
grille()



root.mainloop()
