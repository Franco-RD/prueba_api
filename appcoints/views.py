class Views():
    def insertCoin(self):
        moneda_cripto = input("Ingrese una moneda conocida: ").upper()
        return moneda_cripto
    
    def viewListCoins(self, allcoint):
        print(f"Total: {len(allcoint.lista_general)} \nCriptos: {len(allcoint.lista_criptos)} \nNo criptos: {len(allcoint.lista_no_criptos)}")

    def viewRateExchange(self, change):
        print(f"Fecha de consulta: {change.time}" + "\nRate: {:.2f}€".format(change.rate))

    def viewRateExchange2(self, change):
        print(f"Fecha de consulta: {change.time} \nRate: {change.rate} BTC")

    def getError(self, error):
        print(error)

        