 #On importe les modules nécessaires

import tkinter as tk

from tkinter import ttk

import random

import GenerationOnglets as go

import DinosauresClasses as dino

import const

import pygame


tabNbTriceratopsTemps = []

tabNbStegosauridaeTemps = []

tabNbTyrannosaureTemps = []

tabNbAllosaurusTemps = []


#Nombre de chaque population



#-------------Générateur aléatoire----------


def Naissance(nomDinosaure):

		compteurJours = 0

		while compteurJours != nbJoursNaissance:

			compteurJours = compteurJours + 1
	
		#Ici on créer un objet du dinausaure voulu

		if nomDinosaure == "Triceratops":

			sexeAleatoire = random.random()

			if sexeAleatoire <= 0.50:

				listeTriceratopsMales.append(dino.Triceratops(GenerateurPoids(), "male"))

			else:

				listeTriceratopsFemelles.append(dino.Triceratops(GenerateurPoids(), "femelle"))	

	
		if nomDinosaure == "Stegosauridae":

			sexeAleatoire = random.random()

			if sexeAleatoire <= 0.50:

				listeStegosauridaesMales.append(dino.Stegosauridae(GenerateurPoids(), "male"))

			else:
				
				listeStegosauridaesFemelles.append(dino.Stegosauridae(GenerateurPoids(), "femelle"))


		if nomDinosaure == "Tyrannosaure":

			sexeAleatoire = random.random()

			if sexeAleatoire <= 0.50:

				listeTyrannosauresMales.append(dino.Tyrannosaure(GenerateurPoids(), "male"))

			else:
				
				listeTyrannosauresFemelles.append(dino.Tyrannosaure(GenerateurPoids(), "femelle"))	


		if nomDinosaure == "Allosaurus":

			sexeAleatoire = random.random()

			if sexeAleatoire <= 0.50:

				listeAllosaurusMales.append(dino.Allosaurus(GenerateurPoids(), "male"))

			else:
				
				listeAllosaurusFemelles.append(dino.Allosaurus(GenerateurPoids(), "femelle"))	



def GenerateurAleatoireAction(isPregnant, nomDinosaure, obj):


	compteurTemps = 0 #Le compteur qui repésente le temps


	nbAleatoire = random.randint(1, 3) 	#On génére un nombre aléatoire entre 0 et 1

	#Pour l'instant, seulement deux actions sont notées

	nutrition = 0 # Temps passé après la nutrition

	reproduction = 0 # Temps passé après la reproduction
	

	if nomDinosaure == "Triceratops":

			tempsNutrition = creationTab1.valeurTempsNutrition.get()

			tempsReproduction = creationTab1.valeurTempsReproduction.get()


	elif nomDinosaure == "Stegosauridae":

		tempsNutrition = creationTab2.valeurTempsNutrition.get()

		tempsReproduction = creationTab2.valeurTempsReproduction.get()


	elif nomDinosaure == "Tyrannosaure":

		tempsNutrition = creationTab3.valeurTempsNutrition.get()

		tempsReproduction = creationTab3.valeurTempsReproduction.get()

	else:

		tempsNutrition = creationTab4.valeurTempsNutrition.get()

		tempsReproduction = creationTab4.valeurTempsReproduction.get()


	"""
	if isPregnant:

		Naissance(nomDinosaure)

	#if #la case sur laquelle se trouve le dinosaures est une plantes ou un autre dinosaures: 

		#On appelle les fonctions adéquates
	"""
	

	if nbAleatoire == 1:


		if nutrition == tempsNutrition: #Si le dernier repas a eu lieu il y a "tempsNutrition" heure(s) alors
			
			obj.Eat()

			nutrition = 0
				
		else:
			
			nutrition = nutrition + 1



	elif nbAleatoire == 2: 

		listeDirection = ["N", "S", "E", "O"]

		directionAleatoire = random.choice(listeDirection) #On choisi aléatoirement la direction du déplacement 


		obj.seDeplace(directionAleatoire);


	
	else:


		if reproduction == tempsReproduction: #Si le dernier repas a eu lieu il y a "tempsReproduction" heure(s) alors
			
			#On met la fonction pour se reproduire

				#obj.reproduction(obj.life)

				#reproduction = 0
				pass
			
		#else:
			
			#reproduction = reproduction + 1


	compteurTemps = compteurTemps + 1 #Pour les graphiques, à chaque fin de cycles, on incrémente cette variable
									  #qui correspond au temps. 1 = 1 heure



    #Ici on ajoute le nb d'individus de chaque population pour tracer la courbe

	tabNbTriceratopsTemps.append(nbTriceratops)

	tabNbStegosauridaeTemps.append(nbStegosauridae)

	tabNbTyrannosaureTemps.append(nbTyrannosaure)

	tabNbAllosaurusTemps.append(nbAllosaurus)

	

def PositionAleatoire():

	position = []

	positionAleatoireX = random.randint(0, 26)

	position.append(positionAleatoireX)

	positionAleatoireY = random.randint(0, 26)

	position.append(positionAleatoireY)


	return position




#------------------------Fonction principale------------------------



def Start():

	#Création des listes contenant les populations

	listeTriceratopsMales = []
	listeTriceratopsFemelles = []

	listeStegosauridaesMales = []
	listeStegosauridaesFemelles = []

	listeTyrannosauresMales = []
	listeTyrannosauresFemelles = []

	listeAllosaurusMales = []
	listeAllosaurusFemelles = []



	
	pygame.init()

	# Création du DISPLAY
	screen = pygame.display.set_mode((const.W_WIDTH, const.W_HEIGHT))

	# Definition du nom de programme
	pygame.display.set_caption("Ecosysteme_Jurassystem")

	# Création de la grille
	grid = dino.Terrain("map")
	grid.generate()
	

	my_sprites = pygame.sprite.Group()



	#---------------------------Création des objets---------------------------------

	#Pour les Triceratops mâles

	nbMalesTab1 = creationTab1.valeurMales.get()

	while nbMalesTab1 != 0:

		positionTriceratopsMales = PositionAleatoire()


		while grid.grid[positionTriceratopsMales[0]][positionTriceratopsMales[1]] != "0" or grid.grid[positionTriceratopsMales[0]][positionTriceratopsMales[1]] == "1":

			positionTriceratopsMales = PositionAleatoire()


		listeTriceratopsMales.append(dino.Triceratops(100, False, positionTriceratopsMales[0], positionTriceratopsMales[1], grid, "Triceratops", "Male"))


		nbMalesTab1 = nbMalesTab1 - 1



	#Pour les Triceratops femelles

	nbFemellesTab1 = creationTab1.valeurFemelles.get()

	while nbFemellesTab1 != 0:

		positionTriceratopsFemelles = PositionAleatoire()


		while grid.grid[positionTriceratopsFemelles[0]][positionTriceratopsFemelles[1]] != "0" or grid.grid[positionTriceratopsFemelles[0]][positionTriceratopsFemelles[1]] == "1":

			positionTriceratopsFemelles = PositionAleatoire()



		listeTriceratopsFemelles.append(dino.Triceratops(100, False, positionTriceratopsFemelles[0], positionTriceratopsFemelles[1], grid, "Triceratops", "Femelle"))

		nbFemellesTab1 = nbFemellesTab1 - 1

	

	#Pour les Stegosauridae mâles

	nbMalesTab2 = creationTab2.valeurMales.get()

	while nbMalesTab2 != 0:

		positionStegosauridaeMales = PositionAleatoire()

		while grid.grid[positionStegosauridaeMales[0]][positionStegosauridaeMales[1]] != "0" or grid.grid[positionStegosauridaeMales[0]][positionStegosauridaeMales[1]] == "1":
				

			positionStegosauridaeMales = PositionAleatoire()

		listeStegosauridaesMales.append(dino.Stegosauridae(100, False, positionStegosauridaeMales[0], positionStegosauridaeMales[1], grid, "Stegosauridae", "Male"))

		nbMalesTab2 = nbMalesTab2 - 1

	

	#Pour les Stegosauridae Femelles

	nbFemellesTab2 = creationTab2.valeurFemelles.get()

	while nbFemellesTab2 != 0:

		positionStegosauridaeFemelles = PositionAleatoire()

		while grid.grid[positionStegosauridaeFemelles[0]][positionStegosauridaeFemelles[1]] != "0" or grid.grid[positionStegosauridaeFemelles[0]][positionStegosauridaeFemelles[1]] == "1":
			positionStegosauridaeFemelles = PositionAleatoire()

		listeStegosauridaesFemelles.append(dino.Stegosauridae(100, False, positionStegosauridaeFemelles[0], positionStegosauridaeFemelles[1], grid, "Stegosauridae", "Femelle"))

		nbFemellesTab2 = nbFemellesTab2 - 1


	
			#Pour les Tyrannosaure mâles

	nbMalesTab3 = creationTab3.valeurMales.get()

	while nbMalesTab3 != 0:

		positionTyrannosaureMales = PositionAleatoire()

		while grid.grid[positionTyrannosaureMales[0]][positionTyrannosaureMales[1]] != "0" or grid.grid[positionTyrannosaureMales[0]][positionTyrannosaureMales[1]] == "1":

			positionTyrannosaureMales = PositionAleatoire()

		listeTyrannosauresMales.append(dino.Tyrannosaure(100, False, positionTyrannosaureMales[0], positionTyrannosaureMales[1], grid, "Tyrannosaure", "Male"))

		nbMalesTab3 = nbMalesTab3 - 1



	#Pour les Tyrannosaure femelles

	nbFemellesTab3 = creationTab3.valeurFemelles.get()

	while nbFemellesTab3 != 0:

		positionTyrannosaureFemelles = PositionAleatoire()

		while grid.grid[positionTyrannosaureFemelles[0]][positionTyrannosaureFemelles[1]] != "0" or grid.grid[positionTyrannosaureFemelles[0]][positionTyrannosaureFemelles[1]] == "1":
			positionTyrannosaureFemelles = PositionAleatoire()

		listeTyrannosauresFemelles.append(dino.Tyrannosaure(100, False, positionTyrannosaureFemelles[0], positionTyrannosaureFemelles[1], grid, "Tyrannosaure", "Femelle"))

		nbFemellesTab3 = nbFemellesTab3 - 1



	#Pour les Allosaurus mâles

	nbMalesTab4 = creationTab4.valeurMales.get()

	while nbMalesTab4 != 0:

		positionAllosaurusMales = PositionAleatoire()

		while grid.grid[positionAllosaurusMales[0]][positionAllosaurusMales[1]] != "0" or grid.grid[positionAllosaurusMales[0]][positionAllosaurusMales[1]] == "1":
			positionAllosaurusMales = PositionAleatoire()

		listeAllosaurusMales.append(dino.Allosaurus(100, False, positionAllosaurusMales[0], positionAllosaurusMales[1], grid, "Allosaurus", "Male"))

		nbMalesTab4 = nbMalesTab4 - 1




	#Pour les Allosaurus femelles

	nbFemellesTab4 = creationTab4.valeurFemelles.get()

	while nbFemellesTab4 != 0:

		positionAllosaurusFemelles = PositionAleatoire()

		while grid.grid[positionAllosaurusFemelles[0]][positionAllosaurusFemelles[1]] != "0" or grid.grid[positionAllosaurusFemelles[0]][positionAllosaurusFemelles[1]] == "1":
			positionAllosaurusFemelles = PositionAleatoire()

		listeAllosaurusFemelles.append(dino.Allosaurus(100, False, positionAllosaurusFemelles[0], positionAllosaurusFemelles[1], grid, "Allosaurus", "Femelle"))

		nbFemellesTab4 = nbFemellesTab4 - 1
	


	
	
	#Boucle pour créer les sprites pour chaques objets

	for i in listeTriceratopsMales:

		i.attributionEspece()

		my_sprites.add(i)

	for i in listeTriceratopsFemelles:

		i.attributionEspece()

		my_sprites.add(i)
	

	for i in listeStegosauridaesMales:

		i.attributionEspece()

		my_sprites.add(i)

	for i in listeStegosauridaesFemelles:

		i.attributionEspece()

		my_sprites.add(i)

	for i in listeTyrannosauresMales:

		i.attributionEspece()

		my_sprites.add(i)

	for i in listeTyrannosauresFemelles:

		i.attributionEspece()

		my_sprites.add(i)

	for i in listeAllosaurusMales:

		i.attributionEspece()

		my_sprites.add(i)

	for i in listeAllosaurusFemelles:

		i.attributionEspece()

		my_sprites.add(i)


	#Apparition des plantes
	
	listePlantes = []

	nbPlantes = random.randint(0, 729)

	while nbPlantes != 0:

		positionPlante = PositionAleatoire()
	
		while grid.grid[positionPlante[0]][positionPlante[1]] != "0" or grid.grid[positionPlante[0]][positionPlante[1]] == "1":

			positionPlante = PositionAleatoire()

		listePlantes.append(dino.Plant(positionPlante[0], positionPlante[1], grid))


		nbPlantes = nbPlantes - 1


	for i in listePlantes:

		my_sprites.add(i)

		i.appear()


	#**********************Boucle principale***********************

	
	

	run = True

	while run:

	    
	    pygame.time.delay(70)

	    for event in pygame.event.get():
	    	if event.type == pygame.QUIT: # Si le programme est éteint la boucle est fermée
	    		run = False


	    for i in listeTriceratopsMales:
	    		
	    	GenerateurAleatoireAction(i.pregnant, "Triceratops", i)

	    	i.life = i.life - 1

	    	if i.life == 0:
	
	    		del listeTriceratopsMales[listeTriceratopsMales.index(i)] #On supprime l'objet de la liste d'objets
	    		my_sprites.remove(i) #On supprime la sprite de l'écran
	    		i.remove() #On supprime l'objet

	    
	    for i in listeTriceratopsFemelles:
	    		
	    	GenerateurAleatoireAction(i.pregnant, "Triceratops", i)

	    	i.life = i.life - 1

	    	if i.life == 0:

	    		my_sprites.remove(i) #On supprime la sprite de l'écran
	    		i.remove() #On supprime l'objet
	    		del listeTriceratopsFemelles[listeTriceratopsFemelles.index(i)] #On supprime l'objet de la liste d'objets	    	

	    		

	    		print(listeTriceratopsFemelles)

	    for i in listeStegosauridaesMales:

	    	GenerateurAleatoireAction(i.pregnant, "Stegosauridae", i)
	    	
	    	i.life = i.life - 1

	    	if i.life == 0:
	    		i.remove()
	    		del listeStegosauridaesMales[listeStegosauridaesMales.index(i)]
	    		my_sprites.remove(i)
		
		
	    for i in listeStegosauridaesFemelles:

	    	GenerateurAleatoireAction(i.pregnant, "Stegosauridae", i)

	    	i.life = i.life - 1
	    	
	    	if i.life == 0:
	    		i.remove()
	    		del listeStegosauridaesFemelles[listeStegosauridaesFemelles.index(i)]
	    		my_sprites.remove(i)
			
	    for i in listeTyrannosauresMales:

	    	GenerateurAleatoireAction(i.pregnant, "Tyrannosaure", i)

	    	i.life = i.life - 1

	    	if i.life == 0:
	    		i.remove()
	    		del listeTyrannosauresMales[listeTyrannosauresMales.index(i)]
	    		my_sprites.remove(i)

	    for i in listeTyrannosauresFemelles:

	    	GenerateurAleatoireAction(i.pregnant, "Tyrannosaure", i)

	    	i.life = i.life - 1

	    	if i.life == 0:
	    		i.remove()
	    		del listeTyrannosauresFemelles[listeTyrannosauresFemelles.index(i)]
	    		my_sprites.remove(i)

	    for i in listeAllosaurusMales:

	    	GenerateurAleatoireAction(i.pregnant, "Allosaurus", i)

	    	i.life = i.life - 1

	    	if i.life == 0:
	    		i.remove()
	    		del listeAllosaurusMales[listeAllosaurusMales.index(i)]
	    		my_sprites.remove(i)

	    for i in listeAllosaurusFemelles:

	    	GenerateurAleatoireAction(i.pregnant, "Allosaurus", i)

	    	i.life = i.life - 1

	    	if i.life == 0:
	    		i.remove()
	    		del listeAllosaurusFemelles[listeAllosaurusFemelles.index(i)]
	    		my_sprites.remove(i)
	    my_sprites.draw(screen)
	    grid.displayGrid(screen)
	    pygame.display.flip()
	pygame.quit()
		


#---------------------------Gestion principale de la simulation-------------------------



if __name__ == '__main__':


	#On créer la fenêtre

	mainWindow = tk.Tk()


	#On définit la taille de la fenêtre

	mainWindow.geometry("800x700")
			
	mainWindow.title("Simulation d'écosystème")

	#On créer les onglets

	tabsBar = ttk.Notebook(mainWindow)
	tabsBar.pack(fill = tk.BOTH)


	tab1 = ttk.Frame(tabsBar)
	tab1.pack()


	tab2 = ttk.Frame(tabsBar)
	tab2.pack()


	tab3 = ttk.Frame(tabsBar)
	tab3.pack()


	tab4 = ttk.Frame(tabsBar)
	tab4.pack()


	tab5 = ttk.Frame(tabsBar)
	tab5.pack()


	tabsBar.add(tab1, text = "Tricératops")
	tabsBar.add(tab2, text = "Stegosauridae")
	tabsBar.add(tab3, text = "Tyrannosaure")
	tabsBar.add(tab4, text = "Allosaurus")
	tabsBar.add(tab5, text = "Statistiques")



	creationTab1 = go.Onglet("Nom : Tricératops", "Catégorie : Herbivore", "Comportement : agressif envers les plantes", "Images/Triceratops.pgm", tab1)

	creationTab2 = go.Onglet("Nom : Stegosauridae", "Catégorie : Herbivore", "Comportement : agressif envers les plantes", "Images/Stegosauridae.pgm", tab2)

	creationTab3 = go.Onglet("Nom : Tyrannosaure", "Catégorie : Carnivore", "Comportement : agressif envers les dinosaures", "Images/Tyrannosaure.pgm", tab3)

	creationTab4 = go.Onglet("Nom : Allosaurus", "Catégorie : Carnivore", "Comportement : agressif envers les dinosaures", "Images/Allosaurus.pgm", tab4)

	creationTab5 = go.OngletsStastistiques(tab5)


	creationTab1.Creation()
	creationTab2.Creation()
	creationTab3.Creation()
	creationTab4.Creation()

	creationTab5.Creation()

	nbTriceratops = (creationTab1.valeurMales.get() + creationTab1.valeurFemelles.get())

	nbStegosauridae = (creationTab2.valeurMales.get() + creationTab2.valeurFemelles.get())

	nbTyrannosaure = (creationTab3.valeurMales.get() + creationTab3.valeurFemelles.get())

	nbAllosaurus = (creationTab4.valeurMales.get() + creationTab4.valeurFemelles.get())


	#-------------------------Création des boutons-------------------------

		#-------------------------Tab1-------------------------

	creationTab1.boutonLancer = tk.Button(creationTab1.buttonSection, text = "Lancer la simulation", width = 25, command = lambda: Start()).grid(row = 14, column = 2)

	creationTab1.boutonArreter = tk.Button(creationTab1.buttonSection, text = "Arrêter la simulation", width = 25, command = lambda: Arret()).grid(row = 14, column = 4)

		#-------------------------Tab2-------------------------

	creationTab2.boutonLancer = tk.Button(creationTab2.buttonSection, text = "Lancer la simulation", width = 25, command = lambda: Start()).grid(row = 14, column = 2)

	creationTab2.boutonArreter = tk.Button(creationTab2.buttonSection, text = "Arrêter la simulation", width = 25, command = lambda: Arret()).grid(row = 14, column = 4)

		#-------------------------Tab3-------------------------

	creationTab3.boutonLancer = tk.Button(creationTab3.buttonSection, text = "Lancer la simulation", width = 25, command = lambda: Start()).grid(row = 14, column = 2)

	creationTab3.boutonArreter = tk.Button(creationTab3.buttonSection, text = "Arrêter la simulation", width = 25, command = lambda: Arret()).grid(row = 14, column = 4)

		#-------------------------Tab4-------------------------


	creationTab4.boutonLancer = tk.Button(creationTab4.buttonSection, text = "Lancer la simulation", width = 25, command = lambda: Start()).grid(row = 14, column = 2)

	creationTab4.boutonArreter = tk.Button(creationTab4.buttonSection, text = "Arrêter la simulation", width = 25, command = lambda: Arret()).grid(row = 14, column = 4)


	mainWindow.mainloop()

	





