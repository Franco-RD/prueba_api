from appcoints.model import AllCointsApiIO, Exchange, ModelError
from appcoints.config import APIKEY
import pytest

def test_allcoint():
    listas = AllCointsApiIO()
    listas.getAllCoins(APIKEY)
    assert listas != None  #True
    cantidad = len(listas.lista_criptos) + len(listas.lista_no_criptos)
    assert cantidad == 18516  #True

def test_exchange():
    cambio = Exchange("ETH")
    cambio.updateExchange(APIKEY)
    assert cambio.rate > 0  #True
    assert cambio.rate != None  #True

def test_exchange_error():
    cambio = Exchange("ÑÑÑ")
    
    with pytest.raises(ModelError) as exceptionInfo:
        cambio.updateExchange(APIKEY)
    assert str(exceptionInfo.value) == f"Status: {cambio.status_code}, error: You requested specific single item that we don't have at this moment."
    assert cambio.status_code