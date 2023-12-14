from config import APIKEY
from model import *
from views import *

allcoint = AllCointsApiIO()
allcoint.getAllCoins(APIKEY)

viewTools = Views()

viewTools.viewListCoins(allcoint=allcoint)  #El parametro se pasa con = porque se llama exactamente igual el objeto que el parametro declarado en el metodo de la clase

########################################################################################################

moneda_cripto = viewTools.insertCoin()

while moneda_cripto != '' and moneda_cripto.isalpha():
    if moneda_cripto in allcoint.lista_criptos:
        exchange = Exchange(moneda_cripto)
        try:
            exchange.updateExchange(APIKEY)
            viewTools.viewRateExchange(exchange)
        except ModelError as error:
            viewTools.getError(error=error)            

    moneda_cripto = viewTools.insertCoin()
