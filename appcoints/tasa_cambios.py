import requests 
#from .utils import *  #En este import se pone solo . antes de utils porque el archivo en el que estoy esta a la misma altura que la carpeta utils. 

APIKEY = '046BC141-EE9A-429C-AB7A-14953FA91D43'
moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()


while moneda_cripto != '' and moneda_cripto.isalpha():  #.isalpha() comprueba que todos los caracteres de un str sean letras. Da True si lo son. 

    #Invocando al metodo get con url especifica
    url = f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}'

    r = requests.get(url)  #Hace un get a la url y guarda lo obtenido en la variable r

    #Ej 1, como capturar el rate.
    respuesta = r.json()  #Guardo el JSON en una variable que queda como diccionario
    #print("Rate: ", respuesta['rate'])


    #Ej 2, como capturo errores de peticion http.
    if r.status_code == 200:
        print("Rate: {:.2f}€".format(respuesta['rate']))  #Cuando todo funciona el JSON da un diccionario con unas claves particulares (diccionario respuesta en pruebas)
        break
    else:
        print("Error: ", respuesta['error'])  #Cuando da un error porque la url esta mal, da otro diccionario (tambien en pruebas), que la key que tiene se llama 'error'. 

    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()