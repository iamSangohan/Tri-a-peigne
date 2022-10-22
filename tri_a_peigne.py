import math  

def tri_peigne(tableau):
    permutation = True
    
    #On recupere la longueur du tableau entré en paramètre
    gap = len(tableau)
    
    #Verifier qu'il y a plus d'un element dans le tableau
    while (permutation == True) or  (gap>1):
        permutation = False
        
        #Devise le gap par le facteur de reduction recommandé a 1,3 ou 4/3
        gap = math.floor(gap / 1.3)
        if gap<1 : gap = 1 #On met le gap a 1 si apres la division il est inf a 1
        for i in range(0, len(tableau) - gap):
        #L'operation va etre repeter de 0 a la taille du tableau-gap
            if tableau[i] > tableau[i + gap]:
                permutation = True
                
                #On echange les deux elements
                tableau[i], tableau[i + gap] = tableau[i + gap],tableau[i]
                
    return tableau  

tableau = input("Entrez les valeurs de votre tableau (Separez les elements par un espace) : ")
tableau = tableau.split()
liste = []
for i in list(tableau) :
    liste.append(i)

test = tri_peigne(liste)
print(test)