#### Clear workspace ###
rm(list=ls(all=TRUE))

###############################
### Custom functions to run ###
###############################

library(reshape)
instant_pkgs <- function(pkgs) { 
  pkgs_miss <- pkgs[which(!pkgs %in% installed.packages()[, 1])]
  if (length(pkgs_miss) > 0) {
    install.packages(pkgs_miss)
  }
  if (length(pkgs_miss) == 0) {
    message("\n ...Packages were already installed!\n")
  }
  pkgs_miss <- pkgs[which(!pkgs %in% installed.packages()[, 1])]
  if (length(pkgs_miss) > 0) {
    install.packages(pkgs_miss)
  }
  attached <- search()
  attached_pkgs <- attached[grepl("package", attached)]
  need_to_attach <- pkgs[which(!pkgs %in% gsub("package:", "", attached_pkgs))]
  
  if (length(need_to_attach) > 0) {
    for (i in 1:length(need_to_attach)) require(need_to_attach[i], character.only = TRUE)
  }
  
  if (length(need_to_attach) == 0) {
    message("\n ...Packages were already loaded!\n")
  }
}

## Start Code ###
### Install Pckges
instant_pkgs("RCurl")
instant_pkgs("XML")
instant_pkgs("xml2")
instant_pkgs("stringr")
instant_pkgs("RSelenium")
instant_pkgs("httr")
instant_pkgs("jsonlite")
instant_pkgs("xml2")
instant_pkgs("rvest")
instant_pkgs("dplyr")
instant_pkgs("data.table")



#Abrir el explorador

#driver <- rsDriver(browser=c("chrome"), chromever="74.0.3729.6", port=6666L)


driver <- rsDriver(browser=c("chrome"), chromever="74.0.3729.6", port=1001L)
remDr <- driver[["client"]]


remDr$navigate("http://siaobserva.auditoria.gov.co/guess/informe_rendidos_guess.aspx")
#remDr$findElement(using = "xpath", "//select[//*[@id='ctl00_contentMain_cmbDepartamento']]/option[@value = '3']")$clickElement()


#remDr$getCurrentUrl()

#Sacar la lista de todos los departamentos
departamentos <- remDr$findElement(using = "xpath", '//*[@id="ctl00_contentMain_cmbDepartamento"]')
departamentos <- departamentos$getElementAttribute("outerHTML")[[1]]
departamentos <- iconv(departamentos, to = "utf8")
departamentos <- repair_encoding(departamentos)
departamentos <- htmlTreeParse(departamentos, useInternalNodes = TRUE, encoding = "utf8") 
departamentos.value <- unlist(xpathApply(departamentos, '//*[@value]', xmlGetAttr, 'value'))
departamentos.name <- unlist(xpathApply(departamentos, '//*[@value]', xmlValue, 'value'))
departamentos <- data.table("state" = departamentos.name, "value" = departamentos.value) %>%
  .[state != ""]

departamentos <- departamentos[value %in% c(3, 11)]

remDr$close()

z <- 1
lista <- list()
for (i in 1:nrow(departamentos)) {tryCatch({
  
  felipe <- 2200+i  %>% as.integer()
  driver <- rsDriver(browser=c("chrome"), chromever="74.0.3729.6", port=as.integer(felipe))
  remDr <- driver[["client"]]
  
  
  j <- departamentos[i, value]
  h <- departamentos[i, state]
  remDr$navigate("http://siaobserva.auditoria.gov.co/guess/informe_rendidos_guess.aspx")

  Sys.sleep(3)
  
  temp1 <- paste0("//*[(@id = 'ctl00_contentMain_cmbDepartamento')]/option[@value = '", j, "']")
  
  option <- remDr$findElement(using = "xpath", temp1)
  option <- remDr$findElement(using = "xpath", temp1)
  option <- remDr$findElement(using = "xpath", temp1)
  
  option$clickElement()  
  
  Sys.sleep(3)
  
  #Sacar cada uno de los municipios
  #Sacar la lista de todos los departamentos
  municipios <- remDr$findElement(using = "xpath", "//*[@id='ctl00_contentMain_cmbMunicipio']")
  municipios <- remDr$findElement(using = "xpath", "//*[@id='ctl00_contentMain_cmbMunicipio']")
  municipios <- remDr$findElement(using = "xpath", "//*[@id='ctl00_contentMain_cmbMunicipio']")
  municipios <- remDr$findElement(using = "xpath", "//*[@id='ctl00_contentMain_cmbMunicipio']")
  municipios <- municipios$getElementAttribute("outerHTML")[[1]]
  municipios <- iconv(municipios, to = "utf8")
  municipios <- repair_encoding(municipios)
  remDr$close()
  # Convert to xml
  municipios <- htmlTreeParse(municipios, useInternalNodes = TRUE, encoding = "utf8") # parse string into HTML tree
  # Extract names and values
  municipios.value <- unlist(xpathApply(municipios, '//*[@value]', xmlGetAttr, 'value'))
  municipios.name <- unlist(xpathApply(municipios, '//*[@value]', xmlValue, 'value'))  
  municipios <- data.table("state" = municipios.name, "value" = municipios.value) %>%
    .[state != ""]  %>%
    .[state != "Todos"] 
    
  municipios[, departamento := get("h")]
  municipios[, departamento_code := get("j")]  
  
  lista[[z]] <- municipios
  z <- 1 + z
  rm(h, j, municipios, municipios.name, municipios.value)
  

  }, error=function(e){})
}


lista <- rbindlist(lista)
rm(departamentos, z, departamentos.name, departamentos.value, i, option, remDr, temp1)


salida <- list()
z <- 1
rm(driver)

for ( i in 1:nrow(lista)) {
  
  felipe <- 3011+i  %>% as.integer()
  
  driver <- rsDriver(browser=c("chrome"), chromever="74.0.3729.6", port=as.integer(felipe))
  remDr <- driver[["client"]]
  remDr$maxWindowSize()
  j <- lista[i, departamento_code]
  h <- lista[i, value]
  remDr$navigate("http://siaobserva.auditoria.gov.co/guess/informe_rendidos_guess.aspx")
  #temp <- departamentos[i, value]
  temp1 <- paste0("//*[(@id = 'ctl00_contentMain_cmbDepartamento')]/option[@value = '", j, "']")
  option <- remDr$findElement(using = "xpath", temp1)
  option <- remDr$findElement(using = "xpath", temp1)
  option <- remDr$findElement(using = "xpath", temp1)
  
  option$clickElement()  
  
  
  #Ciudad
  temp.municipio1 <- paste0("//*[@id='ctl00_contentMain_cmbMunicipio']/option[@value = '", 
                            h, "']")
  
  Sys.sleep(2)
  
  for( y in 1:5) {
  option.municipio <- remDr$findElement(using = "xpath", temp.municipio1)
  }
  option.municipio$clickElement()  
  
  
  #Fecha de inicio
  for( y in 1:15) {
    fecha_inicio <- remDr$findElement(using = "xpath", "//*[@id='ctl00_contentMain_txtFechaDesdeProcesoSel']")
  }
  fecha_inicio$clickElement()
  
  fecha_inicio <- remDr$findElement(using = "xpath", "//*[@id='ctl00_contentMain_txtFechaDesdeProcesoSel']")
  for (y in 1:5) {
  fecha_inicio <- remDr$findElement(using = "xpath", 
                                    "//*[@id='ui-datepicker-div']/div[1]/div/div/select[2]/option[@value = '2016']")
  }
  fecha_inicio$clickElement()

  for (y in 1:5) {    
  fecha_inicio <- remDr$findElement(using = "xpath", 
                                    "//*[@id='ui-datepicker-div']/div[1]/div/div/select[1]/option[@value = '0']")  
  }
  fecha_inicio$clickElement()
  

  fecha_inicio <- remDr$findElement(using = "xpath", 
                                    "//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[1]/td[5]/a")
  
  fecha_inicio$clickElement()

  for( y in 1:15) {
    
  fecha_fin <- remDr$findElement(using = "xpath", "//*[@id='ctl00_contentMain_txtFechaHastaProcesoSel']")
  
  }


  fecha_fin$clickElement()
  
  fecha_fin <- remDr$findElement(using = "xpath", "//*[@id='ctl00_contentMain_txtFechaHastaProcesoSel']")
  
  fecha_fin <- remDr$findElement(using = "xpath", 
                                 "//*[@id='ui-datepicker-div']/div[1]/div/div/select[1]/option[5]")
  
  fecha_fin$clickElement()
  
  fecha_fin <- remDr$findElement(using = "xpath", 
                                 "//*[@id='ui-datepicker-div']/div[1]/div/div/select[1]/option[5]")
  
  fecha_fin <- remDr$findElement(using = "xpath", 
                                 "//*[@id='ui-datepicker-div']/div[3]/table/tbody/tr[2]/td[5]/a")
  
  fecha_fin$clickElement()
  
  fecha_fin <- remDr$findElement(using = "xpath", 
                                 "//*[@id='ui-datepicker-div']/div[3]/table/tbody/tr[2]/td[5]/a")
  
  for (f in 1:5) {
  felipe_ <- remDr$findElement(using = "xpath", "//*[@id='ctl00_contentMain_btnConsultarProcesoSel']")
  }
  
  felipe_$clickElement()
  
  webElem <- remDr$findElement("css", "body")
  webElem$sendKeysToElement(list(key = "home"))
  for(f in 1:15){
    remDr$sendKeysToActiveElement(list(key = "down_arrow"))
  }  
  
  Sys.sleep(2)
  
  aux <- NULL    
  while(is.numeric(aux) == FALSE) {  
    
    codigo <- htmlParse(remDr$getPageSource()[[1]]) 
    aux <- xpathSApply(codigo, '//*[@id="ctl00_contentMain_spanResultadoLinea1"]', xmlValue) %>%
      gsub("(.*\\s{1,}?).*", "\\1", .) %>%
      gsub("\\s{1,}$", "", .) %>%
      as.numeric()
  }  
  
  if (aux != 0) {
    
    
    #Click en consultar
    remDr$findElement(using = "xpath", "//*[@id='tblResultadosInformeEntidades']/tbody/tr/td[5]/button/i")$clickElement()
    #Dejar la sisión en espera
    Sys.sleep(30)
    
    #remDr$findElement(using = "xpath", '//*[@id="ToolTables_tblResultadosInformeEntidades_0"]/span')$clickElement()
    
    #remDr$findElement(using = "xpath", '//*[@id="ToolTables_tblResultadosInformeEntidades_1"]')$clickElement()
    
    remDr$findElement(using = "xpath", '//*[@id="tblResultadosInformeEntidades_length"]/label/select/option[4]')$clickElement()
    
    Sys.sleep(5)
    
    for ( f in 1:5){
    pg <- remDr$getPageSource()
    }
    remDr$close()
    doc <- read_html(pg[[1]])
    st <- html_nodes(doc, "table") %>%
      html_table(fill = TRUE) %>%
      .[[1]] %>%
      data.table()
    primero <- lista[i, state]
    segundo <- lista[i, departamento]
    

    st[, municipio := get("primero")]
    st[, municipio_codigo := get("h")]
    st[, departamento := get("segundo")]
    st[, departamento_codigo := get("j")]
    
    salida[[z]] <- st
    
    rm(primero, segundo, h, j, pg, doc, st)
    
    z <- z+1
    

  }


}

salida <- unique(salida)


base_final <- rbindlist(salida)


limpieza <- function(col) {
  
  
  col <- gsub("\\$", "", col) %>%
    gsub("\\.", "", .) %>%
    gsub("\\s{1,}", "", .) %>%
    as.numeric(.)
  
  
}

cols <- c("VALOR INIC.CONTRATO")

base_final[, (cols) := lapply(.SD, limpieza), .SDcols = cols]



  


write.table(base_final, file = "D:/Documentos/faca/base1.csv", row.names = FALSE, col.names = TRUE, sep = ",")







  