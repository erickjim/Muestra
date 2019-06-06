#!/usr/bin/env python
# coding: utf-8

# # Muestra de proyecto

# In[ ]:


import pandas as pd
import os
import collections
import numpy as np
import zipfile 
from __future__ import division


# ## Lectura de Datos

# In[ ]:


#Se leen todas las bases de datos corresp a las diferentes comunidades
a=[]
for i in os.listdir(r'C:/Users/ejimenez/Bases_de_datos/'):
    if (i != '.ipynb_checkpoints') & (i!= 'Carpeta_Orden_Datos') &(i != 'Muestra.ipynb') & (i != 'Comprimidos'):
        a.append(pd.read_excel(i))
        print i


# In[ ]:


b=pd.concat(a)


# ## Creación de carpetas para el ordenamiento de datos ya procesados

# In[ ]:


#Se crean las carpetas donde se guardarán resultados e incidencias (Ahí se guardan los datos ya procesados)
path=r'C:/Users/ejimenez/Bases_de_datos/Carpeta_Orden_Datos'
for i in b['Comunidades'].value_counts().index:
    os.makedirs(path + i)
for i in b['Comunidades'].value_counts().index:
    os.makedirs(path + i + '/Incidencias')
    os.makedirs(path + i + '/Resultados')
#Se crea la carpeta que corresponde a los resultados EDI
for i in b['Comunidades'].value_counts().index:
    os.makedirs(path + i + u'/Resultados/EDI')
#Se exporta la base de datos consolidada
b.to_excel('CVS_2019.xlsx',index=False)


# ## Ejemplo de manipulación de datos.

# In[ ]:


#Creación de nuevas variables de acuerdo a condiciones y criterios de variables ya existentes
b['Variable']=map(lambda x,y,z :u'Sí' if ((x==u'criterio_1') & (y==u'criterio_2')) | ((z==u'Condición_1') & (y==u'criterio_3')) else 'No', b['Variable_1'],b['Variable_2'],b['Variable_3'])


# In[ ]:


#Agrupamiento de datos de acuerdo a condiciones
b[b['Variable']==u'Sí'].groupby(['Comunidades','Otra_variable'])['Libre_de_NAs'].count().unstack().fillna(0)


# ## Procesamiento de datos y guardado de acuerdo a la variable deseada y a la variable Comunidad.

# In[ ]:


for i in b['Comunidades'].value_counts().index:
    variable=b.groupby(['Comunidades','Etapa_de_vida','Variable'])['Libre_de_NAs'].count().unstack().fillna(0).loc[i]
    variable=variable.reset_index().append(variable.sum(numeric_only=True), ignore_index=True)
    tote=list(variable.dropna()['Etapa_de_vida'])
    tote.append('Total')
    variable['Etapa_de_vida']=tote
    variable.to_excel('Carpeta_Orden_Datos/'+ i + '/Resultados/' + u'Niños presentes al momento de la entrevista de acuerdo a etapa de vida.xlsx', index=False)


# ## Compresión de carpetas

# In[ ]:


path=r'C:/Users/ejimenez//Bases_de_datos/Carpeta_Orden_Datos'
for i in b['Comunidades'].value_counts().index:
    zp = zipfile.ZipFile('Comprimidos/'+i+'.zip', 'w')
    for j in os.listdir(path + '/' + i + '/Resultados'):
        if (j != '.ipynb_checkpoints') & (j!= 'EDI'):
            zp.write( 'Carpeta_Orden_Datos/'+i + '/Resultados/'+j )
        else:
            for k in os.listdir(path + '/' + i + '/Resultados/EDI'):
                zp.write( 'Carpeta_Orden_Datos/'+i + '/Resultados/EDI/'+k )
    for j in os.listdir(path + '/' + i + '/Incidencias'):
        if (j != '.ipynb_checkpoints'):
            zp.write( 'Carpeta_Orden_Datos/'+i + '/Incidencias/'+j )
    zp.close()


# In[ ]:




