import sys

class MetroDirection:


	global nomLignes,arrets,lignes,moinsLong,moinsChangements,
	nomLignes = []
	arrets = {}
	lignes = {}



	def formeLigne(self,nomLigne,ligne):
		apparitions = {}
		ligneTriee = None
		for arret in ligne:
			if not apparitions.has_key(arret):
				apparitions[arret] = 1
			else:
				apparitions[arret] += 1
		for arret in apparitions:
			if apparitions[arret] == 1 and not ligneTriee:
				ligneTriee = [arret]
				arretActuel = arret

		over = False
		while not over:
			over = True
			for arret in arrets[(arretActuel,nomLigne)]:
				if not arret[0] in ligneTriee and arret[1] == nomLigne:
					ligneTriee.append(arret[0])
					arretActuel = arret[0]
					over = False
		return(ligneTriee)




	def __init__(self,sourceFile):
		file = open(sourceFile,'r')
		for line in file:
			infosTrait = line.split(",")
			arret1 = infosTrait[0].strip()
			ligne1 = infosTrait[1].strip()
			arret2 = infosTrait[2].strip()
			ligne2 = infosTrait[3].strip()
			duree =  float(infosTrait[4].strip())
			if arret1 == arret2:
				if not arrets.has_key((arret1,ligne1)):
					arrets[(arret1,ligne1)] = {(arret1,ligne2):duree}
				else:
					arrets[(arret1,ligne1)][(arret1,ligne2)] = duree
				if not arrets.has_key((arret1,ligne2)):
					arrets[(arret1,ligne2)] = {(arret1,ligne1):duree}
				else:
					arrets[(arret1,ligne2)][(arret1,ligne1)] = duree

			else:

				if not lignes.has_key(ligne1):
					lignes[ligne1] = [arret1,arret2]
				else:
					lignes[ligne1].append(arret1)
					lignes[ligne1].append(arret2)

				if not arrets.has_key((arret1,ligne1)):
					arrets[(arret1,ligne1)] = {(arret2,ligne1):duree}
				else:
					arrets[(arret1,ligne1)][(arret2,ligne1)] = duree
				if not arrets.has_key((arret2,ligne1)):
					arrets[(arret2,ligne1)] = {(arret1,ligne1):duree}
				else:
					arrets[(arret2,ligne1)][(arret1,ligne1)] = duree
		for ligne in lignes:
			lignes[ligne] = self.formeLigne(ligne,lignes[ligne])


	def choixDirection(self,depart,destination,ligne):
		if(ligne.index(depart) < ligne.index(destination)):
			return(ligne[len(ligne)-1])
		else:
			return(ligne[0])

	def miseEnFormeSortie(self,itineraire):
		path = itineraire[0]
		duree = itineraire[1]
		
		ligneActuelle = path[0][1]
		direction = self.choixDirection(path[0][0],path[1][0],lignes[ligneActuelle])
		print("A la station " + str(path[0][0]) + " prendre la ligne " + str(ligneActuelle)+" en direction de " + direction)

		indice = -1
		for arret in path:
			indice = indice + 1
			station = arret[0]
			ligne = arret[1]
			if (ligne != ligneActuelle):
				direction = self.choixDirection(station,path[indice+1][0],lignes[ligne])
				print("A l'arret " + station + " changer et prendre la ligne " + ligne + " en direction de " + direction)
				ligneActuelle = ligne
		print("Descendre a " + itineraire[0][len(itineraire[0])-1][0])




	def itineraire(self,depart,arrivee,nbMaxChangements=1,nbChangements=0,path=[],ligneActuelle=None,duree=0):
		if depart == arrivee:
			return((path+[(arrivee,ligneActuelle)],duree))
		if ligneActuelle and nbChangements==nbMaxChangements and not arrivee in lignes[ligneActuelle]:
			return(None)

		best = None

		# Uniquement a la premiere etape
		if not ligneActuelle:
			best = None
			for ligne in lignes:
				if depart in lignes[ligne]:
					actuel = self.itineraire(depart,arrivee,nbMaxChangements,0,[],ligne,0)
					if actuel:
						if (not best or actuel[1] < best[1]):
							best = actuel
			return(best)


		else:
			path = path + [(depart,ligneActuelle)]

			shortest = None
			for destination in arrets[(depart,ligneActuelle)]:
				if destination not in path:
					if(destination[1] != ligneActuelle):
						newPath = self.itineraire(destination[0],arrivee,nbMaxChangements,nbChangements+1,path,destination[1],duree+arrets[(depart,ligneActuelle)][destination])
					else:
						newPath = self.itineraire(destination[0],arrivee,nbMaxChangements,nbChangements,path,destination[1],duree+arrets[(depart,ligneActuelle)][destination])
					if newPath:
						if (not shortest or newPath[1] < shortest[1]):
							shortest = newPath
			return(shortest)



depart = sys.argv[1]
arrivee= sys.argv[2]


reseauMetro = MetroDirection("metroDirections.txt")
chemin = reseauMetro.itineraire(depart,arrivee,5)

reseauMetro.miseEnFormeSortie(chemin)


