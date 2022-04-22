
                            
def creation_liste(mot):
    liste = []
    for i in range(len(mot)):
        liste.append([])
    return liste

def split(word):
    return [char for char in word]

def supersimple(grey,green,yellow,tentatives_possibles):
    
    for i in range(len(grey)):
        for j in reversed(range(len(tentatives_possibles))):
            if grey[i] in split(tentatives_possibles[j]):
                tentatives_possibles.pop(j)
    
    for i in range(len(green)):
        for j in reversed(range(len(tentatives_possibles))):
            for u in range(len(split(green[i]))):
                if split(green[i])[u].isalpha():    
                    if green[i] != split(tentatives_possibles[j])[i]:
                            tentatives_possibles.pop(j)
    
    for i in range(len(yellow)):
        for j in reversed(range(len(tentatives_possibles))):
            for u in range(len(split(yellow[i]))):
                if split(yellow[i])[u].isalpha():    
                    if yellow[i][u] == split(tentatives_possibles[j])[i]:
                            tentatives_possibles.pop(j)
                    elif yellow[i][u] not in split(tentatives_possibles[j]):
                            tentatives_possibles.pop(j)
                            
def fonction_mot_test():
    while True : 
        mot_test = input("Input a 5 letter word : ")
        #mot_test=random.choice(tentatives_possibles)
        if not (mot_test.lower() in allowed_words):
            continue
        else :
            mot_test = mot_test.lower()
            break
    return mot_test
