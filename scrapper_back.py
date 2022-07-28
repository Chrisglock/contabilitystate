import sys
import json
import os
import re
import time
from pathlib import Path 

start_time = time.time()

def scrape(cuenta,maxitems,tipo):
    os.system("instagram-scraper "+ cuenta +" -u ellocokriz@gmail.com -p petrol7272 --quiet --destination scrapeos/" + cuenta +" --media-types "+ tipo + " --media-metadata --maximum " + str(maxitems))
    
def opendatacuenta(cuenta):
    ct="scrapeos/"+cuenta+"/"+cuenta+".json"
    f = open(ct, encoding = "utf8")
    data = json.load(f)
    f.close()
    return data

def getdesc(data,numimg):
    desc = "Sin Descripcion"
    tipo = data["GraphImages"][numimg]["edge_media_to_caption"]["edges"]
    if tipo != []:
        desc = data["GraphImages"][numimg]["edge_media_to_caption"]["edges"][0]["node"]["text"]
    return desc

def get_url(data,numimg):
    link = "Sin link"
    tipo = data["GraphImages"][numimg]["shortcode"]
    if tipo != []:
        link = data["GraphImages"][numimg]["shortcode"]
        link = "instragram.com/p/"+link
        
    return link

def savedesc(data,numdata):
    array1 = []
    if numdata == 0:
        numdata = len(data["GraphImages"])
    for i in range(0,numdata,1):
        array1.append(getdesc(data,i))
    return array1

def saveurls(data,numdata):
    array1 = []
    for i in range(0,numdata,1):
        array1.append(get_url(data,i))
    return array1

def getprices(descripciones):
    precios = []
    for i in descripciones:
        i = i[0] #toma la primera palabra de la descripcion
        peso_position = i.find("$") #busca posicion de las palabras que contienen $
        if peso_position != -1: # si la palabra contiene $
            i = i[peso_position:len(i)] #toma la descripcion desde el signo $ hasta el resto
            i = i.split(" ")[0] #separa la descripcion restante por espacios
            i = i.replace(".","")#quita los puntos de las palabras
            i = re.findall(r'\d+',i)[0] #encuentra la primera palabra 
            i = "$"+i #se le agrega el signo peso que se pierde
            precios.append(i) #se añade a precios
        else:
            precios.append("null")
    return precios

def filter_desc(descripciones,urls,palabra):# filtra las descripciones que contengan una palabra
    desc = []
    for i in range(len(descripciones)):
        desc_actual = descripciones[i].lower()
        peso_position = desc_actual.find(palabra)
        if peso_position != -1:
            desc.append([desc_actual])
    return desc

def filter_urls(descripciones,urls,palabra):# filtra las descripciones que contengan una palabra
    url = []
    for i in range(len(descripciones)):
        desc_actual = descripciones[i].lower()
        url_actual = urls[i]
        peso_position = desc_actual.find(palabra)
        if peso_position != -1:
            url.append([url_actual])
    return url


def concatenate_data(tipo,descripcion,urls,precio):
    productos = []
    for i in range(len(descripcion)):
        productos.append([str(tipo),str(descripcion[i][0]),str(urls[i][0]),str(precio[i])])
    return productos
def search(cuenta,busqueda,datos):
    #se setea la data
    cuenta_objetivo = str(cuenta)
    BUSCAR = str(busqueda)
    numero_datos = int(datos) # 0 para todos los datos
    item_buscado = BUSCAR.lower()
    #print(item_buscado)
    

    #                    se scrapea la cuenta
    ruta = "scrapeos/" +  cuenta_objetivo + "/" + cuenta_objetivo + ".json"
    fileObj = Path(ruta)
    if fileObj.is_file() == False:
        
        scrape(cuenta_objetivo,50,"none") #se consugue la data mediante scraping
        

    #              se abre la data y guardan las descripciones
    data = opendatacuenta(cuenta_objetivo) #se abre la data de la cuenta
    
    max_num_datos=len(data["GraphImages"])
    if numero_datos == 0 or numero_datos>max_num_datos:
        numero_datos = len(data["GraphImages"])
        
    descripciones_raw = savedesc(data,numero_datos) #se obtienen las descripciones, entre todo la data
    urls_raw = saveurls(data,numero_datos)

    #           se hace filtro por producto buscado
    filtrados = filter_desc(descripciones_raw ,urls_raw,item_buscado) # se buscan las descripciones que contenga cierta palabra
    precios = getprices(filtrados)
    urls_filtradas = filter_urls(descripciones_raw ,urls_raw,item_buscado)
    productos_listos = concatenate_data(item_buscado,filtrados,urls_filtradas,precios)
    #ventana.e_carga() 
    return productos_listos