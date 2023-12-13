# Aplicacion de consulta de valor actual de criptomonedas

Programa hecho en python para recuperar el valor en euros de una criptomoneda
desde www.coinapi.io

## Instalacion
-Obtener una apikey en http://docs.coinapi.io/ ingrese un correo valido y dar click al boton GET A FREE APIKEY

-Renombrar el fichero config_template.py a config.py

-Agregar dentro de config.py el apikey de esta manera: 

```
APIKEY = 'AQUI VA SU APIKEY'
```

## Instalacion de dependencias(librerias)
-Crear un entorno virtual de pyton con alguna de estas maneras:
```
py -m venv entorno
python -m venv entorno
python3 -m venv entorno
```

-Activar el entrono e instalar los requerimientos:
```
Windows: .\venv\Scripts\activate
Mac o Linux: source venv/bin/activate

pip install -r requirements.txt
```

-Utiliza las librerias pytest y requests