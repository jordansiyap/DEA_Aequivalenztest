# Gefordert: Python-Programm
# Sie können weitere Hilfsfunktionen verwenden!
# Namen:
#
#
#

########## HILFSFUNKTION ##########

# gibt alle Paare von unterscheidbaren Zustaenden in A zurueck
def deaUnterscheidbareZustaende(A):
    [Sigma, Z, delta, z0, F] = A
    markiert = list()
    tabelle = []
    zeile = 0
    aenderung = True
    for i in range(len(Z)): # hier wir konstruieren unsere Treppentabelle, wir setzen am Anfang alle Zellen auf 0
                                    # 0 ==> nicht Unterscheidbar , 1 ==> Unterscheidbar
        tabelle.append([0] * zeile)
        zeile += 1
    for i in F:  # Nach dieser Schleife wir haben alle paare von nichtakzeptierenden Zustände und akzeptierenden Zustände mit 1 markiert.
        for j in Z:
            if i != j:  # dadurch wird die unterscheidung von einem Zustand mit sich selbst nicht gemacht
                if j not in F: # Um nicht 2 akzeptierenden Zustände zu betrachten
                    tabelle[max(i, j) - min(Z)][min(i, j) - min(Z)] = 1 #min(Z) ist der Zustand mit der kleinster Nummer
                                                            # und i, j sind genau die Nummern von Zustände
                                                #Wir substrahieren i oder j mit min(Z) um genau die Indexe im Tabelle zu bekommen
                                                # Falls min(Z) = 0, die Nummern von Zustände entsprechen genau die Index in der Tabelle
                    markiert.append({i, j})
    while aenderung == True:
        aenderung = False
        for i in range(len(tabelle)):
            for j in range(len(tabelle[i])):
                    if (tabelle[i][j] == 0):
                        for zeichen in Sigma:
                            if {delta[(i + min(Z), zeichen)], delta[(j + min(Z), zeichen)]} in markiert: # i und j sind hier Index im Tabellle
                                markiert.append({i + min(Z), j + min(Z)})             # wir addieren mit min(Z) um genau die Nummern von Zustände zu bekommen
                                tabelle[i][j] = 1
                                aenderung = True # wenn ein unterscheidbares Paar gefunden wurde, muss man die Tabelle wieder komplett durchlaufen, deswegen True gesetzt.

                                break  # Bei einlesen von einem Zeichen, wir haben schon ein Zeugewort für die akuelle bearbeitete
                                      # paare von Zustände i und j gefunden also es ist nicht mehr nötig die Unterscheidbarkeit
                                        # von dem Paar {i,j} zu überprüfen, deswegen brechen wir die Berechnung ab.
    return markiert # hält die Paare von unterscheidbaren Zustände in einer Liste.


########## HAUPTFUNKTION ########## (Namen und Signatur nicht ändern!)

def deasAequivalent(A, B):  # prueft, ob DEAs A und B die gleiche Sprache akzeptieren
    [ASigma, AZ, Adelta, Az0, AF] = A
    [BSigma, BZ, Bdelta, Bz0, BF] = B
    Sigma = ASigma  # Annahme: ASigma = BSigma
    Z =  AZ.union(BZ)
    Adelta.update(Bdelta)
    F =  AF.union(BF)
    C = [Sigma, Z, Adelta, Az0, F]
    return {Az0, Bz0} not in deaUnterscheidbareZustaende(C)

if __name__ == '__main__':
            #Beispiel 3.41 Unterscheidbarkeit
    Sigma = {0,1}
    Z = {0,1,2,3,4,5,6}
    delta = {(0,0):1, (0,1):4, (1,0):5, (1,1):2, (2,0):0, (2,1):2, (3,0):6, (3,1):4, (4,0):2, (4,1):5, (5,0):5, (5,1):3, (6,0):5, (6,1):2}
    z0 = 0
    F = {2}
    A = [Sigma, Z, delta, z0, F]
            # Beispeil 3.43 ÄquivalenzTest
    #DEATest_1
    ASigma = {0,1}
    AZ = {0,1}
    Adelta = {(0,0):0, (0,1):1, (1,0):0, (1,1):1}
    Az0 = 0
    AF ={0}
    A11 = [ASigma, AZ, Adelta, Az0, AF]

    #DEATest_2
    BSigma = {0,1}
    BZ = {2,3,4}
    Bdelta = {(2,0): 3,(2,1): 4, (3,0):3, (3,1):4, (4,0):2, (4,1):4}
    Bz0 = 2
    BF = {2, 3}
    A22 = [BSigma, BZ, Bdelta, Bz0, BF]

        # Aufgabe2

    #Automat1
    A1Sigma = {'a', 'b', 'c'}
    A1Z = {1, 2, 3}
    A1delta = {(1, 'a'):2, (1, 'b'):2, (1, 'c'):2, (2, 'a'):3, (2, 'b'):3, (2, 'c'):3, (3, 'a'):1, (3, 'b'):1, (3, 'c'):1}
    A1z0 = 1
    A1F = {1}
    A1 = [A1Sigma, A1Z, A1delta, A1z0, A1F]

    #Automat2
    A2Sigma = {'a', 'b', 'c'}
    A2Z = {4, 5, 6, 7, 8}
    A2delta = {(4, 'a'):7, (4, 'b'):6, (4, 'c'):7, (5, 'a'):4, (5, 'b'):4, (5, 'c'):4, (6, 'a'):5, (6, 'b'):8, (6, 'c'):5, (7, 'a'):8, (7, 'b'):8, (7, 'c'):5, (8, 'a'):4, (8, 'b'):4, (8, 'c'):4}
    A2z0 = 4
    A2F = {4}
    A2 = [A2Sigma, A2Z, A2delta, A2z0, A2F]

    #Simulation von beispiele aus dem Script
    print(deaUnterscheidbareZustaende(A)) #Beispiel 3.41 aud der Vorlesung: Unterscheidbarkeit Algorithmus
    print("Beispiel 3.43", deasAequivalent(A11, A22))  #Beispiel 3.43: AequivalenzTesst für DEA.

    #Simulation von Aufgabe 2
    print("Aufgabe2", deasAequivalent(A1, A2))