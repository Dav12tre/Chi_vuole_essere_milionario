def chi_vuol_essere_millionario():
    import time
    import pandas as pd
    import random
    localtime= time.localtime()
    times= time.strftime("%H:%M",localtime)
    print("BENVENUTI A CHI VUOL ESSERE MILIONARIO!")
    print("Rispondi alle domande per vincere!")
    df = {
        "Domanda" : ["Qual è la capitale della Francia?", "Dov'è nata la pizza?", "Quando fu scoperta l'America?", "Qual è il valore del p greco?", "77+33=", "che ore sono?"],
        "Opzioni" : ["a) Roma b) Parigi c) Berlino d) Marsiglia", "a) Napoli b) New York c) Roma d) Parigi", "a)1200 b)1508 c)1492 d)ieri", "a) 13.2456... b)3.1416... c)3.1415... d)4.1312...", "a)100 b)1000 c)110 d)10", f"a)1:24 b)17:35 c)23:46 d){times}",],
        "Risposta_corretta" : ["b", "a", "c", "b", "c", "d"]
    }
    start_timer = time.time()
    tempo_rimanente = time.time() - start_timer
    print("se riesci a finire in meno di 30 secondi")
    v=0
    o= 5
    soldi=0
    inizia=input("premi invio per iniziare")
    start_timer = time.time()

    for i in range(1, 7):

        numm = random.randint(0, o)
        o=o-1


        dom= df["Domanda"]
        print(i)
        print(dom[numm])
        dom.pop(numm)
        op= df["Opzioni"]
        print(op[numm])
        op.pop(numm)
        risposta = input("Inserisci la lettera corrispondente!")
        rispe= df["Risposta_corretta"]
        risp= rispe[numm]
        vincita= [500, 2500, 10000, 50000 , 100000, 250000, 500000]
        win=vincita[v]
        v+=1

        if risposta.lower() == risp:
            print(f"Complimenti!Hai vinto altri {win}$")
            rispe.pop(numm)
            soldi+=win
        else:
            print("Mi dispiace, hai risposto sbagliato!")
            soldi=0
            rispe.pop(numm)
            return "rifai"
    print(f"hai vinto {soldi}$")
    tempo_rimanente = time.time() - start_timer
    print(f"in {tempo_rimanente} secondi")
    if tempo_rimanente>= 30:
        print("quindi hai perso tutto")
        return "rifai"
rifai= chi_vuol_essere_millionario()
if rifai=="rifai":
    input("premi invio se vuoi avere una seconda chance")
    chi_vuol_essere_millionario()