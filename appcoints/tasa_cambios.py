import requests 

apikey = '046BC141-EE9A-429C-AB7A-14953FA91D43'
moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()

#Invocando al metodo get con url especifica
url = f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}'

r = requests.get(url)  #Hace un get a la url y guarda lo obtenido en la variable r

"""
print("Codigo http de respuesta: ", r.status_code)  #Status code da el codigo de respuesta (200, 404, etc.)
print("Cabecera: ", r.headers['content-type'])  #r.headers obtiene la cabecera 
print("Encoding: ", r.encoding)  #Obtiene el encodeo
print("Respuesta en str: ", r.text)  #Obtiene lo del get en formato texto
print("Respuesta en JSON: ", r.json())  #Obtiene lo del get en formato JSON, y siempre va con () porque es un metodo. Para py los JSON son como diccionarios
print(r.json()['time'])
"""

#Ej 1, como capturar el rate.
respuesta = r.json()  #Guardo el JSON en una variable que queda como diccionario
#print("Rate: ", respuesta['rate'])


#Ej 2, como capturo errores de peticion http.
if r.status_code == 200:
    print("Rate: ", respuesta['rate'])  #Cuando todo funciona el JSON da un diccionario con unas claves particulares (diccionario respuesta en pruebas)
else:
    print("Error: ", respuesta['error'])  #Cuando da un error porque la url esta mal, da otro diccionario (tambien en pruebas), que la key que tiene se llama 'error'. 
