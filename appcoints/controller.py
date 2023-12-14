from appcoints.config import APIKEY
from appcoints.model import *
from appcoints.views import *

class AppCoinsController:
    def executeProgram(self):
        allcoint = AllCointsApiIO()
        allcoint.getAllCoins(APIKEY)

        viewTools = Views()

        viewTools.viewListCoins(allcoint=allcoint)  #El parametro se pasa con = porque se llama exactamente igual el objeto que el parametro declarado en el metodo de la clase

        ########################################################################################################

        moneda_cripto = viewTools.insertCoin()

        while moneda_cripto != '' and moneda_cripto.isalpha():
            if moneda_cripto in allcoint.lista_no_criptos:  #Poner lista_criptos y viewTools.viewExchangeRate(exchange) para pasar de cripto a euro
                exchange = Exchange(moneda_cripto)
                try:
                    exchange.updateExchange(APIKEY)
                    viewTools.viewRateExchange2(exchange)
                except ModelError as error:
                    viewTools.getError(error=error)            

            moneda_cripto = viewTools.insertCoin()
