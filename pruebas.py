respuesta = {
  "time": "2023-12-11T20:03:24.0000000Z",
  "asset_id_base": "EUR",
  "asset_id_quote": "BTC",
  "rate": 0.0000263945958206795136776659
}

error = {
  "error": "You didn\u0027t specify API key or it is incorrectly formatted. You should do it in: query string parameter \u0060apikey\u0060,  in http header named \u0060X-CoinAPI-Key\u0060,  in http header named \u0060Authorization\u0060 or  as part of URL /apikey-YOUR-API-KEY/"
}

"""
print("Codigo http de respuesta: ", r.status_code)  #Status code da el codigo de respuesta (200, 404, etc.)
print("Cabecera: ", r.headers['content-type'])  #r.headers obtiene la cabecera 
print("Encoding: ", r.encoding)  #Obtiene el encodeo
print("Respuesta en str: ", r.text)  #Obtiene lo del get en formato texto
print("Respuesta en JSON: ", r.json())  #Obtiene lo del get en formato JSON, y siempre va con () porque es un metodo. Para py los JSON son como diccionarios
print(r.json()['time'])
"""