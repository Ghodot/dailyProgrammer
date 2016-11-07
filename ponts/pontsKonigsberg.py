fileInput = "ponts.txt"

graphe = {}

file = open(fileInput,'r')



nbPonts = 0
for line in file:
	nbPonts +=1
	noeuds = line.strip().split(" ")
	noeud1 = noeuds[0]
	noeud2 = noeuds[1]
	#print("-- ITERATION " + str(nbPonts) + " --")
	#print("Graphe : " + str(graphe))
	#print("Noeud 1 : " + str(noeud1))
	#print("Noeud 2 : " + str(noeud2))
	if(not noeud1 in graphe):
		graphe[noeud1] = {noeud2:1}
	elif(not noeud2 in graphe[noeud1]):
		graphe[noeud1][noeud2] = 1
	else:
		graphe[noeud1][noeud2] += 1
	#print("Nouveau graphe : "+str(graphe))
	if(not noeud2 in graphe):
		graphe[noeud2] = {noeud1:1}
	elif(not noeud1 in graphe[noeud2]):
		graphe[noeud2][noeud1] = 1
	else:
		graphe[noeud2][noeud1] += 1
	#print("Nouveau graphe : "+ str(graphe))


cheminsComplets = []


def nbApparitions(element1,element2,liste,):
	compteur = 0
	tuple1 = (element1,element2)
	tuple2 = (element2,element1)
	for x in liste:
		if x == tuple1 or x == tuple2:
			compteur +=1
	return compteur


def parcours(graphe,depart,chemin,longueurActuelle,longueurTotale):
	if(longueurActuelle==longueurTotale):
		global bestChemin
		cheminsComplets.append(chemin)
	else:
		for element in graphe[depart]:
			if not ((depart,element) in chemin or (element,depart) in chemin):
				newChemin = list(chemin)
				newChemin.append((depart,element))
				parcours(graphe,element,newChemin,longueurActuelle+1,longueurTotale)
			elif nbApparitions(depart,element,chemin) < graphe[depart][element]:
				#print("bite : "+str(depart)+" "+str(element)+" "+str(chemin)+" "+str(nbApparitions(depart,element,chemin)))
				newChemin = list(chemin)
				newChemin.append((depart,element))			
				parcours(graphe,element,newChemin,longueurActuelle+1,longueurTotale)

for elementDepart in graphe:
	parcours(graphe,elementDepart,[],0,nbPonts)

print(cheminsComplets)