class auto:

    # Attributi di Classe
    garanzia = 1
    negoziocellulare = 0

    #Metodo costruttore
    def _init_(self,proprietario, marca, modello, spazio, dimensione, colore):

        # Attributi di Istanza
        self.proprietario = proprietario
        self.marca = marca
        self.modello = modello
        self.spazio = spazio
        self.dimensione = dimensione
        self.colore = colore
        
        auto.parcoAuto +=1

    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n Marca: {self.marca}\n Modello: {self.modello}\n spazio: {self.spazio}\n dimensione: {self.dimensione}\n colore: {self.colore}\n assicurazione: {self.assicurazione}' 
    
sara = cellulare("sara","samsung","Z flip3", 256, 72, "bianco")

mike = celulare("mike","iphone","13pro", 512, 75, "azzurro")

print("Il tipo di variabile costruita è:")
print(sara)
print(mike)

print("\nLa singola scheda è:")
print (sara.scheda())
print (mike.scheda())
print("\nauto totali: ",cellulare.negoziocellulare)

print("\n\naltro metodo per visualizzare le informazioni (_dict_):")

print(sara._dict_)
print(mike._dict_)
