# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np
import time

ubicacion = 'C:/Users/VDMG015/Desktop/chromedriver.exe'
googleDriver = webdriver.Chrome(ubicacion)


cel_modelo = []
cel_precio = []


for p in np.arange(0,540,60):
    googleDriver.get('https://www.suburbia.com.mx/tienda/nav/blusas/cat-sb-3001/?N=2005922561&No=' + str(p) +'&Nrpp=60&Ntl=es-MX')
    time.sleep(3)
    page = BeautifulSoup(googleDriver.page_source)
    print(p)
    for cel in page.findAll('div', attrs = {'class':'product-list'}):
        modelo = cel.findAll('div', attrs = {'class':'title-item','itemprop':'name'})
        precio = cel.findAll('span', attrs = {'class':'promo-price'})
        for i,j in zip(modelo, precio):
            cel_modelo.append(i.text)
            cel_precio.append(j.text)

lista_celulares_liv = pd.DataFrame({
    'Modelo': cel_modelo,
    'Precio': cel_precio
    })