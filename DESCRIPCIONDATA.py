# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:46:12 2019

@author: JUAN FELIPE BARBOSA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

# Importar la base de datos 
excel_file = 'base excel.xlsx'
base = pd.read_excel(excel_file)

# Contar el número de observaciones que contiene la base: es este caso nos indica el total de contratos en Cundinamarca y Bogotá
len(base)

# queremos determinar el # de contratos que se han firmado por municipio
contrato_mun = base.groupby('Municipio') # agrupamos la base por cada municipio
contratos = contrato_mun["Municipio"].agg('count') # generamos un contador para que cada observación dependiendo el municipio y sume el total de contratos.
contratos

#queremos determinar el monton de contratación por municipio
valor_mun = base.groupby(['Municipio'])["Valor Inicial"].sum() # generamos una suma del monto de contratación por municipio.
valor_mun

# queremos determinar el # de contratos que se han firmado por Provincia
contratos_provincia = base.groupby('PROVINCIA') # agrupamos la base por cada Provincia
contratosP = contratos_provincia["PROVINCIA"].agg('count') # generamos un contador para que cada observación dependiendo de la provincia y sume el total de contratos por provincia.
contratosP

Contrac=pd.DataFrame(contratosP) # realizamos un data frame con el número de contratos de cada provincia para agragarlo como una lista en el label de nuestra gafica
num_contrac=Contrac.values.tolist()

 # graficamos el número de contratos por provincias con la agrupación que realizamos
gra = contratosP.plot(kind='bar' , figsize = (16,9), fontsize = 15, legend=None);
gra.set_title("Número de contratos por provincias", fontsize=30, fontname="Verdana")
# con el data frame creado anteriormente vamos a agregarlo en el label de la grafica
for i in gra.patches:
    num_contrac.append(i.get_width())

# aqui agregamos la etiqueta a cada barra de la grafica
for i in gra.patches:
    # realizamos algunos cambios como centrar las etiquetas definir negrilla y tamaño
    gra.text( i.get_x()+ i.get_width() / 2, i.get_height(), \
            str(round((i.get_height()))), fontsize=15,
                color='black',va='bottom', ha="center", fontweight='bold')
plt.savefig('contratos por provincia')

# queremos determinar el monton de gasto en contratación por provincia
gasto_provincia = base.groupby(['PROVINCIA'])["Valor Inicial"].sum() # generamos una suma del gasto por provincia.
gasto_provincia
# para mayor comprensión de los datos expresamos el gasto en miles de millones de pesos
gasto = (gasto_provincia/1000000000)

# Creo un Data frame con el total de gasto en contratación de cada provincia y luego lo convierto en una lista para utilizarlo como label en la gráfica.
Gasto=pd.DataFrame(gasto)
G=Gasto.values.tolist()

# Graficamos el monto total de gasto en contratación correspondiente a cada provincia.
gra = gasto.plot(kind='bar' , figsize = (20,9), fontsize = 15, legend=None);
gra.set_title("Gasto total en contratación por provincia", fontsize=40, fontname="Verdana")
# con el Data frame creado anteriormente correspondiente a los montos de gasto en contratación de cada provincia, lo vamos a agregar como el label de cada barra
for i in gra.patches:
    G.append(i.get_width())

# aqui se agrega el Data frame como etiqueta de cada barra
for i in gra.patches:
    # realizamos algunos cambios como centrar las etiquetas definir negrilla y tamaño 
    gra.text( i.get_x()+ i.get_width() / 2, i.get_height(), \
           "$"  + str(round(i.get_height(),1)), fontsize=10,
                color='black',va='bottom', ha="center")
    
plt.savefig('Gasto total en contratación por provincia')

# Ahora queremos determinar el procentaje del monto total de contratación correspondiente a cada provincia
gasto_total = sum(gasto) # expresamos el monto total del gasto en contratación en miles de millones de pesos
gasto_total

# determinamos el porcentaje del monto del gasto por provincia referente al gasto total en contratación
porcentaje_provincia = (gasto/gasto_total)*100

porcentaje_provincia = round(porcentaje_provincia,1)
porcentaje_provincia

# realizamos la grafica del porcentaje de gasto en contratación por provincia
gra = porcentaje_provincia.plot(kind='bar' , figsize = (20,10), fontsize = 15, legend=None);
gra.set_title("Porcentaje de gasto por provincia", fontsize=40, fontname="Verdana", fontweight='bold')

for i in gra.patches: # agregamos el Data frame creado anteriormente como labels para cada barra
    G.append(i.get_width())

for i in gra.patches:
    #  realizamos algunos cambios como centrar las etiquetas definir negrilla y tamaño 
    gra.text( i.get_x()+ i.get_width() / 2, i.get_height(), \
            str(round((i.get_height()),1))+" %", fontsize=10,
                color='black',va='bottom', ha="center", fontweight='bold')
    
plt.savefig('Porcentaje de gasto por provincia')

# realizamos la agregación por modalidad de contratación y conteo de contratos y lo convertimos en un Data Frame
contratos_modalidad = base.groupby(['Modalidad Selección'], axis=0)["Valor Inicial"].count()
contratos_modalidad.to_frame()
cont_moda=contratos_modalidad.reset_index(level=0)
cont_moda
# realizamos la agregación por modalidad de contratación y suma de contratos y lo convertimos en un Data Frame
contratos_modalidad2 = base.groupby(['Modalidad Selección'], axis=0)["Valor Inicial"].sum()
contratos_modalidad2.to_frame()
contratos_modalidad2 = (contratos_modalidad2/1000000000)
cont_moda2=contratos_modalidad2.reset_index(level=0)
cont_moda2
# realizamos el merge entre el número de contratos y gasto de contración
cont_mod_ = pd.merge(cont_moda, cont_moda2, how="outer", on="Modalidad Selección")
cont_mod_


cont_mod_.columns = ['Modalidad Selección','contratos', 'Valor Inicial']
cont_mod_ = cont_mod_.round(1)
cont_mod_


# queremos generar un Dataframe que nos indique el número de contratos y gasto en contratación por provincia

# realizamos la agregación por ConcursodeMéritos-Modalidaddecontratación y número de contratos, y lo convertimos en un Data Frame
Concurso_meritos = base[base["Modalidad Selección"]=="Concurso de Méritos"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].count()
Concurso_meritos.to_frame()
Con_meritos=Concurso_meritos.reset_index(level=0)
Con_meritos
# realizamos la agregación de contratos y gasto en contratación y lo convertimos en un Data Frame
Concurso_meritos2 = base[base["Modalidad Selección"]=="Concurso de Méritos"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].sum()
Concurso_meritos2.to_frame()
Concurso_meritos2 = (Concurso_meritos2/1000000000)
Con_meritos2=Concurso_meritos2.reset_index(level=0)
# realizamos el merge de los contratos y la suma de gasto en contratación por provincia 
Con_meritos = pd.merge(Con_meritos, Con_meritos2, how="outer", on="PROVINCIA")
Con_meritos

# realizamos la agregación por InvitaciónDirecta-Modalidaddecontratación y número de contratos, y lo convertimos en un Data Frame
Invitación_Directa = base[base["Modalidad Selección"]=="Invitación Directa"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].count()
Invitación_Directa.to_frame()
Inv_directa=Invitación_Directa.reset_index(level=0)
Inv_directa
# realizamos la agregación de contratos y gasto en contratación y lo convertimos en un Data Frame
Invitación_Directa2 = base[base["Modalidad Selección"]=="Invitación Directa"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].sum()
Invitación_Directa2.to_frame()
Invitación_Directa2 = (Invitación_Directa2/1000000000)
Inv_directa2=Invitación_Directa2.reset_index(level=0)
# realizamos el merge de los contratos y la suma de gasto en contratación por provincia 
Inv_directa = pd.merge(Inv_directa, Inv_directa2, how="outer", on="PROVINCIA")
Inv_directa

# realizamos la agregación por ContrataciónDirecta-Modalidaddecontratación y número de contratos, y lo convertimos en un Data Frame
Contratación_Directa = base[base["Modalidad Selección"]=="Contratación Directa"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].count()
Contratación_Directa.to_frame()
Con_directa=Contratación_Directa.reset_index(level=0)
Con_directa
# realizamos la agregación de contratos y gasto en contratación y lo convertimos en un Data Frame
Contratación_Directa2 = base[base["Modalidad Selección"]=="Contratación Directa"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].sum()
Contratación_Directa2.to_frame()
Contratación_Directa2 = (Contratación_Directa2/1000000000)
Con_directa2=Contratación_Directa2.reset_index(level=0)
# realizamos el merge de los contratos y la suma de gasto en contratación por provincia 
Con_directa = pd.merge(Con_directa, Con_directa2, how="outer", on="PROVINCIA")
Con_directa

# realizamos la agregación por ConvocatoriaPública-Modalidaddecontratación y número de contratos, y lo convertimos en un Data Frame
Convocatoria_Pública = base[base["Modalidad Selección"]=="Convocatoria Pública - Decreto 092/2017"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].count()
Convocatoria_Pública.to_frame()
Con_Publica=Convocatoria_Pública.reset_index(level=0)
Con_Publica
# realizamos la agregación de contratos y gasto en contratación y lo convertimos en un Data Frame
Convocatoria_Pública2 = base[base["Modalidad Selección"]=="Convocatoria Pública - Decreto 092/2017"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].sum()
Convocatoria_Pública2.to_frame()
Convocatoria_Pública2 = (Convocatoria_Pública2/1000000000)
Con_Publica2=Convocatoria_Pública2.reset_index(level=0)
# realizamos el merge de los contratos y la suma de gasto en contratación por provincia 
Con_Publica = pd.merge(Con_Publica, Con_Publica2, how="outer", on="PROVINCIA")
Con_Publica

# realizamos la agregación por InvitaciónDirecta-Modalidaddecontratación y número de contratos, y lo convertimos en un Data Frame
Invitación_Cerrada = base[base["Modalidad Selección"]=="Invitación Cerrada"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].count()
Invitación_Cerrada.to_frame()
Inv_Cerrada=Invitación_Cerrada.reset_index(level=0)
Inv_Cerrada
# realizamos la agregación de contratos y gasto en contratación y lo convertimos en un Data Frame
Invitación_Cerrada2 = base[base["Modalidad Selección"]=="Invitación Cerrada"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].sum()
Invitación_Cerrada2.to_frame()
Invitación_Cerrada2 = (Invitación_Cerrada2/1000000000)
Inv_Cerrada2=Invitación_Cerrada2.reset_index(level=0)
# realizamos el merge de los contratos y la suma de gasto en contratación por provincia 
Inv_Cerrada = pd.merge(Inv_Cerrada, Inv_Cerrada2, how="outer", on="PROVINCIA")
Inv_Cerrada

# realizamos la agregación por InvitaciónPública-Modalidaddecontratación y número de contratos, y lo convertimos en un Data Frame
Invitación_Pública = base[base["Modalidad Selección"]=="Invitación Pública"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].count()
Invitación_Pública.to_frame()
Inv_Pública=Invitación_Pública.reset_index(level=0)
Inv_Pública
# realizamos la agregación de contratos y gasto en contratación y lo convertimos en un Data Frame
Invitación_Pública2 = base[base["Modalidad Selección"]=="Invitación Pública"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].sum()
Invitación_Pública2.to_frame()
Invitación_Pública2 = (Invitación_Pública2/1000000000)
Inv_Pública2=Invitación_Pública2.reset_index(level=0)
# realizamos el merge de los contratos y la suma de gasto en contratación por provincia 
Inv_Pública = pd.merge(Inv_Pública, Inv_Pública2, how="outer", on="PROVINCIA")
Inv_Pública

# realizamos la agregación por LicitacionesPúblicas-Modalidaddecontratación y número de contratos, y lo convertimos en un Data Frame
Licitaciones_Pública = base[base["Modalidad Selección"]=="Licitaciones Públicas"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].count()
Licitaciones_Pública.to_frame()
Lic_Pública=Licitaciones_Pública.reset_index(level=0)
Lic_Pública
# realizamos la agregación de contratos y gasto en contratación y lo convertimos en un Data Frame
Licitaciones_Pública2 = base[base["Modalidad Selección"]=="Licitaciones Públicas"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].sum()
Licitaciones_Pública2.to_frame()
Licitaciones_Pública2 = (Licitaciones_Pública2/1000000000)
Lic_Pública2=Licitaciones_Pública2.reset_index(level=0)
# realizamos el merge de los contratos y la suma de gasto en contratación por provincia 
Lic_Pública = pd.merge(Lic_Pública, Lic_Pública2, how="outer", on="PROVINCIA")
Lic_Pública

# realizamos la agregación por MínimaCuantía-Modalidaddecontratación y número de contratos, y lo convertimos en un Data Frame
Mínima_Cuantía = base[base["Modalidad Selección"]=="Mínima Cuantía"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].count()
Mínima_Cuantía.to_frame()
Mín_Cuantía=Mínima_Cuantía.reset_index(level=0)
Mín_Cuantía
# realizamos la agregación de contratos y gasto en contratación y lo convertimos en un Data Frame
Mínima_Cuantía2 = base[base["Modalidad Selección"]=="Mínima Cuantía"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].sum()
Mínima_Cuantía2.to_frame()
Mínima_Cuantía2 = (Mínima_Cuantía2/1000000000)
Mín_Cuantía2=Mínima_Cuantía2.reset_index(level=0)
# realizamos el merge de los contratos y la suma de gasto en contratación por provincia 
Mín_Cuantía = pd.merge(Mín_Cuantía, Mín_Cuantía2, how="outer", on="PROVINCIA")
Mín_Cuantía

# realizamos la agregación por RégimenEspecial-Modalidaddecontratación y número de contratos, y lo convertimos en un Data Frame
Régimen_Especial = base[base["Modalidad Selección"]=="Régimen Especial"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].count()
Régimen_Especial.to_frame()
Rég_Especial=Régimen_Especial.reset_index(level=0)
Rég_Especial
# realizamos la agregación de contratos y gasto en contratación y lo convertimos en un Data Frame
Régimen_Especial2 = base[base["Modalidad Selección"]=="Régimen Especial"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].sum()
Régimen_Especial2.to_frame()
Régimen_Especial2 = (Régimen_Especial2/1000000000)
Rég_Especial2=Régimen_Especial2.reset_index(level=0)
# realizamos el merge de los contratos y la suma de gasto en contratación por provincia 
Rég_Especial = pd.merge(Rég_Especial, Rég_Especial2, how="outer", on="PROVINCIA")
Rég_Especial

# realizamos la agregación por SelecciónAbreviada-Modalidaddecontratación y número de contratos, y lo convertimos en un Data Frame
Selección_Abreviada = base[base["Modalidad Selección"]=="Selección Abreviada"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].count()
Selección_Abreviada.to_frame()
Sel_Abreviada=Selección_Abreviada.reset_index(level=0)
Sel_Abreviada
# realizamos la agregación de contratos y gasto en contratación y lo convertimos en un Data Frame
Selección_Abreviada2 = base[base["Modalidad Selección"]=="Selección Abreviada"].groupby(['PROVINCIA'], axis=0)["Valor Inicial"].sum()
Selección_Abreviada2.to_frame()
Selección_Abreviada2 = (Selección_Abreviada2/1000000000)
Sel_Abreviada2=Selección_Abreviada2.reset_index(level=0)
# realizamos el merge de los contratos y la suma de gasto en contratación por provincia 
Sel_Abreviada = pd.merge(Sel_Abreviada, Sel_Abreviada2, how="outer", on="PROVINCIA")
Sel_Abreviada

# hacemos el merge uno a uno empezando por el gasto total en contratación y cada una de las modalidades de contratación
por_modalidad= pd.merge(Con_meritos, Inv_directa, how='outer',  on='PROVINCIA')
por_modalidad= pd.merge(por_modalidad,Con_directa,how='outer',  on='PROVINCIA')
por_modalidad= pd.merge(por_modalidad,Con_Publica,how='outer',  on='PROVINCIA')
por_modalidad= pd.merge(por_modalidad,Inv_Cerrada,how='outer',  on='PROVINCIA')
por_modalidad= pd.merge(por_modalidad,Inv_Pública,how='outer',  on='PROVINCIA')
por_modalidad= pd.merge(por_modalidad,Lic_Pública,how='outer',  on='PROVINCIA')
por_modalidad= pd.merge(por_modalidad,Mín_Cuantía,how='outer',  on='PROVINCIA')
por_modalidad= pd.merge(por_modalidad,Rég_Especial,how='outer',  on='PROVINCIA')
por_modalidad= pd.merge(por_modalidad,Sel_Abreviada,how='outer',  on='PROVINCIA')
por_modalidad

# vamos a renombrar las columnas para identificar la inversión por convenio
por_modalidad.columns = ['PROVINCIA','Concurso de Méritos', 'Con_meritos','Invitación Directa', 'Inv_directa','Contratación Directa', 'Con_directa','Convocatoria Pública - Decreto 092/2017', 'Con_Publica','Invitación Cerrada', 'Inv_Cerrada', 'Invitación Pública', 'Inv_Pública', 'Licitaciones Públicas', 'Lic_Pública', 'Mínima Cuantía', 'Mín_Cuantía', 'Régimen Especial', 'Rég_Especial', 'Selección Abreviada', 'Sel_Abreviada']

# los valores que tienen NaN se convierten a 0
por_modalidad.fillna(0, inplace=True)

# Redondear los valores a un solo decimal
por_modalidad=por_modalidad.round(1)
por_modalidad

# Cuadro con la distribución de los montos de la contratación segun la modalidad de contratación por cada una de las privincias
in_modalidad = por_modalidad.drop(columns=['Concurso de Méritos','Invitación Directa','Contratación Directa','Convocatoria Pública - Decreto 092/2017', 'Invitación Cerrada', 'Invitación Pública', 'Licitaciones Públicas', 'Mínima Cuantía', 'Régimen Especial', 'Selección Abreviada'])
in_modalidad

# vamos a realizar el data frame con solo el número de contratos por modalidad de contratación
pro_modalidad = por_modalidad.drop(columns=['Con_meritos','Inv_directa','Con_directa', 'Con_Publica', 'Inv_Cerrada','Inv_Pública', 'Lic_Pública', 'Mín_Cuantía', 'Rég_Especial', 'Sel_Abreviada'])
pro_modalidad

# graficar # de proyectos por vigencia de cada departamento
ay = pro_modalidad.plot.bar(stacked=True, figsize=(26,13), fontsize = 20)

ay.set_title("Número de contratos por modalidad de contratación", fontsize=40, fontname="Verdana")

ay.set_xticklabels(pro_modalidad["PROVINCIA"])

ay.legend(fontsize=20);

plt.savefig('Número de contratos por modalidad de contratación - PROVINCIA')

# graficas del gasto en contratación por modalidad de contratación de cada provincia
ay = in_modalidad.plot.bar(stacked=True, figsize=(26,13), fontsize = 20)

ay.set_title("Gasto en Contratación por modalidad de contratación", fontsize=40, fontname="Verdana")

ay.set_xticklabels(in_modalidad["PROVINCIA"])

ay.legend(fontsize=20);

plt.savefig('Gasto en contratación por modalidad de contratación - Provincia')