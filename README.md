
# Contratación estatal en el departamento de Cundinamarca y Bogotá

# Descripción y Motivación
<p align="justify">El SIA-OBSERVA es un aplicativo de las contralorías regionales en el cual cada una de las entidades rinde informe de contratación cada mes vencido.Dicha información permite evidenciar que tipo de gasto predomina en cada uno de los municipios, y da evidencia de la calidad del gasto que se realiza por las distintas entidades. Los entes de control realizan una labor de vital importancia para afrontar el problema de corrupción que tanto daño le ha hecho a un país en proceso de desarrollo como Colombia. En este trabajo abre las puertas para una investigación mucho más rigurosa, en la cual se puede llegar a justificar argumentos referentes a la abolición de la Ley de Garantías.</p> 
Algunas de las principales motivaciones del trabajo son: <br/>

•	Los métodos de recolección de datos tradicionales (ej. encuestas de hogares ) son costosos<br/>
•	El proceso de descarga de la información es engorroso sin técnicas sofisticadas.<br/>
•	La información consignada en el aplicativo de la contraloría es desconocida e inutilizada.<br/>
Métodos Usados:<br/> 
# 1.	Scrapping :<br/> 
-	La información de la contratacion realizada desde el 1° de enero de 2016 hasta la fecha se encuentra consignada en http://siaobserva.auditoria.gov.co/Login.aspx?redirect=Inicio <br/>
-	El Scrapping serealizo por medio de RStudio usando las siguientes librerías:
"RCurl", "XML", "xml2", "stringr", "RSelenium", "httr", "jsonlite", "xml2", "rvest", "dplyr", "data.table"
1.1.	Hice que el computador se ubicará al interior del aplicativo SIA – OBSERVA como usuario invitado.

<p align="justify">1.2.	Identifique cada código referente a cada Departamento y cree una lista en la cual cada departamento tenía su respectivo código. Se toma una primera decisión y es quedarme únicamente con la información de Cundinamarca y Bogotá. Se hace un loop para que el computador observe cada departamento e identifique su código. Se establece que lo anterior sea realizado cada 3 segundos y cierre cada pasada de loop porqué la página estaba protegida.</p>

<p align="justify">1.3.	Repito el procedimiento para los municipios, pero filtrados por Bogotá y Cundinamarca. una vez tengo la nueva lista, creo una base con la información de cada departamento con su respectivo municipio e identificaciones. Lo anterior tiene como finalidad ganar tiempo en términos de eficiencia y evitar realizar tantos clips como municipios existen en cada departamento.</p>

<p align="justify">1.4.	El siguiente filtro si se programaron clips para seleccionar las fechas que me interesaban analizar, y realizar una primera consulta. Llevo al computador a que identifique si existe algún contrato en el municipio seleccionado. De ser verdad que existen contratos, busco un filtro adicional para consultar la información pertinente a la contratación.</p>
  
# 2.	Almacenamiento de los datos:

-	Los datos de cada municipio se guardaban en una única base en formato csv. Se realizó la limpieza de la base, específicamente lo que fue el signo pesos y las comas del valor del contrato inicial. Posteriormente fue transformada la base a Excel.   
# 3.	Procesamiento de los datos : 
-	Una vez obtenida la base de datos  se adiciono la información de los municipios por provincia desde Excel, todos los cálculos, tablas y graficas de realizaron desde Python. Se trabajó con la información consignada en el aplicativo para lo corrido de vigencia 2019.
-	Las librerías usadas fueron:
a.	pandas como pd
b.	numpy como np
c.	matplotlib.pyplot como plt
d.	matplotlib.patches como patches
e.	matplotlib.path como path 

Resultados : 
![alt text](https://github.com/juanbarbosa219/Trabajo-final/blob/master/figura1.png)
En la Figura 1 observamos el número de contratos por provincia.  Se observa mayor número de contratos en Sabana Centro y Sabana de Occidente. Se observa menor número de contratos en la provincia del Bajo Magdalena y Medina.  En la Figura 2 se muestra el análisis del monto de contratación por provincia, se observa  que a pesar de que la provincia de Sumapaz tiene un total de contratos de 4.311 y que Bogotá de 3.478 cuando nos referimos en términos del monto total de contratación, Bogotá tiene mayor participación que el Sumapaz.

![alt text](https://github.com/juanbarbosa219/Trabajo-final/blob/master/Gasto%20total%20en%20contrataci%C3%B3n%20por%20provincia.png)

En la Figura 3 se observa la distribución en términos de porcentajes del monto de contratación por provincia.  La información es consistente con la expresada en la figura 2.  El 25.9% del monto total contratado en Bogotá y Cundinamarca se encuentra en la provincia de Sabana Centro. Según los objetos contratados de mayor monto. Seguido de Bogotá con el 17.7%. Medina y el Bajo Magdalena son las provincias con menor participación.

![alt text](https://github.com/juanbarbosa219/Trabajo-final/blob/master/Porcentaje%20de%20gasto%20por%20provincia.png)

La tabla1 deja en evidencia el número de contratos realizados y el monto contratado por cada modalidad de contratación. Sobresale las modalidades de contratación denominadas Contratación Directa y Régimen Especial. En el código de Python se podrán observar una extensión de la tabla 1, en la cual se muestran 3 tablas con la información de contratación por provincia, modalidad de contratación y números de contratos. 

![alt text](https://github.com/juanbarbosa219/Trabajo-final/blob/master/Tabla%20modalidad%20de%20contrataci%C3%B3n.png)

Con base a la extensión de la Tabla 1, se realizan las figuras 4 y 5. La figura 4 muestra el número de contratos por cada modalidad de contratación para cada una de las provincias. Como era de esperarse, sobresale el color referente a la contratación directa para cada una de las provincias. El color referente al régimen especial también juega un papel importante. 

![alt text](https://github.com/juanbarbosa219/Trabajo-final/blob/master/N%C3%BAmero%20de%20contratos%20por%20modalidad%20de%20contrataci%C3%B3n%20-%20PROVINCIA.png)
La figura 5 muestra la distribución del monto contratado para cada modalidad de contratación por provincia. Es interesante el rol protagónico que toma la variable referente a la licitación pública para las provincias de Sabana Centro y Occidente. En Bogotá, el monto de la contratación directa es muy importante. 

![alt text](https://github.com/juanbarbosa219/Trabajo-final/blob/master/Gasto%20en%20contrataci%C3%B3n%20por%20modalidad%20de%20contrataci%C3%B3n%20-%20Provincia.png)

