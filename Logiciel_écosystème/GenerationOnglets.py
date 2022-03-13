#On importe les modules nécessaires

import tkinter as tk

import Main


class Onglet:

	def __init__(self, name, category, behaviour, image, numTab):

		self.name = name
		self.category = category
		self.behaviour = behaviour
		self.image = image
		self.numTab = numTab


		self.valeurMales = tk.IntVar()
		self.valeurFemelles = tk.IntVar()

		self.valeurTempsNutrition = tk.IntVar()
		self.valeurTempsReproduction = tk.IntVar()

		self.valeurTempsNaissance = tk.IntVar()
	

	def Creation(self):


		#Création du titre de la section
		self.informationsTab1 = tk.Label(self.numTab, borderwidth = 3, relief = "groove", text = "Informations")

		self.informationsTab1.pack(fill = tk.BOTH)


		#Section principale des informations avec l'image

		self.sectionPrincipale = tk.Frame(self.numTab, borderwidth = 3, relief = "groove")

		self.sectionPrincipale.pack()


		self.nom = tk.Label(self.sectionPrincipale, text = self.name).grid(row = 1, column = 1)


		self.categorieTab1 = tk.Label(self.sectionPrincipale, text = self.category).grid(row = 2, column = 1)

		self.comportement1 = tk.Label(self.sectionPrincipale, text = self.behaviour).grid(row = 3, column = 1)


		#On charge l'image et on l'affiche

		self.tab1Image = tk.PhotoImage(file = self.image)

		self.labelImageTab1 = tk.Label(self.sectionPrincipale, image = self.tab1Image).grid(row = 2, column = 3)



		#Section du titre des paramètres

		self.parametersSectionTitle = tk.Label(self.numTab, borderwidth = 3, relief = "groove", text = "Paramètres")

		self.parametersSectionTitle.pack(fill = tk.BOTH)


		#Sections des paramètres

		self.sectionParameters = tk.Frame(self.numTab, borderwidth = 3, relief = "groove")
		self.sectionParameters.pack(side = "bottom")

		#Paramètres nbIndividus

		

		#Paramètres rapport mâles/femelles

		self.rapportMaleFemellesLabel = tk.Label(self.sectionParameters, text = "Rapport Mâles/Femelles :").grid(row = 4, column = 2)


		self.rapportMale = tk.Entry(self.sectionParameters, textvariable = self.valeurMales, width = 2).grid(row = 5, column = 2)


		self.rapportFemelle = tk.Entry(self.sectionParameters, textvariable = self.valeurFemelles, width =2).grid(row = 5, column = 3)
		


		#Temps entre la nutrition

		self.tempsNutritionLabel = tk.Label(self.sectionParameters, text = "Temps entre la nutrition : (en heure)").grid(row = 11, column = 2)

		self.sliderTempsNutrition = tk.Scale(self.sectionParameters, variable = self.valeurTempsNutrition, orient = "horizontal", from_ = 0, to = 24, resolution = 1, tickinterval = 2, length = 250).grid(row = 11, column = 3)


		#Temps entre la reproduction

		self.tempsReproductionLabel = tk.Label(self.sectionParameters, text = "Temps entre la reproduction : (en heure)").grid(row = 12, column = 2)


		self.sliderTempsReproduction = tk.Scale(self.sectionParameters, variable = self.valeurTempsReproduction, orient = "horizontal", from_ = 0, to = 24, resolution = 1, tickinterval = 2, length = 250).grid(row = 12, column = 3)

		self.tempsNaissance = tk.Label(self.sectionParameters, text = "Nombre de jours avant l'accouchement : (en heure) (Max : environ 3 mois)").grid(row = 13, column = 3)

		self.sliderTempsNaissance = tk.Scale(self.sectionParameters, variable = self.valeurTempsNaissance, orient = "horizontal", from_ = 1, to = 2190, resolution = 50, tickinterval = 500, length = 250).grid(row = 14, column = 3)


		self.buttonSection = tk.Frame(self.numTab, borderwidth = 3, relief = "groove")
		self.buttonSection.pack(side = "bottom")

class OngletsStastistiques:

	def __init__(self, numTab):

		self.numTab = numTab

	def Creation(self):

		self.informationsTab5 = tk.Label(self.numTab, borderwidth = 3, relief = "groove", text = "Statistiques")

		self.informationsTab5.pack(fill = tk.BOTH)


		self.sectionPrincipale = tk.Frame(self.numTab, borderwidth = 3, relief = "groove")

		self.sectionPrincipale.pack()


