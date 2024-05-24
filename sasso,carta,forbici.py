import random 
punti=0
while True:
    mosse=["sasso","carta","forbici"]
    computer=mosse[random.randint(0,2)]
    user=mosse[int(input("fai la tua mossa (0 sasso,1 carta,2 forbici):"))]
    print(f"la tua mossa:{user}\nLa mossa del computer:{computer}")
    if computer==user:
        print("pareggio")
    elif computer==mosse[0] and user==mosse[2]:
        print("hai perso")
    elif computer==mosse[1] and user==mosse[0]:
        print("hai perso") 
    elif computer==mosse[2] and user==mosse[1]:
        print("hai perso")  
    else:
        print("hai vinto!")
        punti=punti +1
    scelta=input("vuoi continuare? si o no: ")
    print("il tuo punteggio:",punti)
    if scelta.lower()=="no":
        print("ci vediamo alla prossima partita")
        break           
